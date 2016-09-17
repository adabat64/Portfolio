using System;


namespace ConsoleTestEF.Sqlite
{
    public class Program
    {
        public static void Main()
        {
            using (var db = new SQLite.BloggingContext())
            {
                bool menu = true;

                while (menu == true)
                {
                    Console.WriteLine(@"
This console application saves different blogs and posts in a database.
Main Menu:  
Press 1 to view the Blog Database
Press 2 to add a new Blog
Press 3 to write a new Blog Post
Press Q to quit");
                    string choice = Console.ReadLine();


                    if (choice == "1")
                    {
                        Console.WriteLine("All blogs in database:");
                        Console.WriteLine("Blog ID\t\tBlog Name\tBlog URL");

                        foreach (var blog in db.Blogs)
                        {
                            Console.WriteLine("{0,-8}\t{1,-8}\t{2,-8}", blog.BlogID, blog.Name, blog.Url);
                        }
                    menu = true;
                    }
                    else if(choice == "2")
                    {
                        Console.WriteLine("Enter the new Blog's name: ");
                        string blog_name = Console.ReadLine();
                        Console.WriteLine("Enter the new blog's URL: ");
                        string blog_url = Console.ReadLine();
                        db.Blogs.Add(new SQLite.Blog { Name = $"{blog_name}", Url = $"{blog_url}" });

                        var count = db.SaveChanges();
                        Console.WriteLine("{0} records saved to database: ", count);
                        
                        menu = true;
                    }
                    /*else if(choice == "3")
                    {
                        Console.WriteLine("Enter the Blog ID you want to post to: ");
                        int blog_id = Console.Read();
                        Console.WriteLine("Enter the Post title: ");
                        string post_name = Console.ReadLine();
                        Console.WriteLine("Add the Post content: ");
                        string post_content = Console.ReadLine();
                        db.Posts.Add(new SQLite.Post { BlogID = blog_id, Title = "post_name", Content = "post_content" });
                        
                        var count = db.SaveChanges();
                        Console.WriteLine("{0} records saved to database: ", count);
                    }*/

                    else{
                        menu = false;
                    }

                }

            }
        }
    }
}