#include <iostream>
#include "book.cpp"

int main()
{
    Book marvel("Avengers", "Joss Whedon", 500), disney("Finding Nemo", "Davies", 400);

    std::string author = marvel.getAuthor();
    int pages=  marvel.getPages();
    std::string title = marvel.getTitle();
    std::cout<<author<<std::endl;
    std::cout<<pages<<std::endl;
    std::cout<<title<<std::endl;
    marvel.getBook();

    std::cout << std::endl;

    std::string author2 = disney.getAuthor();
    int pages2=  disney.getPages();
    std::string title2 = disney.getTitle();
    std::cout<<author2<<std::endl;
    std::cout<<pages2<<std::endl;
    std::cout<<title2<<std::endl;
    disney.getBook();


    return 0;
}