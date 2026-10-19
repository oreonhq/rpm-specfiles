%global source0_hash 813f24570ca7590a9ae6e8e9ca4e5bd6c9f09d61fe36ad6feca89b7c2feaae70
%global geany_plug_docdir %{?_pkgdocdir}%{!?_pkgdocdir:%{_docdir}/%{name}-%{version}}
%global req_geany_ver 2.1.0
Name:           geany-plugins
Version:        2.1.0
Release:        1%{?dist}
Summary:        Plugins for Geany
License:        GPL-3.0-or-later
URL:            http://plugins.geany.org/
Source0:        http://plugins.geany.org/geany-plugins/geany-plugins-%{version}.tar.bz2
# oreon:deps
BuildRequires:  cppcheck
BuildRequires:  ctpl-devel
BuildRequires:  enchant2-devel
BuildRequires:  geany-devel
BuildRequires:  geany-libgeany
BuildRequires:  gettext
BuildRequires:  gpgme-devel
BuildRequires:  gtkspell3-devel
BuildRequires:  intltool
BuildRequires:  libgit2-devel
BuildRequires:  libsoup-devel
BuildRequires:  libtool
BuildRequires:  libwnck3-devel
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gconf-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(webkit2gtk-4.1)
BuildRequires:  python3-docutils
BuildRequires:  vala
BuildRequires:  vte291-devel
# /oreon:deps
%description
Plugins for Geany. Plugins included are:
* Addons (Various small Addons)
* Autoclose (intellectually helps you to write code)
* Automark (highlights all words that match current word)
* Code navigation (Navigate through your source code easily)
* Commander (Control Geany using commands from a command panel)
* Debugger (Enables debugging in Geany)
* Defineformat (Write multiline defines with aligned backslash)
* GeanyGDB (Integration with GDB)
* GeanyGenDoc (Automatically generate documentation source code)
* GeanyLaTeX (Improved Support for LaTeX documents)
* GeanyMacro (User defined Macros for Geany)
* GeanyNumberedBookmarks (Provide users with 10 numbered Bookmarks)
* GeanyPG (Encrypt, decrypt and verify signatures with GnuPG)
* GeanyVC (Support for various Version Control Systems)
* Geanyctags (Generate and query ctags files for a Geany project)
* Geanydoc (Call specific documentation from within Geany)
* Geanyextrasel (Additional features for selecting code)
* Geanyinsertnum (Insert huge number ranges with small efforts)
* Geanylua (Support for Scripting with Lua)
* Geanyminiscript (Geany Mini-Script filter plugin)
* Geanyprj (Alternate project management for Geany)
* Geniuspaste (Use nopaste services directly from within Geany)
* Git-changebar (Highlights uncommitted changes, and allows navigation through hunks)
* KeyRecord (record a sequence of keystrokes and to replay it several times)
* Latex (Add LaTeX support to Geany)
* LineOperations (Assortment of simple line functions that can be applied to an open file)
* Lipsum (Generate random Text)
* LSP (Language Server Protocol for Geany)
* Markdown (Real time preview for Markdown documents)
* Overview (Overview over the code in a sidebar)
* PairTagHighlighter (Find and highlight matching opening/closing HTML tags)
* Pairtaghighlighter (Extension of Geany's project management)
* Pohelper (Improves Support for GetText translation files)
* Pretty-Print (XML Pretty Printer)
* ProjectOrganizer (Extension of Geany's Project Management)
* Scope (Graphical GDB front-end)
* SendMail (Sending of documents from within Geany)
* Shiftcolumn (Moving blocks of text horizontally)
* Spellcheck (Spell checking of documents or marked text)
* Tableconvert (Helps on converting a tabulator separated selection into a table)
* Treebrowser (Alternate file browser with tree view of folders)
* Updatechecker (Automatically check for Geany updates)
* Vimode: The plugin you always waited for
* Webhelper (Provides some web development facilities for Geany)
* Workbench (Manage multiple projects in Geany)
* XMLSnippets (Extends XML/HTML tag autocompletion provided by Geany)

%package common
Summary:   Common files used by all geany plugins
Requires:  geany >= %{req_geany_ver} geany-libgeany >= %{req_geany_ver}
Obsoletes: geany-plugins-debugger <= 1.31
Obsoletes: geany-plugins-devhelp <= 2.0
Obsoletes: geany-plugins-geanylua < 1.25
Obsoletes: geany-plugins-geanypy <= 1.31
Obsoletes: geany-plugins-multiterm <= 1.31
Obsoletes: geany-plugins-scope <= 1.31
%description common
This package contains some common files which are used by every Geany plugin,
e.g. language translations.

%package addons
Summary:   Miscellaneous Addons for Geany
Requires:  geany-plugins-common = %{version}-%{release}
%description addons
This plugins consists of various small addons too small to justify their own
plugin, but are useful to have. The following functionality is implemented:
* Document list: This addon places a new item in the toolbar and when clicked
  offers a menu listing all open files plus the 'Close All' and 'Close Other
  Documents' menu items. This can be useful to quickly access open files and
  switch to them.
* Open and Copy URI: Adds 'Open URI' and 'Copy URI' menu items to the editor
  menu when the word under the cursor looks like a URI. 'Open URI' uses the
  browser command configured in Geany to open it.
* Tasks: The tasks plugin goes through a file being edited and picks out
  lines with configurable keywords (e.g. "TODO" or "FIXME") in them. It
  collects the text after those words and puts them in a new "Tasks" tab in
  the message window. Clicking on a task in that tab takes you to the line in
  the file where the task was defined.
* Systray: Adds a status icon to the notification area (systray) and provides
  a simple popup menu with some basic actions. It can also be used to
  quickly show and hide the Geany main window.
* Bookmark list: Add a list of defined bookmarks (line markers) to the sidebar.
  This list contains all bookmarks defined in the current file
  for faster overview and access.
* Mark Word: When double-clicking a word, all occurrences of this word are
  searched and then highlighted (similar to Geany's 'Mark All' Find option).
* Strip trailing blank lines: This addon removes excessive trailing blank
  lines from the document when it is saved. If you have 'Ensure new line at
  file end' option checked in Preferences, one trailing newline will be left.
* XML tagging: XML tagging allows to easy tag a selected text, by checking for a
  selection, offering a little dialog for inserting a tag and
  replacing a selection.

%package autoclose
Summary:   Intellectually helps you to write code
Requires:  geany-plugins-common = %{version}-%{release}
%description autoclose
This plugin enables auto-closing features. Auto-closing works while you typing
and intellectually helps you to write code.

%package automark
Summary:   Highlights all words that match current word
Requires:  geany-plugins-common = %{version}-%{release}
%description automark
This simple plugin highlights all words that match the current word.

%package codenav
Summary:    Navigate through your source code easily
Requires:   geany-plugins-common = %{version}-%{release}
%description codenav
This plugin adds some facilities for navigating in the code.
Actually, it will make it possible to:
- switch between header and implementation
- go to a file by typing its name

%package commander
Summary:    Control Geany using commands from a command panel.
Requires:   geany-plugins-common = %{version}-%{release}
%description commander
Commander is a plugin for Geany that provides a command panel for rapid
access to any action.

%package debugger
Summary:    Enables debugging in Geany
Group:      Development/Tools
Requires:   geany-plugins-common = %{version}-%{release}
Requires:   vte291 >= 0.24
Provides:   geany-plugins-debugger >= 1.36
%description debugger
Plugin enables debugging in Geany. Currently supports GDB only, but was
developed with multiple debuggers support in mind, so the other backends
support is planned as well.

%package defineformat
Summary:    Write multiline defines with aligned backslash
Requires:   geany-plugins-common = %{version}-%{release}
%description defineformat
On-the-fly #define prettyprinter. This plugin will help you to
write multiline defines with aligned backslash. After installed successfully,
load the plugin in Geany's plugin manager. Try it: open C/C++ file and type:

    #define A() do {

%package geanyctags
Summary:    Generate and query ctags files for a Geany project
Requires:   geany-plugins-common = %{version}-%{release}
Requires:   ctags
%description geanyctags
Even though Geany supports symbol definition searching by itself within the
open files (and with a plugin support within the whole project), tag
regeneration can become too slow for really big projects. This is why this
plugin was created. It makes it possible to generate the tag file only once and
just query it when searching for a particular symbol definition/declaration.
This approach is fine for big projects where most of the codebase remains
unchanged and the tag positions remain more or less static.

%package geanydoc
Summary:   Call documentation from within Geany
Requires:  geany-plugins-common = %{version}-%{release}
%description geanydoc
Geanydoc allows you to execute specific commands on the word under the cursor.
This word is passed as an argument to the command. The output of the command
can either be placed into a special buffer called "DOC" or can be used to
execute an external program. Geanydoc is intended to be used for searching
through API documentation.

%package geanyextrasel
Summary:   Additional features for selecting code
Requires:  geany-plugins-common = %{version}-%{release}
%description geanyextrasel
Geanyextrasel provides some special features for selecting code, e.g. from
opening brace to closed brace and so on. This plugin will be very useful for
you if you're a programmer and working with much sourcecodes.

%package geanygendoc
Summary:   Automatically generate documentation source code
Requires:  geany-plugins-common = %{version}-%{release}
Requires:  ctpl-libs >= 0.3
Requires:  /usr/bin/rst2html
%description geanygendoc
GeanyGenDoc is a plugin for Geany that aims to automatically generate
documentation comment basis from the source code.

You may also want to install the following packages which enable
some extra features:
 - Docutils (http://docutils.sourceforge.net/) -- or another implementation of
   rst2html -- is needed to (re)generate the HTML manual.

%package geanyinsertnum
Summary:   Insert huge number ranges with small efforts
Requires:  geany-plugins-common = %{version}-%{release}
%description geanyinsertnum
Geanyinsertnum replaces a (possibly zero-width) rectangular selection with
integer numbers, using start/step/base etc. specified by the user. For
practical reasons, the number of lines is limited to 500000.

%package latex
Summary:   LaTeX support for Geany
Requires:  geany-plugins-common = %{version}-%{release}
Obsoletes: geany-plugins-geanylatex <= 1.32
Provides:  geany-plugins-geanylatex >= 1.33
Recommends: tex(latex)
%description latex
This plugin improves LaTeX support in Geany. It provides several templates for
new documents, help with adding labels and inserting special characters,
and much more.

%package lipsum
Summary:   Lorem Ipsum generator for Inserting Placeholder Text
Requires:  geany-plugins-common = %{version}-%{release}
Obsoletes: geany-plugins-geanylipsum <= 1.28
Provides:  geany-plugins-geanylipsum >= 1.29
%description lipsum
Lipsum is a Lorem Ipsum generator for inserting placeholder text into a
document.

#%package geanylua
#Summary:   Lua Scripting for Geany
#Group:     Development/Tools
#Requires:  geany-plugins-common = %{version}-%{release}
#Requires:  lua < 5.2
#
#%description geanylua
#This plugin provides extensive support for developing in the lua programming
#language.

%package lsp
Summary:   Language Server Protocol for Geany
Group:     Development/Tools
Requires:  geany-plugins-common = %{version}-%{release}
%description lsp
LSP Client is a language server protocol client plugin that allows to run
multiple language servers for various programming languages, making their
functionality accessible to Geany.  

%package geanymacro
Summary:   User defined Macros for Geany
Requires:  geany-plugins-common = %{version}-%{release}
%description geanymacro
GeanyMacro is a plugin to provide user defined macros for Geany. It started
out as part of the ConText feature parity plugin, which was split into
individual plugins to better suit Geany's ethos of being as light as
possible while allowing users to select which features they want to add to
the core editor. The idea was taken from a Text Editor for Windows called
ConText.

This plugin alows you to record and use your own macros. Macros are
sequences of actions that can then be repeated with a single key
combination. So if you had dozens of lines where you wanted to delete the
last 2 characters, you could simple start recording, press End, Backspace,
Backspace, down line and then stop recording. Then simply trigger the macro
and it would automaticaly edit the line and move to the next. You could then
just repeatedly trigger the macro to do as many lines as you want.

%package geanyminiscript
Summary:   Geany Mini-Script filter plugin
Requires:  geany-plugins-common = %{version}-%{release}
%description geanyminiscript
The GeanyMiniScript plugin is a tool to apply a script filter on:

* the text selection
* the current document
* all documents of the current session.

The filter type can be:

* Unix shell script
* perl script
* python script
* sed commands
* awk script

The output can be:

* the selection of the current document
* all the current document
* or a new document

%package geanynumberedbookmarks
Summary:   Provide users 10 numbered Bookmarks
Requires:  geany-plugins-common = %{version}-%{release}
%description geanynumberedbookmarks
GeanyNumberedBookmarks is a plugin to provide users with 10 numbered
bookmarks (in addition to the usual bookmarks). It started out as part of
the ConText feature parity plugin, which was split into individual plugins
to better suit Geany's ethos of being as light as possible while allowing
users to select which features they want to add to the core editor. The idea
was taken from a Text Editor for Windows called ConText.

Normally if you had more than one bookmark, you would have to cycle through
them until you reached the one you wanted. With this plugin you can go
straight to the bookmark that you want with a single key combination.

%package geanypg
Summary:   encrypt, decrypt and verify signatures with GnuPG
Requires:  geany-plugins-common = %{version}-%{release}
Requires:  gpgme
%description geanypg
GeanyPG is a plugin for Geany that allows the user to encrypt, decrypt and
verify signatures with GnuPG.

%package geanyprj
Summary:   Provides an alternate project management tool for Geany
Requires:  geany-plugins-common = %{version}-%{release}
%description geanyprj
Geanyprj provides an alternate project management approach to Geany's built-in
project facility. The idea is to be less a "session manager" as the built-in
project management does: It allows/requires you to manually open and close
project and allows you to store project files in different locations from
project sources.

Geanyprj takes a different approach:
It never saves session information, so that project files can be stored in
version control without constant noise from changes of opened files or cursor
position. You also will never have to open/close projects manually. If a
*.geanyprj file is found somewhere up in path it will be opened automatically.

%package sendmail
Summary:   Send E-Mails from within Geany
Requires:  geany-plugins-common = %{version}-%{release}
Obsoletes: geany-plugins-geanysendmail < 1.28
%description sendmail
GeanySendMail is a little plugin to send a document as attachment using the
preferred mail client from inside Geany. It is similar to the envelope symbol
of most office tools and requires a mail client that supports remote calls.

%package geanyvc
Summary:   Version Control for Geany
Requires:  geany-plugins-common = %{version}-%{release}
Obsoletes: geanyvc <= 0.5
Provides:  geanyvc = %{version}-%{release}
%description geanyvc
Geanyvc is a plugin that provides a uniform way of accessing different version
control systems from within the Geany IDE. Currently, support for the following
version control systems is provided:

* Bazaar
* Git
* Mercurial
* Subversion
* SVK
* CVS

%package git-changebar
Summary:   Highlights uncommitted changes, and allows navigation through hunks
Requires:  geany-plugins-common = %{version}-%{release}
BuildRequires:  libgit2-devel
%description git-changebar
This plugin highlights uncommitted changes to files tracked with Git, and allows to navigate through the hunks.

%package geniuspaste
Summary:   Use nopaste services directly from within Geany
Requires:  geany-plugins-common = %{version}-%{release}
BuildRequires: libsoup-devel
%description geniuspaste
This plugin allows the user to paste the code from Geany into five different
pastebins. At the moment it supports this services:

* codepad.org
* tinypaste.com
* pastebin.geany.org
* dpaste.de
* sprunge.us

GeniusPaste detects automatically the syntax of the code and paste it with
syntax highlighting enabled. It can also display the pasted code opening a new
browser tab.

%package keyrecord
Summary:   Records and replays a sequence of keystrokes
Requires:  geany-plugins-common = %{version}-%{release}
%description keyrecord
This plugin allows you to record a sequence of keystrokes and to replay it
several times.

%package lineoperations
Summary:   Assortment of simple line functions that can be applied to an open file
Requires:  geany-plugins-common = %{version}-%{release}
%description lineoperations
Line Operations is an assortment of simple line functions that can be applied to an open file.

%package projectorganizer
Summary:   Extension of Geany's project management
Requires:  geany-plugins-common = %{version}-%{release}
Obsoletes: geany-plugins-gproject < 1.25
Provides:  geany-plugins-gproject >= 1.25
%description projectorganizer
ProjectOrganizer is an extension of Geany's project management displaying a tree of
files belonging to the project in the sidebar. In addition, it enables quick
swapping between header and source files, searching project files by name
and more. The plugin was created with big projects in mind so everything
works fast enough even with projects consisting of hundreds of thousands of
files.

%package markdown
Summary:       Real time preview for Markdown documents
Requires:      geany-plugins-common = %{version}-%{release}
BuildRequires: pkgconfig(webkit2gtk-4.1)
BuildRequires: python3-docutils
Provides:      geany-plugins-markdown >= 1.34
%description markdown
The Markdown plugin provides a real-time preview of rendered Markdown, that is,
Markdown converted to HTML and inserted into an HTML template and loaded
into a WebKit view.

%package overview
Summary:   Overview over the code in a sidebar
Requires:  geany-plugins-common = %{version}-%{release}
%description overview
This plugin provides overview over the code from bird perspective in a sidebar.

%package pairtaghighlighter
Summary:   Extension of Geany's project management
Requires:  geany-plugins-common = %{version}-%{release}
%description pairtaghighlighter
Find and highlight matching opening/closing HTML tags by clicking or moving the
cursor inside a tag.

%package pohelper
Summary:   Extension of Geany's project management
Requires:  geany-plugins-common = %{version}-%{release}
%description pohelper
A plugin for Geany that improves the support for GetText translation files, by
providing various features specific to this format and to translators.

Features:

* Navigation between all, untranslated or fuzzy messages;
* Reformatting of the translation (reflow);
* Toggling the fuzziness of a translation;
* Pasting of the untranslated string to the translation;
* Automatic updating of the translation metadata.

%package pretty-printer
Summary:   XML pretty printing plugin for Geany
Requires:  geany-plugins-common = %{version}-%{release}
Requires:  libxml2 >= 2.6.27
Obsoletes: geany-plugins-pretty-print <= 1.23
Provides:  geany-plugins-pretty-print >= 1.23
%description pretty-printer
Plugin for Geany to easily beautify XML code.

%package scope
Summary:   Graphical GDB front-end
Requires:  geany-plugins-common = %{version}-%{release}
Requires:  gdb >= 7.3
Provides:  geany-plugins-scope >= 1.32
%description scope
Scope is a graphical GDB front-end with the normal functions you would
expect (stepping, breakpoints...), and a few notable features:

* The communication between Scope and GDB is asynchronous
* You can enter any GDB command, at any time
  (of course, for the command to be executed, GDB must be[come] available)
* All GDB I/O (along with some other messages) is displayed in a terminal-like
  "Debug Console". Whenever you find the GUI lacking, simply switch to that
  console and work directly with GDB
* 7-bit/Locale/UTF-8 support for values.

%package shiftcolumn
Summary:   Move Blocks of Text horizontally
Requires:  geany-plugins-common = %{version}-%{release}
%description shiftcolumn
Shiftcolumn allows you to move blocks of text horizontally in Geany.

%package spellcheck
Summary:   Spellcheck Text in Geany using the Enchant Library
Requires:  geany-plugins-common = %{version}-%{release}
%description spellcheck
Spellcheck checks the selected text (or the whole document) with the spellcheck
library Enchant

%package tableconvert
Summary:   Helps on converting a tabulator separated selection into a table
Requires:  geany-plugins-common = %{version}-%{release}
%description tableconvert
Tableconvert is a plugin which helps on converting a tabulator separated
selection into a table.

%package treebrowser
Summary:   Alternate file browser plugin providing a tree view of directories
Requires:  geany-plugins-common = %{version}-%{release}
%description treebrowser
The tree browser plugin for Geany provides an alternate way to browse through
your files. It displays files and directories in a tree view and has more
features than the file browser plugin delivered with Geany itself.

%package updatechecker
Summary:   Automatically check for Geany updates
Requires:  geany-plugins-common = %{version}-%{release}
BuildRequires: libsoup-devel
%description updatechecker
UpdateChecker is a plugin for Geany, which is able to check whether there is
a more recent version of Geany available.

%package vimode
Summary:   Vim-mode plugin for Geany
Requires:  geany-plugins-common = %{version}-%{release}
BuildRequires: make
%description vimode
Vimode is a Vim-mode plugin for Geany written by a guy who does not use Vim.
Expect problems unexpected by a Vim user and, please, report them.

Despite the limited Vim knowledge of the author, the plugin tries to be a
reasonably complete Vim mode implementation featuring:

* normal mode, insert/replace mode, visual mode, line visual mode
* repeated commands (e.g. 10dd - delete 10 lines)
* "motion" commands (e.g. d10l - delete 10 characters to the right)
* "text object" commands (e.g. di( - delete inner contents of parentheses)
* visual mode commands (e.g. ~ to swap case of the selected text)
* basic ex mode commands like :s, including range specifications
* most basic navigation, selection and text manipulation commands
* command repetition using "." and repeated insert

%package webhelper
Summary:   Preview and Debug Web documents from within Geany using WebKit
Group:     Development/Tools
Requires:  geany-plugins-common = %{version}-%{release}
BuildRequires: pkgconfig(webkit2gtk-4.1)
%description webhelper
WebHelper is a plugin for Geany that provides some web development
facilities, such as a web page preview and some debugging tools (web
inspector).

Prominent features:

* A basic web view, allowing to display any web page (using WebKit)
* Possible automatic reloading of the web view upon document saving
* A web inspector/debugging tool for the web view's content (including a
  JavaScript console, a viewer and editor of processed HTML and CSS, a network
  usage analysis tool and many more, thanks to WebKit).

%package workbench
Summary:   Manage multiple projects in Geany
Requires:  geany-plugins-common = %{version}-%{release}
%description workbench
The Workbench plugin is an extension that makes it possible to manage multiple
projects in geany. You can add geany projects to a workbench. From there you
can add directories to the project to manage the files belonging to the
project.

%package xmlsnippets
Summary:   Extends XML/HTML tag autocompletion provided by Geany
Requires:  geany-plugins-common = %{version}-%{release}
%description xmlsnippets
This plugin extends XML/HTML tag autocompletion provided by Geany. It
automatically inserts a matching snippet after you type an opening tag.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf -fiv
%configure --docdir=%{geany_plug_docdir}
%make_build
%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -delete
find $RPM_BUILD_ROOT -type f -empty -delete
%find_lang %{name}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n geany-plugins-common -f %{oreon_filedir}/geany-plugins-common.list
%files -n geany-plugins-addons -f %{oreon_filedir}/geany-plugins-addons.list
%files -n geany-plugins-autoclose -f %{oreon_filedir}/geany-plugins-autoclose.list
%files -n geany-plugins-automark -f %{oreon_filedir}/geany-plugins-automark.list
%files -n geany-plugins-codenav -f %{oreon_filedir}/geany-plugins-codenav.list
%files -n geany-plugins-commander -f %{oreon_filedir}/geany-plugins-commander.list
%files -n geany-plugins-debugger -f %{oreon_filedir}/geany-plugins-debugger.list
%files -n geany-plugins-defineformat -f %{oreon_filedir}/geany-plugins-defineformat.list
%files -n geany-plugins-geanyctags -f %{oreon_filedir}/geany-plugins-geanyctags.list
%files -n geany-plugins-geanydoc -f %{oreon_filedir}/geany-plugins-geanydoc.list
%files -n geany-plugins-geanyextrasel -f %{oreon_filedir}/geany-plugins-geanyextrasel.list
%files -n geany-plugins-geanygendoc -f %{oreon_filedir}/geany-plugins-geanygendoc.list
%files -n geany-plugins-geanyinsertnum -f %{oreon_filedir}/geany-plugins-geanyinsertnum.list
%files -n geany-plugins-latex -f %{oreon_filedir}/geany-plugins-latex.list
%files -n geany-plugins-lipsum -f %{oreon_filedir}/geany-plugins-lipsum.list
%files -n geany-plugins-lsp -f %{oreon_filedir}/geany-plugins-lsp.list
%files -n geany-plugins-geanymacro -f %{oreon_filedir}/geany-plugins-geanymacro.list
%files -n geany-plugins-geanyminiscript -f %{oreon_filedir}/geany-plugins-geanyminiscript.list
%files -n geany-plugins-geanynumberedbookmarks -f %{oreon_filedir}/geany-plugins-geanynumberedbookmarks.list
%files -n geany-plugins-geanypg -f %{oreon_filedir}/geany-plugins-geanypg.list
%files -n geany-plugins-geanyprj -f %{oreon_filedir}/geany-plugins-geanyprj.list
%files -n geany-plugins-sendmail -f %{oreon_filedir}/geany-plugins-sendmail.list
%files -n geany-plugins-geanyvc -f %{oreon_filedir}/geany-plugins-geanyvc.list
%files -n geany-plugins-git-changebar -f %{oreon_filedir}/geany-plugins-git-changebar.list
%files -n geany-plugins-geniuspaste -f %{oreon_filedir}/geany-plugins-geniuspaste.list
%files -n geany-plugins-keyrecord -f %{oreon_filedir}/geany-plugins-keyrecord.list
%files -n geany-plugins-lineoperations -f %{oreon_filedir}/geany-plugins-lineoperations.list
%files -n geany-plugins-projectorganizer -f %{oreon_filedir}/geany-plugins-projectorganizer.list
%files -n geany-plugins-markdown -f %{oreon_filedir}/geany-plugins-markdown.list
%files -n geany-plugins-overview -f %{oreon_filedir}/geany-plugins-overview.list
%files -n geany-plugins-pairtaghighlighter -f %{oreon_filedir}/geany-plugins-pairtaghighlighter.list
%files -n geany-plugins-pohelper -f %{oreon_filedir}/geany-plugins-pohelper.list
%files -n geany-plugins-pretty-printer -f %{oreon_filedir}/geany-plugins-pretty-printer.list
%files -n geany-plugins-scope -f %{oreon_filedir}/geany-plugins-scope.list
%files -n geany-plugins-shiftcolumn -f %{oreon_filedir}/geany-plugins-shiftcolumn.list
%files -n geany-plugins-spellcheck -f %{oreon_filedir}/geany-plugins-spellcheck.list
%files -n geany-plugins-tableconvert -f %{oreon_filedir}/geany-plugins-tableconvert.list
%files -n geany-plugins-treebrowser -f %{oreon_filedir}/geany-plugins-treebrowser.list
%files -n geany-plugins-updatechecker -f %{oreon_filedir}/geany-plugins-updatechecker.list
%files -n geany-plugins-vimode -f %{oreon_filedir}/geany-plugins-vimode.list
%files -n geany-plugins-webhelper -f %{oreon_filedir}/geany-plugins-webhelper.list
%files -n geany-plugins-workbench -f %{oreon_filedir}/geany-plugins-workbench.list
%files -n geany-plugins-xmlsnippets -f %{oreon_filedir}/geany-plugins-xmlsnippets.list

%changelog

%autochangelog
