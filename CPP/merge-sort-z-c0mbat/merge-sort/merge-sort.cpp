#include "merge-sort.hpp"
#include <memory>
#include <iostream>

List::List(std::initializer_list<int> list) {
    // Задание №1: сделать список из list
    ListElement * tail = nullptr;
    if(list.begin()){
        for (auto number : list) {
            // TODO: Добавить в создаваемый односвязный список
            if (tail == nullptr) {
                // TODO: Создать первый элемент списка в head
                head = std::make_unique<ListElement>(number);
                tail=head.get();
            } else {
                // TODO: Создать элемент списка в tail->next
                tail->next = std::make_unique<ListElement>(number);
                tail=tail->next.get();
            }
        }
    }
}

auto listMiddle(ListElement *list) -> ListElement * {
    auto *ptr = list->next.get();
    if (ptr != nullptr)
        ptr = ptr->next.get();
    while (ptr != nullptr) {
        list = list->next.get();
        ptr = ptr->next.get();
        if (ptr != nullptr)
            ptr = ptr->next.get();
    }
    return list;
}

auto merge(List a, List b) noexcept -> List {
    // Слияние двух упорядоченных списков
    List result;
    ListElement *tail = result.head.get();
    while (a.head && b.head) {
        // Выбираем меньший из a.head.value и b.head.value
        // и переносим a.head или b.head в конец result,
        // после чего переносим tail->next обратно
        // в a.head или b.head
        if(a.head->value<b.head->value){
            if(result.head){
                tail->next = std::make_unique<ListElement>(a.head->value);
                a.head=std::move(a.head->next);
                tail=tail->next.get();
            }else{
                result.head = std::make_unique<ListElement>(a.head->value);
                a.head = std::move(a.head->next);
                tail = result.head.get();
            };
        }else{
            if(result.head){
                tail->next = std::make_unique<ListElement>(b.head->value);
                b.head=std::move(b.head->next);
                tail=tail->next.get();
            }else{
                result.head = std::make_unique<ListElement>(b.head->value);
                b.head = std::move(b.head->next);
                tail = result.head.get();
            }
        }
    }
    // переносим оставшийся список в конец result
    while (a.head) {
        if(result.head){
            tail->next = std::make_unique<ListElement>(a.head->value);
            a.head=std::move(a.head->next);
            tail=tail->next.get();
        }else{
            result.head = std::make_unique<ListElement>(a.head->value);
            a.head = std::move(a.head->next);
            tail = result.head.get();
        };
    }
    while (b.head) {
        if(result.head){
            tail->next = std::make_unique<ListElement>(b.head->value);
            b.head=std::move(b.head->next);
            tail=tail->next.get();
        }else{
            result.head = std::make_unique<ListElement>(b.head->value);
            b.head = std::move(b.head->next);
            tail = result.head.get();
        }
    }
    return result;
}

auto mergesort(List &list) noexcept -> void {
    // Сортировка слиянием
    // 1. Определяем середину списка (см. ветку list-algo семинаров)
    List second;
    if(list.head) {
        if (list.head->next != nullptr) {
            ListElement *middle = listMiddle(list.head.get());
            //  2. Переносим вторую половину в новый список
            second.head = std::move(middle->next);
            // 3. Для каждой половины запускаем mergesort
            mergesort(list);
            mergesort(second);
        } else {
            return;
        }
        // 4. Делаем merge от результатов,
        // не забыв std::move в аргументах,
        // присваивая результат в list
        list = merge(std::move(list), std::move(second));
    }
}
