/** @odoo-module */
import {patch} from "@web/core/utils/patch";
import {onWillStart} from "@odoo/owl";

var TranslationDialog = require("@web/views/fields/translation_dialog");

patch(TranslationDialog.TranslationDialog.prototype, 'deepl', {
    setup() {
        this.props.company_id = null;
        this.props.deepl_enabled = false;

        onWillStart(async () => {
                const company_fields = await this._getCompanyFields();
                this.props.user_lang = company_fields.user_lang;
                this.props.deepl_enabled = company_fields.deepl_enabled;
                this.props.company_id = company_fields.company_id;
            }
        );

        this._super();
    },

    async _getCompanyFields() {
        return this.orm.call('deepl.account', 'rpc_get_current_company_lang', [false]);
    },

    async onClickTranslateAll(ev) {
            // Filter out english and user lang.
            var $translate_btns = $('.o_translation_dialog').find('button:not([data-lang*="en_US"]):not([data-is-user-lang="true"])');
            var index = 0; // Keep track of the current button index

            var translateNext = () => {
                if (index < $translate_btns.length) {
                    var btn = $translate_btns[index];
                    $(btn).click();
                    index++; // Move to the next button
                } else {
                    // Remove the event listener once all translations are done
                    $(document).off('translationCompleted', translateNext);
                }
            };

            // Listen for the custom event to trigger the next translation
            $(document).on('translationCompleted', translateNext);

            // Start the first translation
            translateNext();
    },

    async onClickTranslate(ev) {
        var $btn = $(ev.currentTarget);
        var inputType = $btn.data('field-type');
        var fieldType = inputType === 'textarea' ? 'html' : 'text';
        // var $currentInput = $btn.parent().find(inputType);
        if (this.props.deepl_enabled) {
            $btn.addClass('disabled');
            await this._translateDeepl($btn, inputType, fieldType);
            $btn.removeClass('disabled');
        }
    },

    async _translateDeepl($translateBtn, inputType, fieldType) {
        /**
         * @param {Object} $translateBtn - The jQuery object of the translation button.
         * @param {String} inputType - The type of input field. Can be 'input' or 'textarea'
         */
        let target_lang = $translateBtn.data('lang');
        let source_lang = $translateBtn.data('base-lang');
        if (!source_lang) {
            console.error('Base translation language not found');
            return;
        }
        let $currentInput = $translateBtn.parent().find(inputType);
        let $source_input = $('.o_translation_dialog').find('button[data-lang="' + source_lang + '"]').parent().find(inputType);
        let source_text = $source_input.val();
        if (!source_text) {
            source_text = $translateBtn.closest('.row').find('.source')[0].innerText;
        }

        let self = this; // Capture the context of 'this'

        this.orm.call('deepl.account', 'rpc_translate', [false, target_lang, source_text, fieldType]).then(function (result) {
            if (result) {
                $currentInput.val(result);
                // .trigger('change') method doesn't work with Owl?
                self.updatedTerms[$currentInput.data('id')] = $currentInput.val();
                $currentInput.css('color', 'green');

            }
            // Emit custom event to indicate translation completion
            $(document).trigger('translationCompleted');
        });
    },

});
