import java.util.*;

public class OccurrenceSet<T> implements Set<T>{
    private HashMap<T, Integer> map;
    
    
    public OccurrenceSet(){
        map = new HashMap<T, Integer>();
    }
    
    
    @Override
    public boolean add(T t){
        if(map.containsKey(t)){
            int count = map.get(t);
            count++;
            map.put(t, count);
            return false;
        }
        else{
            map.put(t, 1);
            return true;
        }
    }
    
    
    @Override
    public boolean addAll(Collection<? extends T> c){
        boolean changed = false;

        for(T t: c){
            if(map.containsKey(t)){
                int count = map.get(t);
                count++;
                map.put(t, count);
            }
            else{
                map.put(t, 1);
                changed = true;
            }
        }
        
        return changed;
    }
    
    
    @Override
    public boolean remove(Object o){
        if(map.containsKey(o)){
            map.remove(o);
            return true;
        }
        else{
            return false;
        }
    }
    
    
    @Override
    public boolean removeAll(Collection<?> c){
        boolean changed = false;
        
        for(Object o: c){
            if(map.containsKey(o)){
                map.remove(o);
                changed = true;
            }
        }
        
        return changed;
    }
    
    @SuppressWarnings("unchecked")
    @Override
    public boolean retainAll(Collection<?> c){
        boolean changed = false;
        
        HashMap<T, Integer> newMap = new HashMap<T, Integer>();
        
        for(Object o: c){
            if(map.keySet().contains(o)){
                newMap.put((T) o, map.get(o));
            }
        }
        
        if(map.size() != newMap.size()){
            changed = true;
        }
        
        map = newMap;
        
        return changed;
    }
    
    
    @Override
    public boolean contains(Object o){
        if(map.containsKey(o)){
            return true;
        }
        else{
            return false;
        }
    }
    
    
    @Override
    public boolean containsAll(Collection<?> c){
        for(Object o: c){
            if(!map.containsKey(o)){
                return false;
            }
        }
        return true;
    }
    
    
    @Override
    public int size(){
        return map.size();
    }
    
    
    @Override
    public void clear(){
        map.clear();
    }
    
    
    @Override
    public boolean isEmpty(){
        if(map.size() == 0){
            return true;
        }
        else{
            return false;
        }
    }
    
    
    //Create an ordered ArrayList for use in other methods
    public ArrayList<T> order(){
        ArrayList<T> list = new ArrayList<T>(map.keySet());
        Collections.sort(list, new Comparator<T>(){
            public int compare(T first, T second){
                return (map.get(first)) - (map.get(second));
            }
        });
        return list;
    }
    
    
    @Override
    public Object[] toArray(){
        return order().toArray();
    }
    
    
    @SuppressWarnings("unchecked")
    @Override
    public <T> T[] toArray(T[] a){
        if(a.length < map.size()){
            a = Arrays.copyOf(a, map.size());
        }
        
        ArrayList<T> list = (ArrayList<T>) order();
        list.toArray(a);
        
        return a;
    }
    
    
    @Override
    public Iterator<T> iterator(){
        return order().iterator();
    }
    
    
    public String toString(){
        return order().toString();
    }
    
    
}