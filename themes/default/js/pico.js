/**
 * Pico's Default Theme - JavaScript helper
 *
 * Pico is a stupidly simple, blazing fast, flat file CMS.
 *
 * @author  Daniel Rudolf
 * @link    http://picocms.org
 * @license http://opensource.org/licenses/MIT The MIT License
 * @version 2.1
 */

function main()
{
    // capability CSS classes
    document.documentElement.className = 'js';

    // wrap tables
    var tables = document.querySelectorAll('#main > .container > table');
    for (var i = 0; i < tables.length; i++) {
        if (!/\btable-responsive\b/.test(tables[i].parentElement.className)) {
            var tableWrapper = document.createElement('div');
            tableWrapper.className = 'table-responsive';

            tables[i].parentElement.insertBefore(tableWrapper, tables[i]);
            tableWrapper.appendChild(tables[i]);
        }
    }

    // responsive menu
    var menu = document.getElementById('nav'),
        menuToggle = document.getElementById('nav-toggle');

    if (menu && menuToggle) {
        function toggleMenuEvent(event) {
            if (event.type === 'keydown') {
                if ((event.keyCode !== 13) && (event.keyCode !== 32)) {
                    return;
                }
            }

            event.preventDefault();

            if (menuToggle.getAttribute('aria-expanded') === 'false') {
                menuToggle.setAttribute('aria-expanded', 'true');
                utils.slideDown(menu, null, function () {
                    if (event.type === 'keydown') {
                        menu.focus();
                    }
                });
            } else {
                menuToggle.setAttribute('aria-expanded', 'false');
                utils.slideUp(menu);
            }
        }

        function onResizeEvent() {
            if (utils.isElementVisible(menuToggle)) {
                menu.className = 'hidden';
                menuToggle.addEventListener('click', toggleMenuEvent);
                menuToggle.addEventListener('keydown', toggleMenuEvent);
            } else {
                menu.className = '';
                menu.removeAttribute('data-slide-id');
                menuToggle.removeEventListener('click', toggleMenuEvent);
                menuToggle.removeEventListener('keydown', toggleMenuEvent);
            }
        }

        window.addEventListener('resize', onResizeEvent);
        onResizeEvent();
    }

    // κουμπί επιστροφής στην κορυφή: εμφανίζεται όταν το header βγαίνει από το viewport
    var backBtn = document.getElementById('back-to-top');
    var headerEl = document.getElementById('header');
    if (backBtn && headerEl) {
        function setBackToTopVisible(visible) {
            backBtn.classList.toggle('is-visible', visible);
            backBtn.setAttribute('tabindex', visible ? '0' : '-1');
            backBtn.setAttribute('aria-hidden', visible ? 'false' : 'true');
        }
        if ('IntersectionObserver' in window) {
            var io = new IntersectionObserver(function (entries) {
                entries.forEach(function (entry) {
                    setBackToTopVisible(!entry.isIntersecting);
                });
            }, { root: null, threshold: 0, rootMargin: '0px' });
            io.observe(headerEl);
        } else {
            var onScrollFallback = function () {
                var rect = headerEl.getBoundingClientRect();
                setBackToTopVisible(rect.bottom < 0);
            };
            window.addEventListener('scroll', onScrollFallback, { passive: true });
            onScrollFallback();
        }
        backBtn.addEventListener('click', function () {
            try {
                window.scrollTo({ top: 0, behavior: 'smooth' });
            } catch (e) {
                window.scrollTo(0, 0);
            }
        });
    }
}

main();
