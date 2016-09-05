using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FileCheckApp
{
    class FileCheck
    {
        public string src = @"C:\Users\Owner\Desktop\Source\";
        // string file = System.IO.Path.Combine(src, filename);

        public void processDirectory()
        {
            string[] fileEntries = Directory.GetFiles(src);
            foreach (string filename in fileEntries)
                ProcessFile(filename);
        }
        public void ProcessFile(string filename)
        {
            Console.WriteLine(filename);
            DateTime lastModified = System.IO.File.GetLastWriteTime(filename);
            //Console.WriteLine(lastModified);
            DateTime check = DateTime.Now.AddHours(-24);
           // Console.WriteLine(check);
            string temp = filename.Remove(0, 30);
            Console.WriteLine(temp);
            string dest = "C:\\Users\\Owner\\Desktop\\Dest\\" + temp;
            //Console.WriteLine(dest);


            if (lastModified >= check) {
                Console.WriteLine(lastModified - check);
                File.Move(filename,dest);
            }
        }
    }
        class Program
        {
            static void Main(string[] args)
            {
                FileCheck fc = new FileCheck();
                fc.processDirectory();


            }
        }
    }
