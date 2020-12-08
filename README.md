# xmr-to-btc

Command line Python 3 implementation of the [XMR.to](https://xmr.to/) REST API.

--- 

## How to Use

Call the utility according to the following template:

```shell
python xmr2btc.py <query> [params]
```

For example:
    
- to [query Order Parameters](https://xmrto-api.readthedocs.io/en/latest/api_v3.html#querying-order-parameters):

    ```shell
    python xmr2btc.py order_parameter_query
    ```

- to [create a new Order](https://xmrto-api.readthedocs.io/en/latest/api_v3.html#creating-a-new-order) immediately:

    ```shell
    python xmr2btc.py order_create "{'btc_dest_address': '1FhnVJi2V1k4MqXm2nHoEbY5LV7FPai7bb', 'amount': 0.1, 'amount_currency': 'BTC'}"
    ```

  or to use interactively:

    ```shell
    python xmr2btc.py order_create
    ```
