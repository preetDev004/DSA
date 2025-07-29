#include <iostream>
#include "book.h"

Book::Book()
{
    title.assign("");
    author.assign("");
    pages = 0;
}

Book::Book(std::string t, std::string a, int p)
{
    title.assign(t);
    author.assign(a);
    pages = p;
}

std::string Book::getAuthor() const
{
    return this->author;
}

std::string Book::getTitle() const
{
    return this->title;
}

int Book::getPages() const
{
    return this->pages;
}

void Book::getBook() const
{
    std::cout << "Title: " << this->title << std::endl;
    std::cout << "Author: " << this->author << std::endl;
    std::cout << "Pages: " << this->pages << std::endl;
}