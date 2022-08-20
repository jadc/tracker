# Tracker
Repository of information regarding unreleased music files.

Visit [the website](http://leak.info.gf/) to view the contents.

## Contribution Guidelines
### What to contribute
This tracker is for CD-quality leaks only. The following are outside the scope of this tracker and will be rejected.
* Snippets (low or high quality)
* Released songs (e.g. in higher bitrate, OG file)
    * If an unreleased song on the tracker gets released, then it may remain on the tracker (just tag it with "Former")
    * Do not add songs to the tracker that were never leaked at any point

### Creating a song page
To create a new page for a song, copy and paste the template from [here](archetypes/default.md).

**Everything should be written in lower-case**. An exception to this being when specific capitalization is needed. (e.g. "DY krazy" or "capo DTE")

**Use double-quotes when necessary, not single-quotes**.

> I suggest viewing existing songs to get an idea of the format. Visit the [content folder](content/), click any `.md` file, then press the "Raw" button. This is the template that these files must be in.

#### Fields
Any of the following options may be omitted if they are not publicly known.

1. `title`: The song's name. All characters are allowed.
2. `aka`: List of common alternative names for the song
3. `artists`: List of artists featured in the song
4. `producers`: List of producers who produced the beat
5. `tags`: Any additional info about the song that isn't unique to it. Some examples include:
    * "2018" if the song was recorded in 2018
    * "OG file" if the file related options are describing an OG file
    * "open" if the song contains an open verse
6. `file_name`: The exact file name and extension of the song (ideally the OG file, but not necessary)
7. `file_title`: The title in the metadata of the file, if it has one
8. `file_comment`: The comment in the metadata of the file, if it has one
9. `recorded`: If known, the date the song was recorded. (YYYY-MM-DD)
10. `leaked`: If known, the date the song was leaked. (YYYY-MM-DD)
11. `length`: The duration of the song. (mm:ss)
12. `md5`: The MD5 checksum of the file
13. `mirrors`: List of **Base64 encoded** URLs to download the file. Avoid uploading files to websites that frequently get taken down. Avoid uploading files to websites that re-encode the files.

#### Page's file name
The name of the file you submit should be the song's name, replacing any spaces with hyphens, URL safe characters (no ', &, or brackets), and ending in `.md`

### Submitting a song
If you are familiar with GitHub, feel free to fork this repository and create a pull request with any changes/additions you wish to make. 
* Please keep your changes within the [content folder](content/) unless you are familiar with [Hugo](https://gohugo.io/).

If you have no idea what that meant, you can also join the [Leak Preservationists Discord server](https://discord.com/invite/wx2hj6hbUT) and submit your Markdown (.md) files in `#submissions`. This will take significantly longer, however, so I suggest learning how to create pull requests on GitHub.
