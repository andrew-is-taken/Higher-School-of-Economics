#include "tree.hpp"

auto tree::insert(int val) -> tree_node * {
    // Код для добавления элемента в дерево
    std::unique_ptr<tree_node> node(new tree_node(val));
    if (root == nullptr) { //если корень дерева пустой
        root = std::move(node);
        return root.get();
    }
    tree_node *temp = root.get();
    tree_node *prev = root.get();
    while (temp != nullptr) { //ищем, куда вставить новую ноду
        if (temp->value == val) { //если уже нашлось такое значение
            return temp;
        }
        prev = temp;
        if (temp->value < val) //перемещаемся направо или налево по дереву
            temp = temp->right.get();
        else
            temp = temp->left.get();
    }
    auto &ref = prev->value < val ? prev->right : prev->left; //выбираем и возвращаем место, куда ставить новую ноду
    ref = std::move(node);
    ref->up = prev;
    return ref.get();
}

auto tree::remove(int val) -> bool {
    // Код для удаления элемента из дерева
    tree_node* temp = root.get();
    tree_node* prev = root.get();
    bool findingOnRight;
    if(root == nullptr) //если дерево пустое
        return false;
    if (root->right == nullptr && root->left == nullptr) { //если один элемент в дереве
        if(root->value != val)
            return false;
        root = nullptr;
        return true;
    }
    while (temp != nullptr) { //перебираем элементы дерева
        if(temp->value==val){ //если нашелся нужный
            if(temp->right.get() != nullptr) findingOnRight = true; //ищем справа от нашего элемента
            else if(temp->left.get() != nullptr) findingOnRight = false; //ищем слева от нашего элемента
            else{
                if(temp->up->right.get() == temp){
                    temp = temp->up;
                    temp->right = nullptr;
                }else{
                    temp = temp->up;
                    temp->left = nullptr;
                }
                return true;
            }
            //заменяем удаленный элемент на подходящий и перестраиваем дерево
            tree_node* smallest;
            tree_node* preSmallest = temp;
            if(findingOnRight){ //если ищем справа
                smallest = temp->right.get();
                //smallest->up = temp;
                while (smallest != nullptr){
                    smallest->up = preSmallest;
                    preSmallest = smallest;
                    smallest = smallest->left.get();
                }
                tree_node* old = preSmallest->up;
                temp->value = preSmallest->value;
                old->right = std::move(preSmallest->right);
            }else{ //если ищем слева
                smallest = temp->left.get();
                //smallest->up = temp;
                while (smallest != nullptr){
                    smallest->up = preSmallest;
                    preSmallest = smallest;
                    smallest = smallest->right.get();
                }
                tree_node* old = preSmallest->up;
                temp->value = preSmallest->value;
                old->right = std::move(preSmallest->left);
            }
            return true;
        }
        if (temp->value < val){
            temp = temp->right.get();
        }
        else{
            temp = temp->left.get();
        }
        temp->up = prev;
        prev = temp;
    }
    return false;
}