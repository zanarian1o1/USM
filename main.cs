using System;
using System.IO;
using System.Linq;

namespace UnturnedServerManager
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Welcome to the Unturned Server Manager!");

            // Select the server folder
            Console.Write("Enter the path to the server folder: ");
            string serverFolderPath = Console.ReadLine();

            if (!Directory.Exists(serverFolderPath))
            {
                Console.WriteLine("The specified folder does not exist.");
                return;
            }

            // Search for specific files
            string[] targetFiles = { "config.json", "server.cfg", "settings.txt" };
            var foundFiles = targetFiles
                .Select(file => Path.Combine(serverFolderPath, file))
                .Where(File.Exists)
                .ToList();

            if (foundFiles.Count == 0)
            {
                Console.WriteLine("No target files found in the specified folder.");
                return;
            }

            Console.WriteLine("Found the following files:");
            for (int i = 0; i < foundFiles.Count; i++)
            {
                Console.WriteLine($"{i + 1}: {foundFiles[i]}");
            }

            // Select a file to edit
            Console.Write("Enter the number of the file you want to edit: ");
            if (int.TryParse(Console.ReadLine(), out int fileIndex) && fileIndex > 0 && fileIndex <= foundFiles.Count)
            {
                string selectedFilePath = foundFiles[fileIndex - 1];
                string fileContent = File.ReadAllText(selectedFilePath);
                Console.WriteLine("Current file content:");
                Console.WriteLine(fileContent);

                // Edit the file content
                Console.WriteLine("Enter new content for the file (or press Enter to keep current content):");
                string newContent = Console.ReadLine();

                if (!string.IsNullOrEmpty(newContent))
                {
                    File.WriteAllText(selectedFilePath, newContent);
                    Console.WriteLine("File saved successfully.");
                }
                else
                {
                    Console.WriteLine("No changes made to the file.");
                }
            }
            else
            {
                Console.WriteLine("Invalid selection.");
            }
        }
    }
}
