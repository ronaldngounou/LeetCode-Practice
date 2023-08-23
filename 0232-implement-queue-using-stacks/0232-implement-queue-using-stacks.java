class MyQueue {
    public Stack<Integer> stack1 = new Stack<>();
    public Stack<Integer> stack2 = new Stack<>();
    public MyQueue() {
        
    }
    
    public void push(int x) {
        stack1.push(x);
    }
    
    public int pop() {
        if (empty())
            throw new IllegalStateException();
        if (stack2.empty())
            while (!stack1.empty())
                stack2.push(stack1.pop());
        return stack2.pop();
    }
    
    public int peek() {
        if (empty())
            throw new IllegalStateException();
        if (stack2.empty())
            while(!stack1.empty())
                stack2.push(stack1.pop());
        return stack2.peek();
    }
    
    public boolean empty() {
        return (stack1.empty() && stack2.empty());
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */