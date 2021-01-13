# Queues

<table>
  <tr>
    <th>Operation</th>
    <th>Worst Case</th>
  </tr>
  <tr>
    <td>Add</td>
    <td>O(1)</td>
  </tr>
  <tr>
    <td>Deletion</td>
    <td>O(1)</td>
  </tr>
  <tr>
    <td>Search</td>
    <td>O(n)</td>
  </tr>
  <tr>
    <td>Access</td>
    <td>O(n)</td>
  </tr>
</table>

## Implementation 

```python
class Queue:
    def __init__(self):
        self.data = []
    
    def getData(self):
        print(self.data)
        
    def enqueue(self, item):
        self.data.insert(0, item)
        
    def dequeue(self):
        return self.data.pop()
        
        
def main():
    q = Queue()
```
