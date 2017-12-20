import java.util.HashMap;
import java.util.ArrayList;

class TrieNode{
  private char label;
  private HashMap<Character, TrieNode> children;
  private String word;

  public TrieNode(char c){
    label = c;
    children = new HashMap<Character, TrieNode>();
    word = "";
  }

  public TrieNode(){
    children = new HashMap<Character, TrieNode>();
    word = "";
  }

  public char getLabel(){
    return label;
  }

  public HashMap<Character, TrieNode> getChildren(){
    return children;
  }

  public String getWord(){
    return word;
  }

  public void setWord(String newword){
    this.word = newword;
  }

  public int numChildren(){
    return children.size();
  }

}

class Trie{
  private TrieNode root;

  public Trie(){
    root = new TrieNode();
  }

  public void add(String word){
    TrieNode current = root;
    for(int i = 0; i < word.length(); i++){
      char c = word.charAt(i);
      if(current.getChildren().containsKey(c))
        current = current.getChildren().get(c);
      else {
        TrieNode newnode = new TrieNode(c);
        current.getChildren().put(c, newnode);
        current = newnode;
      }
      if(i == word.length() - 1)
        current.setWord(word);
    }
  }

  public boolean hasWord(String word){
    boolean result = true;
    TrieNode current = root;
    for(int i = 0; i < word.length(); i++){
      char c = word.charAt(i);
      if(!current.getChildren().containsKey(c)){
        result = false;
        break;
      }
    }
    return result;
  }

  public ArrayList<String> startsWith(String word){
    ArrayList<String> result = new ArrayList<String>();
    TrieNode current = root;
    for(int i = 0; i < word.length(); i++){
      char c = word.charAt(i);
      if(!current.getChildren().containsKey(c)){
        return result;
      }
      current = current.getChildren().get(c);
    }
    result = startsWithHelper(current);
    return result;
  }

  public ArrayList<String> startsWithHelper(TrieNode parent){
    ArrayList<String> result = new ArrayList<String>();
    if(parent.numChildren() == 0){
      result.add(parent.getWord());
    } else {
      if(!parent.getWord().equals("")){
        result.add(parent.getWord());
      }
      for(TrieNode child : parent.getChildren().values()) {
        result.addAll(startsWithHelper(child));
      }
    }
    return result;
  }
}
