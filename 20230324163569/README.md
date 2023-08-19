# Messaging service (Pub/Sub)

GCP Pub/Sub: asynchronous messaging queue service that allows to loosely couple application components.

In simple words, general message queue allows you to queue up actions and have part of your application keep running even if another portion were to go down, that way the messages are sitting there waiting and once it comes back up it can continue processing with nothing lost, that's super important in "decoupled" (micro-services) architecture.

If comparing with AWS then PUB/SUB = SQS+SNS

Source: [GCP Pub/Sub](https://cloud.google.com/pubsub/docs/)
