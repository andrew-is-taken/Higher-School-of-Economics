#include "isogram.hpp"
#include <set>
#include <locale>
//#include <iostream>

// Для фукнций std::isalpha и std::toupper используйте эту локаль
std::locale locale{""};

auto is_isogram(std::string const& word) -> bool {
    // Функция is_isogram получает на вход строку word
    // Возвращает true, если строка является изограммой,
    // и false, если не явялется
    std::string newWord;
    std::set<char>detectedLetters;
    char letter;
    for(int i=0; i<word.length(); i++){
        if(std::isalpha(word[i])){
            letter= tolower(word[i]);
            if(detectedLetters.contains(letter)){
                return false;
            }else{
                detectedLetters.insert(letter);
            }
        }
        //std::cout<<std::string(1, word[i])<< std::endl;
    }
    return true;
}