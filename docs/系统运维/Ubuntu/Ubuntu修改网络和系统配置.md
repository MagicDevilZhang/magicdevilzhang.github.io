# 修改主机名

```
sudo vim /etc/hostname
```

```
hadoop-vm-slave
```

```
sudo vim /etc/hosts
```

```
127.0.0.1    hadoop-vm-slave
```

```
sudo shutdown now -r
```

# 修改NetPlan

```
sudo vim /etc/netplan/00-installer-config.yaml
```

```
# This is the network config written by 'subiquity'
network:
  ethernets:
    ens33:
      dhcp4: false
      dhcp6: false
      addresses: [172.37.4.156/16]
      gateway4: 172.37.0.1
      nameservers:
        addresses: [223.5.5.5, 8.8.8.8]
  version: 2
```

```
sudo netplan apply
```

# 修改环境变量

```
sudo vim /etc/profile
```

```
export JAVA_HOME=/opt/jdk/
export PATH=$PATH:$JAVA_HOME/bin
```

```
sudo source /etc/profile
```

