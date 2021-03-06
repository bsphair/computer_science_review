# Linked Lists

Operation | Worst Case
------|--------------
space    | O(n)
prepend  | O(1)
append   | O(1)
lookup   | O(n)
insert   | O(n)
delete   | O(n)


## Structure
* An item is called a <b>node</b>
* <b>head</b> is the first node
* <b>tail</b> is the last node

<img width="386" alt="Screen Shot 2021-01-03 at 11 49 27 PM" src="https://user-images.githubusercontent.com/15611930/103502205-7ee73880-4e1e-11eb-8614-dab68871b020.png">

## Arrays vs Linked Lists
<table>
  <tr>
    <th>Array</th>
    <th>Linked List</th>
  </tr>
  
  <tr>
    <th>
      Insertions/Deletions are inefficient as elements are usually shifted
    </th>
    <th>
      Intertions/Deletions are efficient as no shifting is required
    </th>
  </tr>
  
  <tr>
    <th>
      Random access
    </th>
    <th>
      No random access
    </th>
  </tr>
</table>

## Advantages Over Arrays

* Dynamic size
* Ease of insertion/deletion
* Adding elements to either end is O(1)

## Disadvantages 

* No random access
* Costly lookups
  * Must travel from head to tail searching taking O(i) time
* Not cache-friendly
  * Computers may have caching systems that make reading from sequential addresses in memory fast than scattered addresses
  * Since arrays are sequential, they could be faster
  * Both are theoretically O(n) time
 
## Uses
* Stacks and queues



## References

[Interview Cake's Linked List](https://www.interviewcake.com/concept/java/linked-list)
