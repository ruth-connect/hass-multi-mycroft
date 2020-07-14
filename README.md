# hass-multi-mycroft

This component enables Home Assistant to notify multiple Mycroft voice assistants. You can specify as many Mycroft devices as you need, each with its own name and IP address.

## Installation

This can be easily installed with the Home Assistant Community Store (HACS) using the repository: [ruth-connect/hass-multi-mycroft](https://github.com/ruth-connect/hass-multi-mycroft)

Alternatively, manual installation by downloading the [custom_components/multi_mycroft](https://github.com/ruth-connect/hass-multi-mycroft/tree/master/custom_components/multi_mycroft) directory to the custom_components/multi_mycroft directory on your Home Assistant instance (generally _/config/custom_components/multi_mycroft_).

## Configuration

Multi Mycroft is configured in the configuration.yaml file under the *notify* section:
```yaml
notify:
  - name: mycroft_lounge
    platform: multi_mycroft
    ip_address: 192.168.1.11
    
  - name: mycroft_little_bedroom
    platform: multi_mycroft
    ip_address: 192.168.1.12

  - name: mycroft_kitchen
    platform: multi_mycroft
    ip_address: 192.168.1.13
```

Configuration variables:

  * **name** - Name of the Mycroft instance that you can refer to when sending notifications.
  * **ip_address** - IP address of the Mycroft instance.
