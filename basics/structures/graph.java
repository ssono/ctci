import java.util.HashMap;

class Vertex{
  private String name;
  private int data;
  private HashMap<String, Integer> edges;

  public Vertex(String name){
    name = name;
    data = 0;
    edges = new HashMap<String, Integer>();
  }

  public String getName(){
    return name;
  }

  public int getData(){
    return data;
  }

  public HashMap<String, Integer> getEdges(){
    return edges;
  }

  public void setName(String newname){
    this.name = newname;
  }

  public void setData(int newdata){
    this.data = newdata;
  }

  public void addEdge(String connecting, int weight){
    edges.put(connecting, weight);
  }

  public int getWeight(String connected){
    if(edges.containsKey(connected)){
      return edges.get(connected);
    }
    return 0;
  }

}

class Graph{
  private HashMap<String, Vertex> vertices;
  private int size;

  public Graph(){
    vertices = new HashMap<String, Vertex>();
    size = 0;
  }

  public void addVertex(String name){
    Vertex newvertex = new Vertex(name);
    vertices.put(name, newvertex);
    size++;
  }

  public Vertex getVertex(String name){
    if(vertices.containsKey(name)){
      return vertices.get(name);
    }
    return null;
  }

  public void addEdge(String name1, String name2){
    if(vertices.containsKey(name1) && vertices.containsKey(name2)){
      Vertex v1 = vertices.get(name1);
      Vertex v2 = vertices.get(name2);
      v1.addEdge(v2.getName(), 0);
      v2.addEdge(v1.getName(), 0);
    }
  }

  public void addEdge(String name1, String name2, int weight){
    if(vertices.containsKey(name1) && vertices.containsKey(name2)){
      Vertex v1 = vertices.get(name1);
      Vertex v2 = vertices.get(name2);
      v1.addEdge(v2.getName(), weight);
      v2.addEdge(v1.getName(), weight);
    }
  }
}
