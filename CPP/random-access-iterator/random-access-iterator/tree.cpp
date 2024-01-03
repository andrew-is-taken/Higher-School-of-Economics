#include "tree.hpp"

void pos(tree_node *node, int &i){
    while (node->up) {
        if (node->up->value < node->value) {
            node = node->up;
            if(node->left != nullptr){
                i += node->left->subtree_size + 1;
            }else{
                i += 1;
            }
        } else {
            node = node->up;
        }
    }
}

auto findLeft(tree_node *node){
    while(node->left != nullptr){
        node=node->left.get();
    }
    return node;
}

auto findRight(tree_node *node){
    while(node->right != nullptr){
        node=node->right.get();
    }
    return node;
}

tree::iterator operator+(tree::iterator const &self, ptrdiff_t diff) {
    auto *p = self.p;
    if (p == nullptr){
        return tree::iterator(self.lastElem);
    }
    if (diff == 0){
        return tree::iterator(p);
    }

    int a = 0;
    if (diff < 0) {
        auto inDiff = -diff;
        if (p->left != nullptr && p->left->subtree_size >= inDiff) {
            inDiff--;
            p = p->left.get();
            if(p->right != nullptr){
                a = p->right->subtree_size;
            }
            while (a != inDiff) {
                if (a < inDiff) {
                    if(p->left->right != nullptr){
                        a += p->left->right->subtree_size + 1;
                    }else{
                        a += 1;
                    }
                    p = p->left.get();
                } else {
                    if(p->right->left != nullptr){
                        a -= p->right->left->subtree_size + 1;
                    }else{
                        a -= 1;
                    }
                    p = p->right.get();
                }
            }
            return tree::iterator(p);
        } else {
            if (p->up == nullptr) {
                return tree::iterator(nullptr);
            }
            if (p->up->value >= p->value) {
                if(p->right != nullptr){
                    inDiff += p->right->subtree_size + 1;
                }else{
                    inDiff += 1;
                }
            } else {
                if(p->left != nullptr){
                    inDiff -= p->left->subtree_size + 1;
                }else{
                    inDiff -= 1;
                }
            }

            return tree::iterator(p->up) - inDiff;
        }
    } else {
        if (p->right != nullptr && p->right->subtree_size >= diff) {
            diff--;
            p = p->right.get();
            if(p->left != nullptr){
                a = p->left->subtree_size;
            }
            while (a != diff) {
                if (a < diff) {
                    if(p->right->left != nullptr){
                        a += p->right->left->subtree_size + 1;
                    }else{
                        a += 1;
                    }
                    p = p->right.get();
                } else {
                    if(p->left->right != nullptr){
                        a -= p->left->right->subtree_size + 1;
                    }else{
                        a -= 1;
                    }
                    p = p->left.get();
                }
            }
            return tree::iterator(p);
        } else {
            if (p->up == nullptr) {
                return tree::iterator(nullptr, findRight(p));
            }
            if (p->up->value <= p->value) {
                if(p->left != nullptr){
                    diff += p->left->subtree_size + 1;
                }else{
                    diff += 1;
                }
            } else {
                if(p->right != nullptr){
                    diff -= p->right->subtree_size + 1;
                }else{
                    diff -= 1;
                }
            }
            return tree::iterator(p->up) + diff;
        }
    }
}

ptrdiff_t operator-(tree::iterator const &self, tree::iterator other) {
    int first = 0;
    auto *p = self.p;
    if (p == nullptr) {
        p = self.lastElem;
        first++;
    }
    if(p->left != nullptr){
        first += p->left->subtree_size;
    }
    pos(p, first);

    int second = 0;
    p = other.p;
    if (p == nullptr) {
        p = self.lastElem;
        second++;
    }
    if(p->left != nullptr){
        second += p->left->subtree_size;
    }
    pos(p, second);
    return first - second;
}

auto tree::begin() const -> iterator {
    return tree::iterator(findLeft(root.get()));
}

auto tree::end() const -> iterator {
    return tree::iterator(nullptr, findRight(root.get()));
}