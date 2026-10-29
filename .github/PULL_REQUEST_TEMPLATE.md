<!-- Please read the contributing guidelines before opening a pull request: https://github.com/sparontologies/.github/blob/main/CONTRIBUTING.md -->

Closes #<issue number>

## Summary of the changes

<!-- Delete the lines that do not apply. Use the IRIs of the terms. -->

* **Added terms:**
* **Modified terms:**
* **Deprecated terms:** <!-- with their replacement, if any -->
* **Other changes:** <!-- e.g. typos, broken links, documentation -->

## Checklist

<!-- Small corrections that do not change the model (typos, broken links, formatting) only need the first item. -->

- [ ] The change has been discussed and agreed in the linked issue.
- [ ] Only the `.ttl` file in `docs/current` has been edited by hand.
- [ ] New and modified terms follow the naming conventions and carry all the REQUIRED annotations of the term metadata checklist.
- [ ] No published term has been deleted or renamed (deprecated terms use `owl:deprecated true` and `vs:term_status`).
- [ ] `owl:versionIRI`, `owl:priorVersion`, `owl:versionInfo` and `dcterms:modified` have been updated, and `dcterms:modified` matches the date in `owl:versionIRI`.
- [ ] `CHANGELOG.md` has a new entry for this version.
- [ ] I am listed as `dc:creator` or `dc:contributor`.
- [ ] The report of the `validation.yml` workflow shows no errors.
- [ ] The `README.md` has been updated, if needed.
- [ ] A pull request on the [website repository](https://github.com/sparontologies/sparontologies.github.io) has been opened, if the description or the examples on the website are affected.
