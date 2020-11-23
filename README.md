# Tree Generator

This script generates a binary tree given preorder, inorder or postorder lists as inputs. It prints the tree out properly.

## How to use

### 1. Select the type of tree 

You can generate a tree given preorder and inorder as inputs or postorder and inorder as inputs

### 2. Specify the inputs

Enter the inputs, with each entry seperated by a blank space. For example

```python

Input Inorder Sequence: I A D J N H B E K O F L G C M
Input Preorder Sequence: H N A I J D O B K E C L F G M
```

The tree would be generated if the inputs specified are of the same length, and are valid to generate a tree.

For example, the above inputs would yield the following tree

```txt

     H___
    /    \
  __N  __O___
 /    /      \
 A_   B_    _C
/  \    \  /  \
I  J    K  L  M
  /    /  / \
  D    E  F G
```

### Acknowledgements

The algorithms were extracted from the following source. This program is just a compilation of the following with a menu.

Node generation from given inorder and postorder lists:
<https://www.techiedelight.com/construct-binary-tree-from-inorder-postorder-traversals/>

Node generation from given inorder and ppreorder lists:
<https://www.techiedelight.com/construct-binary-tree-from-inorder-preorder-traversal/>

Tree printer:
<https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python>