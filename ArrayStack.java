/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package dsa;

/**
 *
 * @author K Chamudi
 */
public class ArrayStack {

    private int[] stack;
    private int top;
    private static final int CAPACITY = 10;

    public ArrayStack () {
        stack = new int[CAPACITY];
        top = -1;
    }

    public void push(int item) {
        if (top == stack.length - 1) {
            resize(2 * stack.length);
        }
        stack[++top] = item;
    }

    public int pop() {
        if (isEmpty()) {
            throw new IllegalStateException("Stack underflow");
        }
        int item = stack[top];
        stack[top--] = 0; // Optional: Clear value
        return item;
    }

    public int peek() {
        if (isEmpty()) {
            throw new IllegalStateException("Stack is empty");
        }
        return stack[top];
    }

    public boolean isEmpty() {
        return top == -1;
    }

    public boolean isFull() {
        return top == CAPACITY - 1;
    }

    public int size() {
        return top + 1;
    }

    private void resize(int newCapacity) {
        int[] newStack = new int[newCapacity];
        System.arraycopy(stack, 0, newStack, 0, size());
        stack = newStack;
    }

    public void printStack() {
        System.out.print("Stack (top to bottom): ");
        for (int i = top; i >= 0; i--) {
            System.out.print(stack[i] + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        ArrayStack  myStack = new ArrayStack ();

        myStack.push(10);
        myStack.push(20);
        myStack.push(30);
        System.out.println("Is Full? " + myStack.isFull());
        myStack.printStack();

        System.out.println("Top: " + myStack.peek());
        System.out.println("Popped: " + myStack.pop());
        myStack.printStack();

        System.out.println("Size: " + myStack.size());
        System.out.println("Is Empty? " + myStack.isEmpty());
    }
}

