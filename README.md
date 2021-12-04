# UdaConnect

## Instructions and commands on how to run the project

---

## Step 1: Prerequesites
These tools have to be installed first
* Docker
* Kubectl
* VirtualBox
* Vagrant

## Step 2: Initialize K3S
In the project root run:
```bash
$ vagrant up
```
Then
```bash
$ vagrant ssh
```

## Step 3: Retrieve the Kubernetes 
Run `sudo cat /etc/rancher/k3s/k3s.yaml` to print out the contents of the file.

```bash
$ sudo cat /etc/rancher/k3s/k3s.yaml
```
Copy the contents from the output issued from the previous command into your clipboard.

Type `exit` to exit the virtual OS and you will find yourself back in your computer's session. Create the file (or replace if it already exists) `~/.kube/config` and paste the contents of the `k3s.yaml` output here.

## Step 4: Install Kafka
* Install helm3
* Add the Bitnami charts repository to Helm
```bash
$ helm repo add bitnami https://charts.bitnami.com/bitnami
```
* Execute the following command to deploy an Apache Zookeeper
```bash
$ helm install zookeeper bitnami/zookeeper
```
* Execute the command below to deploy Apache Kafka replacing the ZOOKEEPER-SERVICE-NAME placeholder with the Apache Zookeeper service name obtained from the result of the previous command
```bash
$ helm install kafka bitnami/kafka --set externalZookeeper.servers=ZOOKEEPER-SERVICE-NAME
```

## Step 5: Deploy `kubectl`
```
$ kubectl apply -f deployment/
```

## Step 6: Seed the database
Seed the database with dummy data
```
$ sh scripts/run_db_command.sh <POD_NAME>
```

Run `kubectl get pods` to get the `postgres` pod.
Replace `POD_NAME` by the `postgres` pod.

The following page should now load on the browser:
* `http://localhost:30000/` - Frontend ReactJS Application

## Step 7: Test Apache Kafka
Create a pod to be used as Kafka client to inject some data (person or location)

```
kubectl run kafka-client --restart='Never' --image docker.io/bitnami/kafka:2.8.1-debian-10-r57 --namespace default --command -- sleep infinity
```
Execute the following command to get inside the pod shell
```
kubectl exec --tty -i kafka-client --namespace default -- bash
```
Start a producer by executing this command:
```
kafka-console-producer.sh --broker-list kafka-0.kafka-headless.default.svc.cluster.local:9092 --topic udaconnecttopic
```

Inject the json payload in the following format:
```
{'first_name':'Joel','last_name':'Mbiye','company_name':'HyPerfect SARL'}
```

Refresh the frontend page to see the person added.

## Step 8: gRPC
Run Python command using the file /modules/grpc/writer.py to add a person or a location to the database.

## Step 9: Postman
Open Postman and import [`postman.json`](docs/postman.json) collection to test the different API requests.

Notice how the results are being reflected on the frontend app.

---

