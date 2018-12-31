import media
import fresh_tomatoes

zootopia = media.Movie("Zootopia",
            "The first rabbit cop sets out to prove herself to the world",
            "https://m.media-amazon.com/images/M/MV5BOTMyMjEyNzIzMV5BMl5BanBnXkFtZTgwNzIyNjU0NzE@._V1_SY1000_SX675_AL_.jpg",
            "https://www.youtube.com/watch?v=jWM0ct-OLsM",
            "Byron Howard, Rich Moore")

frozen = media.Movie("Frozen",
            "A princess sets out to save her kindom from perpetual winter",
            "https://m.media-amazon.com/images/M/MV5BMTQ1MjQwMTE5OF5BMl5BanBnXkFtZTgwNjk3MTcyMDE@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
            "https://www.youtube.com/watch?v=TbQm5doF_Uc",
            "Jennifer Lee, Chris Buck")

rise_of_the_guardians = media.Movie("Rise of the Guardians",
            "The guardians must protect the world's children from darkness and disbelief",
            "https://m.media-amazon.com/images/M/MV5BMTkzMjgwMDg1M15BMl5BanBnXkFtZTcwMTgzNTI1OA@@._V1_SY1000_CR0,0,643,1000_AL_.jpg",
            "https://www.youtube.com/watch?v=yd71LWhCO4s",
            "Peter Ramsey")

twelve_angry_men = media.Movie("Twelve Angry Men",
            "12 jurors debate to reach a conclusion of a murder trial",
            "https://m.media-amazon.com/images/M/MV5BMWU4N2FjNzYtNTVkNC00NzQ0LTg0MjAtYTJlMjFhNGUxZDFmXkEyXkFqcGdeQXVyNjc1NTYyMjg@._V1_SY1000_CR0,0,649,1000_AL_.jpg",
            "https://www.youtube.com/watch?v=A7CBKT0PWFA",
            "Sidney Lumet")

make_happy = media.Movie("Make Happy",
            "Bo Burnham's newest stand-up comedy special",
            "https://m.media-amazon.com/images/M/MV5BZjg0YmNiZTAtZDI2Yi00MTVhLTk3ZTctM2JiNjQwY2ZhMzg4XkEyXkFqcGdeQXVyMzE1NjI3MjI@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
            "https://www.youtube.com/watch?v=TXBbLRRGxMc",
            "Bo Burnham, Christopher Storer")

the_imitation_game = media.Movie("The Imitation Game",
            "Alan Turing creates the world's first computer to crack Nazi codes",
            "https://m.media-amazon.com/images/M/MV5BOTgwMzFiMWYtZDhlNS00ODNkLWJiODAtZDVhNzgyNzJhYjQ4L2ltYWdlXkEyXkFqcGdeQXVyNzEzOTYxNTQ@._V1_SY999_CR0,0,670,999_AL_.jpg",
            "https://www.youtube.com/watch?v=S5CjKEFb-sM",
            "Morten Tyldum")

movies = [zootopia, frozen, rise_of_the_guardians, twelve_angry_men, make_happy, the_imitation_game]

fresh_tomatoes.open_movies_page(movies)
