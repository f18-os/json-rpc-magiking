This directory includes 

* `node.py`: which
  * defines a node class. 
    * contains a name, list of children, and a count that's initially zero
    * implements a `show(graph)` method recursively prints the nodes within graph  
  * An `increment(graph)` method that increments the counts of all nodes within graph. 
* `localDemo.py`: which creates a dag of nodes, which it prints, increments, and prints again.

Your tasks are
* to create 
  * a jsonrpc server that exports the `increment(graph)` function
  * a client that demonstrates the effect of `increment()` being remotely executed on the graph from localDemo.py.
  * a file named `request.json` containing a the manually genrated contents of jsonrpc request to `increment()`
   equivalent to the one produced by your client.   You should use nc to confirm that it's correct.

# My Solution
My soultion for the graph encoding was to send a list of all the node
objects and their values, and a dictionary of the graph represented by
the noeds and their children. To uniquely identfy all of the nodes, I
used the `id()` function. That way, when sending the graph to the rpc
server, the nodes would be uniquely identifiable, and the structure of
the graph would be accurate. To rebuild the graph on the other end,
the `decodeGraph()` function uses the nodes from the list of nodes to
build the graph. Each 'node' on the graph, is just an id e.g:
    ```
    {1: children[{2: children[...]}, ...]}
    ```
The decode method takes the id of '1' from the structure and finds the
coresponing node information from the list of nodes by id and grabs
that info to build a node object:
e.g
    ```
    id: 1
    List of nodes:
    {1: 
        {name: root,
         val: 0,
        }
    }
    ```
