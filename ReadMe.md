Template Data Model Project
===========================

This is a template project for creating a new Data Model using
[vodml tools](https://github.com/ivoa/vo-dml).

Steps to use it
---------------
1. decide on your DM name!
2. copy the repository
3. update the repository to use that name
   1. rename files to use that name rather than TemplateDM*
   2. edit the content of some files
      1. [settings.gradle.kts](settings.gradle.kts) first line needs editing
      2. [vo-dml/TemplateDM-v1.vodml-binding.xml](vo-dml/TemplateDM-v1.vodml-binding.xml) (or at least the renamed version) should have appropriate file and model names used.
      3. [doc/std/TemplateDM.tex](doc/std/TemplateDM.tex) should have the included description and model diagram names updated.
      4. [mkdocs_template.yml](./mkdocs_template.yml) (note that this should not be renamed) and [doc/site/index.md](./doc/site/index.md) should be customized and extended.
4. Use the tools ([more detail](https://ivoa.github.io/vo-dml/))
```
gradle test
```
should build the model and run tests against it.
```shell
gradle testSite
```
should build the site and make it available at http://localhost:8000
         