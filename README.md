# Ιστορία — Pico

## Σκοπός του project

Αυτό το αποθετήριο είναι μια **στατική ιστοσελίδα παγκόσμιας ιστορίας** που στήνεται με το **[Pico CMS](https://picocms.org/)**: flat-file CMS χωρίς βάση δεδομένων — το περιεχόμενο είναι αρχεία Markdown κάτω από το `content/`, με μετα-δεδομένα YAML και πρότυπα Twig στο `themes/`.

Οι κύριες ενότητες (ελληνόγλωσσες συνοπτικές χρονολογίες) είναι:

- **Προϊστορία** — `content/prehistory/`
- **Αρχαία ιστορία** — `content/ancient_history/`
- **Μεσαίωνας** — `content/middle_ages/`
- **Νεότερη εποχή** — `content/recent_history/`
- **Σύγχρονη ιστορία** — `content/modern_history/`

Η αρχική επιλογή σελίδων βρίσκεται στο `content/index.md`. Ορισμένα τμήματα παράγουν μεγάλους πίνακες γεγονότων με βοηθητικά scripts Python (`gen.py`, και όπου υπάρχει `build_data.py`)· μετά την επεξεργασία των πηγών, τρέξτε τα από τον αντίστοιχο φάκελο για να ανανεωθεί το `index.md`.

## Απαιτήσεις

- **PHP** 7.2 ή νεότερο (συμβατό με Pico 2.1)
- **[Composer](https://getcomposer.org/)** 2.x
- Διακομιστής ιστού (Apache, nginx, ή ενσωματωμένος εξυπηρετητής PHP για τοπική ανάπτυξη)

## Εγκατάσταση

1. Κλωνοποίηση ή αντιγραφή του project σε έναν κατάλογο στον διακομιστή σας.

2. Εγκατάσταση εξαρτήσεων PHP:

   ```bash
   cd pico
   composer install
   ```

   Αν εμφανιστεί η ερώτηση:

   `Do you trust "picocms/composer-installer" to execute code and wish to enable it now? (writes "allow-plugins" to composer.json) [y,n,d,?]`

   απαντήστε **`n`**. Με **`y`** το εγκαθιστά plugin μπορεί να **ξανατρέξει εγκαταστάσεις θέματος** και να **ανακαταστήσει ή αντικαταστήσει** το προσαρμοσμένο `themes/default`· το **`n`** αποφεύγει αυτή τη συμπεριφορά.

   Αυτό θα δημιουργήσει το `vendor/` και θα εγκαταστήσει το Pico και τα σχετικά πακέτα σύμφωνα με το `composer.json`.

3. Ρύθμιση ιστοτόπου: αντιγράψτε το `config/config.yml.template` σε `config/config.yml` αν χρειάζεται, και ορίστε τουλάχιστον `site_title` (ή άλλες επιλογές σύμφωνα με την [τεκμηρίωση Pico](https://picocms.org/docs/#config)).

4. **Document root** του web server πρέπει να δείχνει στον **κατάλογο όπου βρίσκεται το `index.php`** (εδώ η ρίζα του project `pico/`, όχι υποφάκελος `content/`).

5. Δικαιώματα: βεβαιωθείτε ότι ο διακομιστής μπορεί να διαβάζει `content/`, `config/`, `themes/` και `vendor/`.

### Τοπική δοκιμή (γρήγορα)

```bash
cd pico
composer install   # στο prompt του composer-installer: n (βλ. παραπάνω)
php -S localhost:8080
```

Ανοίξτε στον browser: `http://localhost:8080`

## Περαιτέρω βοήθεια

- Επίσημη τεκμηρίωση Pico: [picocms.org/docs](https://picocms.org/docs/)
- Εγκατάσταση / αναβάθμιση upstream: [picocms/Pico — Install](https://github.com/picocms/Pico#install)

## Άδεια

Το upstream Pico και τα σχετικά πακέτα ακολουθούν τις άδειές τους (π.χ. MIT για το `picocms/pico-composer`). Το περιεχόμενο ιστορίας στο `content/` ανήκει στον ιδιοκτήτη του project.
