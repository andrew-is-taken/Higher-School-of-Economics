# BST iterator

Написать iterator для дерева. Порядок обхода должен быть инфиксный: сначала левое поддерево, потом сама вершина, потом правое поддерево. В случае дерева поиска это будут элементы в порядке возрастания. Алгоритм должен использовать O(log N) времени и O(1) памяти.

Для примера такого обход смотрите (https://visualgo.net/ru/bst), алгоритмы Предшественник/преемник и Tree traversal в режиме inorder.

Я реализовал много мелких методов в `tree.hpp`, их можно не менять. Но обратите внимание на комментарий на строке 42: вам потребуется добавить ещё одно поле в `tree::iterator`.
