// #pragma once - Prevents header files from being included more than once but not for all compilers.
#ifndef BOOK_H 
#define BOOK_H
#include <string>

class Book{
    protected:
        std::string title;
        std::string author;
        int pages;

    public:
        Book();
        Book(std::string t, std::string a, int p);
        std::string getTitle() const;
        std::string getAuthor() const;
        int getPages() const;
        void getBook() const;
};
#endif 