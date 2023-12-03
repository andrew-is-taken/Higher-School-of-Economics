#include "tree.hpp"

auto findSmallest(tree_node *node){
    while(node->left.get() != nullptr){
        node=node->left.get();
    }
    return node;
}

auto findBiggest(tree_node *node){
    while(node->right.get() != nullptr){
        node=node->right.get();
    }
    return node;
}

auto tree::iterator::operator++() -> iterator & {
    if(p->right.get() != nullptr){
        p = findSmallest(p->right.get());
    }else{
        while (p != p->up->left.get()) {
                    p = p->up;
                    if(p->up == nullptr){
                        p = nullptr;
                        return *this;
                    }
                }
                p = p->up;
    }
    return *this;
}

auto tree::iterator::operator--() -> iterator & {
    if(p == nullptr){
        p = findBiggest(root);
        return *this;
    }
    if(p->left.get() != nullptr){
        p = findBiggest(p->left.get());
    }else{
        while (p != p->up->right.get()) {
            p = p->up;
            if(p->up == nullptr){
                p = nullptr;
                return *this;
            }
        }
        p = p->up;
    }
    return *this;
}

auto tree::begin() const -> iterator {
    return {findSmallest(root.get()), root.get() };
}

auto tree::end() const -> iterator {
    return {nullptr, root.get() };
}

// Можно не менять
auto tree::iterator::operator++(int) -> iterator {
    auto it = *this;
    ++*this;
    return it;
}

auto tree::iterator::operator--(int) -> iterator {
    auto it = *this;
    --*this;
    return it;
}
