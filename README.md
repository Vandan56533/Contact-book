# Contact-book

#  Objective
To build a distributed contact book system using DDS (Data Distribution Service), where multiple nodes (e.g., clients and servers) can publish and subscribe to contact information updates in real time.

#How the Program Works
. System Architecture
- Publisher Node: Adds or updates contact information.
- Subscriber Node: Listens for changes and displays updated contact entries.
- Topic: "ContactInfo" — the shared channel for contact data.
- QoS Policies: Ensures reliable delivery and persistence of contact updates.
