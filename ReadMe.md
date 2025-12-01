ExecutionBrokerDM
=================

This project expresses the executionBroker DM using VO-DML and [vodml tools](https://github.com/ivoa/vo-dml).

The real source is in [model/ExecutionBrokerDM-v1.vodsl](model/ExecutionBrokerDM-v1.vodsl).

The [ExecutionBrokerDM documentation](https://pahjbo.github.io/ExecutionBrokerDM/) is published on GitHub pages with CI.


```shell
gradle vodslToVodml
```
will create the VO-DML

```shell
gradle test
```
should build the model and run tests against it.

```shell
gradle testSite
```

should build the site and make it available at http://localhost:8000
      

## Conversion from Calycopis Schema

Conversion from the OpenAPI schema defined in https://github.com/ivoa/Calycopis-schema

```
npx @redocly/cli bundle Calycopis-broker.yaml > single.yaml
```

and then running

```shell
python3 openapi2vodsl.py
```

and then some manual editing