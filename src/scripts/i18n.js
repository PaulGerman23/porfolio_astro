import { translations } from '../i18n/translations';

const LANGUAGE_KEY = 'portfolio_lang';
const DEFAULT_LANG = 'es';

export function getInitialLanguage() {
    if (typeof localStorage !== 'undefined') {
        const savedLang = localStorage.getItem(LANGUAGE_KEY);
        if (savedLang) return savedLang;
    }
    return DEFAULT_LANG;
}

export function setLanguage(lang) {
    if (typeof localStorage !== 'undefined') {
        localStorage.setItem(LANGUAGE_KEY, lang);
    }

    // Update HTML lang attribute
    document.documentElement.lang = lang;

    // Update all text elements
    updatePageContent(lang);

    // Update toggle buttons state if any
    updateToggleState(lang);
}

function updatePageContent(lang) {
    const elements = document.querySelectorAll('[data-i18n]');

    elements.forEach(element => {
        const key = element.getAttribute('data-i18n');
        if (translations[lang] && translations[lang][key]) {
            // Check if it's an input with placeholder
            if (element.tagName === 'INPUT' || element.tagName === 'TEXTAREA') {
                if (element.hasAttribute('placeholder')) {
                    element.placeholder = translations[lang][key];
                }
            } else {
                element.textContent = translations[lang][key];
            }
        }
    });
}

function updateToggleState(lang) {
    const toggles = document.querySelectorAll('.lang-toggle');
    toggles.forEach(toggle => {
        const langSpan = toggle.querySelector('.lang-text');
        if (langSpan) {
            langSpan.textContent = lang.toUpperCase();
        }
    });
}

// Initialize
export function initI18n() {
    const initialLang = getInitialLanguage();
    setLanguage(initialLang);

    // Setup click listeners for toggles
    const toggles = document.querySelectorAll('.lang-toggle');
    toggles.forEach(toggle => {
        toggle.addEventListener('click', (e) => {
            e.preventDefault();
            const currentLang = getInitialLanguage();
            const newLang = currentLang === 'es' ? 'en' : 'es';
            setLanguage(newLang);
        });
    });
}
