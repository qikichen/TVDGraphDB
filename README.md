# TVDGraphDB

TVDGraphDB is an open-source distributed graph database designed for building powerful television show recommendation systems. With TVDGraphDB, you can leverage the simplicity and efficiency of a Breadth-First Search (BFS) algorithm to generate personalized show recommendations based on user preferences and viewing history.

## Table of Contents

- [Motivation] (#motivation)
- [Features](#features)
- [Objectives](#objectives)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Motivation
This project is all about scratching a bunch of itches: learning the ropes of open-source, diving into the realm of distributed systems and databases, tinkering with recommender systems, and dabbling in some machine learning. Plus, I'm a huge TV buff—give me cartoons, Western shows, anime, Asian dramas, you name it, I'm into it.

Most recommendation engines out there focus on what users like. And sure, that's cool. But I had this wild thought: what if we could dig deeper into the connections between shows themselves? Like, what makes one show lead to another? That's where the idea of using graphs came into play. Let's see where it takes us! 📺✨

## Features

- **BFS-Based Recommendations**: TVDGraphDB utilizes a simple BFS search algorithm to find the nearest neighbors of a given TV show, enabling quick and efficient recommendations.
- **Scalable Architecture**: Built on Pyro4, TVDGraphDB offers a distributed architecture that can scale to handle large datasets and high user loads.
- **Customizable**: TVDGraphDB is highly customizable, allowing you to adjust parameters, algorithms, and data models to suit your specific requirements.
- **Integration**: Integrate TVDGraphDB with your existing systems, including frontend applications, recommendation engines, and backend APIs, to enhance the user experience.

## Objectives 

_Note: I want to increase my objectives as time goes on, for now this is what I am working on_

1. **Implement Graph BFS Search for Recommendation**: Utilize the BFS algorithm to efficiently traverse the graph of TV shows and generate relevant recommendations based on user queries and preferences.[In Progress]
   
2. **Allow Distribution Across Multiple Nodes**: Design and implement a distributed architecture that allows TVDGraphDB to distribute data and processing across multiple nodes, ensuring scalability, fault tolerance, and high availability. [In Progress]

## Usage

Here's a basic example of how to use TVDGraphDB to generate show recommendations:

```python
from tvdgraphdb import TVDGraphDB

# Initialize TVDGraphDB instance
db = TVDGraphDB()

# Get recommendations for a user and a given show
user_id = 123
show_id = 'Friends'
recommendations = db.get_recommendations(user_id, show_id)

print(recommendations)
```

For more examples and usage scenarios, refer to the documentation (Which is planned to be created at some point).

## Contributing
Contributions are welcome! Please read the contributing guidelines for details on how to contribute to this project.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
