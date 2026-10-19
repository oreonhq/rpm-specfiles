%global source0_hash efe8d36d7aec7e4b4c297de42ca7af43e1d89eb410970b817101854409b19eef
Name:           flexmark-java
Version:        0.64.6
Release:        1%{?dist}
Summary:        CommonMark/Markdown Java parser with source level AST
License:        BSD-2-Clause
URL:            https://github.com/vsch/flexmark-java
VCS:            git:%{url}.git
Source0:        https://github.com/vsch/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch:          0001-Fix-abbreviations-matching-with-Java-19.patch
Patch:          %{url}/pull/578.patch
Patch:          %{name}-jsoup.patch
BuildArch:      noarch
ExclusiveArch:  noarch %{java_arches}
Requires:       %{name}-util-ast = %{version}-%{release}
Requires:       %{name}-util-builder = %{version}-%{release}
Requires:       %{name}-util-collection = %{version}-%{release}
Requires:       %{name}-util-data = %{version}-%{release}
Requires:       %{name}-util-dependency = %{version}-%{release}
Requires:       %{name}-util-format = %{version}-%{release}
Requires:       %{name}-util-html = %{version}-%{release}
Requires:       %{name}-util-misc = %{version}-%{release}
Requires:       %{name}-util-sequence = %{version}-%{release}
Requires:       %{name}-util-visitor = %{version}-%{release}
%global _desc %{expand:Flexmark-java is a Java CommonMark (spec 0.28) parser using the blocks first,
inlines after Markdown parsing architecture.
Its strengths are speed, flexibility, Markdown source element based AST with
details of the source position down to individual characters of lexemes that
make up the element and extensibility.
The API allows granular control of the parsing process and is optimized for
parsing with a large number of installed extensions.  The parser and
extensions come with plenty of options for parser behavior and HTML rendering
variations.  The end goal is to have the parser and renderer be able to mimic
other parsers with great degree of accuracy.  This is now partially complete
with the implementation of Markdown Processor Emulation.}
# oreon:deps
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.logging.log4j:log4j-1.2-api)
BuildRequires:  mvn(org.apache.logging.log4j:log4j-api)
BuildRequires:  mvn(org.apache.logging.log4j:log4j-core)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-jar-plugin)
BuildRequires:  mvn(org.jetbrains:annotations)
BuildRequires:  mvn(org.jsoup:jsoup)
BuildRequires:  mvn(org.nibor.autolink:autolink)
BuildRequires:  mvn(org.slf4j:slf4j-api)
# /oreon:deps
%description
%_desc

This package contains the core library for parsing markdown and rendering to
HTML.

%{?javadoc_package}

%package        all
Summary:        All flexmark extension and converter modules
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-ext-abbreviation = %{version}-%{release}
Requires:       %{name}-ext-admonition = %{version}-%{release}
Requires:       %{name}-ext-anchorlink = %{version}-%{release}
Requires:       %{name}-ext-aside = %{version}-%{release}
Requires:       %{name}-ext-attributes = %{version}-%{release}
Requires:       %{name}-ext-autolink = %{version}-%{release}
Requires:       %{name}-ext-definition = %{version}-%{release}
Requires:       %{name}-ext-emoji = %{version}-%{release}
Requires:       %{name}-ext-enumerated-reference = %{version}-%{release}
Requires:       %{name}-ext-escaped-character = %{version}-%{release}
Requires:       %{name}-ext-footnotes = %{version}-%{release}
Requires:       %{name}-ext-gfm-issues = %{version}-%{release}
Requires:       %{name}-ext-gfm-strikethrough = %{version}-%{release}
Requires:       %{name}-ext-gfm-tasklist = %{version}-%{release}
Requires:       %{name}-ext-gfm-users = %{version}-%{release}
Requires:       %{name}-ext-gitlab = %{version}-%{release}
Requires:       %{name}-ext-jekyll-front-matter = %{version}-%{release}
Requires:       %{name}-ext-jekyll-tag = %{version}-%{release}
Requires:       %{name}-ext-media-tags = %{version}-%{release}
Requires:       %{name}-ext-resizable-image = %{version}-%{release}
Requires:       %{name}-ext-macros = %{version}-%{release}
Requires:       %{name}-ext-ins = %{version}-%{release}
Requires:       %{name}-ext-xwiki-macros = %{version}-%{release}
Requires:       %{name}-ext-superscript = %{version}-%{release}
Requires:       %{name}-ext-tables = %{version}-%{release}
Requires:       %{name}-ext-toc = %{version}-%{release}
Requires:       %{name}-ext-typographic = %{version}-%{release}
Requires:       %{name}-ext-wikilink = %{version}-%{release}
Requires:       %{name}-ext-yaml-front-matter = %{version}-%{release}
Requires:       %{name}-ext-youtube-embedded = %{version}-%{release}
Requires:       %{name}-html2md-converter = %{version}-%{release}
Requires:       %{name}-jira-converter = %{version}-%{release}
Requires:       %{name}-util-ast = %{version}-%{release}
Requires:       %{name}-util-builder = %{version}-%{release}
Requires:       %{name}-util-collection = %{version}-%{release}
Requires:       %{name}-util-data = %{version}-%{release}
Requires:       %{name}-util-dependency = %{version}-%{release}
Requires:       %{name}-util-format = %{version}-%{release}
Requires:       %{name}-util-html = %{version}-%{release}
Requires:       %{name}-util-misc = %{version}-%{release}
Requires:       %{name}-util-options = %{version}-%{release}
Requires:       %{name}-util-sequence = %{version}-%{release}
Requires:       %{name}-util-visitor = %{version}-%{release}
Requires:       %{name}-youtrack-converter = %{version}-%{release}
%description    all
%_desc

This package provides all of the extension and converter modules.

%package        ext-abbreviation
Summary:        Flexmark extension for abbreviations in text
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-ext-autolink = %{version}-%{release}
Requires:       %{name}-util = %{version}-%{release}
%description    ext-abbreviation
%_desc

This package contains an extension for defining abbreviations and
turning appearance of these abbreviations in text into <abbr> tags with
titles consisting of the expansion of the abbreviation.

%package        ext-admonition
Summary:        Flexmark extension for admonition syntax processing
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-util = %{version}-%{release}
%description    ext-admonition
%_desc

This package contains an extension for Admonition Extension, Material
for MkDocs syntax processing, to create block-styled side content.

%package        ext-anchorlink
Summary:        Flexmark extension to generate anchor links for headers
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-util = %{version}-%{release}
%description    ext-anchorlink
%_desc

This package contains an extension for generating anchor links for
headings using a GitHub-compatible ID algorithm, with options for the
rendered HTML tags.

%package        ext-aside
Summary:        Flexmark extension for converting | to aside tags
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-jira-converter = %{version}-%{release}
Requires:       %{name}-util = %{version}-%{release}
%description    ext-aside
%_desc

This package contains an extension for converting text prefixed with `|`
to aside tags.  The syntax is the same as block quotes with the marker
changed to `|`.

%package        ext-attributes
Summary:        Flexmark extension for attributes
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-util = %{version}-%{release}
%description    ext-attributes
%_desc

This package contains an extension that converts attribute syntax
(`{...}`) into attribute AST nodes and adds an attribute provider to set
attributes for the immediately preceding sibling element during HTML
rendering.

%package        ext-autolink
Summary:        Flexmark extension for autolinking
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-util = %{version}-%{release}
%description    ext-autolink
%_desc

This package contains an extension for turning plain URLs and email
addresses into links.

%package        ext-definition
Summary:        Flexmark extension for definition list processing
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-util = %{version}-%{release}
%description    ext-definition
%_desc

This package contains an extension for definition list processing.

%package        ext-emoji
Summary:        Flexmark extension for emoji shortcuts
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-jira-converter = %{version}-%{release}
Requires:       %{name}-util = %{version}-%{release}
%description    ext-emoji
%_desc

This package contains an extension for emoji shortcuts.  It converts
Emoji Cheat Sheet and GitHub Emoji API shortcuts to characters on the
Unicode Emoji List.

%package        ext-enumerated-reference
Summary:        Flexmark extension for enumerated reference processing
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-ext-attributes = %{version}-%{release}
Requires:       %{name}-util = %{version}-%{release}
%description    ext-enumerated-reference
%_desc

This package contains an extension for enumerated reference processing.

%package        ext-escaped-character
Summary:        Flexmark extension for escaped characters
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-util = %{version}-%{release}
%description    ext-escaped-character
%_desc

This package contains an extension for converting escaped characters to
AST EscapedCharacter nodes.  It has no effect on rendered HTML.

%package        ext-footnotes
Summary:        Flexmark extension for footnotes
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-util = %{version}-%{release}
%description    ext-footnotes
%_desc

This package contains an extension that converts footnote references and
definitions to HTML footnotes.

%package        ext-gfm-issues
Summary:        Flexmark extension for GitHub issue syntax
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-util = %{version}-%{release}
%description    ext-gfm-issues
%_desc

This package contains an extension that converts GitHub Flavored
Markdown issue syntax to HTML links.

%package        ext-gfm-strikethrough
Summary:        Flexmark extension for GitHub strikethrough syntax
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-util = %{version}-%{release}
%description    ext-gfm-strikethrough
%_desc

This package contains an extension that converts GitHub Flavored
Markdown strikethrough syntax (~~) to HTML.

%package        ext-gfm-tasklist
Summary:        Flexmark extension for GitHub task list items
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-util = %{version}-%{release}
%description    ext-gfm-tasklist
%_desc

This package contains an extension that converts GitHub Flavored
Markdown bullet list items that start with [ ], [x], or [X] to an AST
TaskListItem node.

%package        ext-gfm-users
Summary:        Flexmark extension for GitHub user syntax
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-util = %{version}-%{release}
%description    ext-gfm-users
%_desc

This package contains an extension that converts GitHub Flavored
Markdown user syntax to links.

%package        ext-gitlab
Summary:        Flexmark extension for GitLab Flavored Markdown
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-util = %{version}-%{release}
%description    ext-gitlab
%_desc

This package contains an extension that parses and renders GitLab
Flavored Markdown.

%package        ext-ins
Summary:        Flexmark extension for inserted text
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-util = %{version}-%{release}
%description    ext-ins
%_desc

This package contains an extension that converts `++text++` syntax into
`<ins>text</ins>`, the HTML syntax for inserted text.

%package        ext-jekyll-front-matter
Summary:        Flexmark extension for Jekyll front matter
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-ext-yaml-front-matter = %{version}-%{release}
Requires:       %{name}-util = %{version}-%{release}
%description    ext-jekyll-front-matter
%_desc

This package contains an extension that converts Jekyll front matter
YAML to an AST JekyllFrontMatterBlock node.

%package        ext-jekyll-tag
Summary:        Flexmark extension for Jekyll tag parsing
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-util = %{version}-%{release}
%description    ext-jekyll-tag
%_desc

This package contains an extension that converts Jekyll tags of the form
`{% tag tag-parameters %}` into AST JekyllTag or JekyllTagBlock nodes.

%package        ext-macros
Summary:        Flexmark extension for processing macros
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-ext-gitlab = %{version}-%{release}
Requires:       %{name}-util = %{version}-%{release}
%description    ext-macros
%_desc

This package contains an extension that converts macro text to macro
definitions and macro references.

%package        ext-media-tags
Summary:        Flexmark extension for HTML5 media tags
Requires:       %{name} = %{version}-%{release}
%description    ext-media-tags
%_desc

This package contains an extension for embedding media using HTML5 media
tags, in particular the audio, embed, picture, and video tags.

%package        ext-resizable-image
Summary:        Flexmark extension to set image size
Requires:       %{name} = %{version}-%{release}
%description    ext-resizable-image
%_desc

This package contains an extension to set the width and height of images
by stating them as `![text](/src =WxH)`, which is used in Azure DevOps
markdown.

%package        ext-spec-example
Summary:        Flexmark extension for spec test example processing
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-test-util = %{version}-%{release}
Requires:       %{name}-util = %{version}-%{release}
%description    ext-spec-example
%_desc

This package contains an extension that converts flexmark spec example
syntax into AST nodes.

%package        ext-superscript
Summary:        Flexmark extension for superscript processing
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-util = %{version}-%{release}
%description    ext-superscript
%_desc

This package contains an extension that converts `^superscript^` syntax
into `<sup>superscript</sup>`.

%package        ext-tables
Summary:        Flexmark extension for tables
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-util = %{version}-%{release}
%description    ext-tables
%_desc

This package contains an extension for tables using `|` pipes with
optional column spans and table caption.

%package        ext-toc
Summary:        Flexmark extension for table of contents
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-util = %{version}-%{release}
%description    ext-toc
%_desc

This package contains an extension that converts `[TOC style]` text to
AST TocBlock, SimToc, and SimTocContent nodes.

%package        ext-typographic
Summary:        Flexmark extension for typographic processing
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-util = %{version}-%{release}
%description    ext-typographic
%_desc

This package contains an extension for typographic processing.  It
converts:
- apostrophe (`'`) to `&rsquo;`
- ellipsis (`...` or `. . .`) to `&hellip;`
- en dash (`--`) to `&ndash;`
- em dash (`---`) to `&mdash;`
- single quoted `'text'` to `&lsquo;text&rsquo;`
- double quoted `"text"` to `&ldquo;text&rdquo;`
- double angle quoted `<<text>>` to `&laquo;text&raquo;`

%package        ext-wikilink
Summary:        Flexmark extension for wiki links
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-util = %{version}-%{release}
%description    ext-wikilink
%_desc

This package contains an extension that converts references that are
wrapped in `[[]]` into wiki links with optional text separated by `|`.
Optional syntax to convert `![[]]` to image links is available.

%package        ext-xwiki-macros
Summary:        Flexmark extension for xwiki application-specific macros
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-util = %{version}-%{release}
%description    ext-xwiki-macros
%_desc

This package contains an extension for xwiki application-specific
macros.  Both block and inline macros are supported.

%package        ext-yaml-front-matter
Summary:        Flexmark extension for YAML front matter
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-util = %{version}-%{release}
%description    ext-yaml-front-matter
%_desc

This package contains an extension for YAML front matter.

%package        ext-youtube-embedded
Summary:        Flexmark extension for YouTube links
Requires:       %{name} = %{version}-%{release}
%description    ext-youtube-embedded
%_desc

This package contains an extension for converting YouTube links to
embedded video iframes.

%package        ext-zzzzzz
Summary:        Flexmark extension for zzzzzz
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-util = %{version}-%{release}
%description    ext-zzzzzz
%_desc

This package contains an extension that supports zzzzzz syntax.

%package        html2md-converter
Summary:        Flexmark HTML to Markdown extensible converter
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-ext-emoji = %{version}-%{release}
Requires:       %{name}-util = %{version}-%{release}
%description    html2md-converter
%_desc

This package contains a customizable extension to convert HTML to
Markdown.

%package        jira-converter
Summary:        Convert flexmark AST to Jira formatted text
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-ext-gfm-strikethrough = %{version}-%{release}
Requires:       %{name}-ext-ins = %{version}-%{release}
Requires:       %{name}-ext-superscript = %{version}-%{release}
Requires:       %{name}-ext-tables = %{version}-%{release}
Requires:       %{name}-ext-wikilink = %{version}-%{release}
Requires:       %{name}-util = %{version}-%{release}
%description    jira-converter
%_desc

This package contains an extension for rendering flexmark AST as Jira
formatted text.

%package        osgi
Summary:        Flexmark OSGi bundle
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-ext-abbreviation = %{version}-%{release}
Requires:       %{name}-ext-admonition = %{version}-%{release}
Requires:       %{name}-ext-anchorlink = %{version}-%{release}
Requires:       %{name}-ext-aside = %{version}-%{release}
Requires:       %{name}-ext-attributes = %{version}-%{release}
Requires:       %{name}-ext-autolink = %{version}-%{release}
Requires:       %{name}-ext-definition = %{version}-%{release}
Requires:       %{name}-ext-emoji = %{version}-%{release}
Requires:       %{name}-ext-enumerated-reference = %{version}-%{release}
Requires:       %{name}-ext-escaped-character = %{version}-%{release}
Requires:       %{name}-ext-footnotes = %{version}-%{release}
Requires:       %{name}-ext-gfm-issues = %{version}-%{release}
Requires:       %{name}-ext-gfm-strikethrough = %{version}-%{release}
Requires:       %{name}-ext-gfm-tasklist = %{version}-%{release}
Requires:       %{name}-ext-gfm-users = %{version}-%{release}
Requires:       %{name}-ext-gitlab = %{version}-%{release}
Requires:       %{name}-ext-jekyll-front-matter = %{version}-%{release}
Requires:       %{name}-ext-jekyll-tag = %{version}-%{release}
Requires:       %{name}-ext-media-tags = %{version}-%{release}
Requires:       %{name}-ext-resizable-image = %{version}-%{release}
Requires:       %{name}-ext-ins = %{version}-%{release}
Requires:       %{name}-ext-xwiki-macros = %{version}-%{release}
Requires:       %{name}-ext-superscript = %{version}-%{release}
Requires:       %{name}-ext-tables = %{version}-%{release}
Requires:       %{name}-ext-toc = %{version}-%{release}
Requires:       %{name}-ext-typographic = %{version}-%{release}
Requires:       %{name}-ext-wikilink = %{version}-%{release}
Requires:       %{name}-ext-yaml-front-matter = %{version}-%{release}
Requires:       %{name}-ext-youtube-embedded = %{version}-%{release}
Requires:       %{name}-html2md-converter = %{version}-%{release}
Requires:       %{name}-jira-converter = %{version}-%{release}
Requires:       %{name}-util = %{version}-%{release}
Requires:       %{name}-util-ast = %{version}-%{release}
Requires:       %{name}-util-builder = %{version}-%{release}
Requires:       %{name}-util-collection = %{version}-%{release}
Requires:       %{name}-util-data = %{version}-%{release}
Requires:       %{name}-util-dependency = %{version}-%{release}
Requires:       %{name}-util-format = %{version}-%{release}
Requires:       %{name}-util-html = %{version}-%{release}
Requires:       %{name}-util-misc = %{version}-%{release}
Requires:       %{name}-util-options = %{version}-%{release}
Requires:       %{name}-util-sequence = %{version}-%{release}
Requires:       %{name}-util-visitor = %{version}-%{release}
Requires:       %{name}-youtrack-converter = %{version}-%{release}
%description    osgi
%_desc

This package contains all extension modules and converter modules except
the PDF converter in OSGi bundle format.

%package        test-util
Summary:        Flexmark test utilities
Requires:       %{name}-util-ast = %{version}-%{release}
Requires:       %{name}-util-data = %{version}-%{release}
Requires:       %{name}-util-format = %{version}-%{release}
Requires:       %{name}-util-misc = %{version}-%{release}
Requires:       %{name}-util-sequence = %{version}-%{release}
%description    test-util
%_desc

This package contains test utilities.

%package        tree-iteration
Summary:        Flexmark library for recursive tree iteration
Requires:       %{name}-util-ast = %{version}-%{release}
Requires:       %{name}-util-collection = %{version}-%{release}
Requires:       %{name}-util-data = %{version}-%{release}
%description    tree-iteration
%_desc

This package contains a library that allows recursive child and sibling
iteration with filtering, recursion and item mapping provided by
downstream users.

%package        util
Summary:        Flexmark utility classes
Requires:       %{name}-util-ast = %{version}-%{release}
Requires:       %{name}-util-builder = %{version}-%{release}
Requires:       %{name}-util-collection = %{version}-%{release}
Requires:       %{name}-util-data = %{version}-%{release}
Requires:       %{name}-util-dependency = %{version}-%{release}
Requires:       %{name}-util-format = %{version}-%{release}
Requires:       %{name}-util-html = %{version}-%{release}
Requires:       %{name}-util-misc = %{version}-%{release}
Requires:       %{name}-util-options = %{version}-%{release}
Requires:       %{name}-util-sequence = %{version}-%{release}
Requires:       %{name}-util-visitor = %{version}-%{release}
%description    util
%_desc

This package contains utility classes.

%package        util-ast
Summary:        Flexmark AST utilities
Requires:       %{name}-util-collection = %{version}-%{release}
Requires:       %{name}-util-data = %{version}-%{release}
Requires:       %{name}-util-misc = %{version}-%{release}
Requires:       %{name}-util-sequence = %{version}-%{release}
Requires:       %{name}-util-visitor = %{version}-%{release}
%description    util-ast
%_desc

This package contains AST utility classes.

%package        util-builder
Summary:        Flexmark builder utilities
Requires:       %{name}-util-data = %{version}-%{release}
Requires:       %{name}-util-misc = %{version}-%{release}
%description    util-builder
%_desc

This package contains builder utility classes.

%package        util-collection
Summary:        Flexmark collection utilities
Requires:       %{name}-util-misc = %{version}-%{release}
%description    util-collection
%_desc

This package contains collection utility classes.

%package        util-data
Summary:        Flexmark data utilities
Requires:       %{name}-util-misc = %{version}-%{release}
%description    util-data
%_desc

This package contains data utility classes.

%package        util-dependency
Summary:        Flexmark dependency utilities
Requires:       %{name}-util-collection = %{version}-%{release}
Requires:       %{name}-util-data = %{version}-%{release}
Requires:       %{name}-util-misc = %{version}-%{release}
%description    util-dependency
%_desc

This package contains dependency utility classes.

%package        util-experimental
Summary:        Flexmark experimental utilities
Requires:       %{name}-util-ast = %{version}-%{release}
Requires:       %{name}-util-collection = %{version}-%{release}
Requires:       %{name}-util-data = %{version}-%{release}
Requires:       %{name}-util-misc = %{version}-%{release}
Requires:       %{name}-util-sequence = %{version}-%{release}
%description    util-experimental
%_desc

This package contains experimental utility classes that may or may not
work in all cases.  Use at your own risk.

%package        util-format
Summary:        Flexmark format utilities
Requires:       %{name}-util-ast = %{version}-%{release}
Requires:       %{name}-util-collection = %{version}-%{release}
Requires:       %{name}-util-data = %{version}-%{release}
Requires:       %{name}-util-html = %{version}-%{release}
Requires:       %{name}-util-misc = %{version}-%{release}
Requires:       %{name}-util-sequence = %{version}-%{release}
%description    util-format
%_desc

This package contains format utility classes.

%package        util-html
License:        BSD-2-Clause AND Apache-2.0
Summary:        Flexmark HTML utilities
Requires:       %{name}-util-misc = %{version}-%{release}
Requires:       %{name}-util-sequence = %{version}-%{release}
%description    util-html
%_desc

This package contains HTML utility classes.

%package        util-misc
License:        BSD-2-Clause AND Apache-2.0
Summary:        Flexmark miscellaneous utilities
%description    util-misc
%_desc

This package contains miscellaneous utility classes.

%package        util-options
Summary:        Flexmark options utilities
Requires:       %{name}-util-misc = %{version}-%{release}
Requires:       %{name}-util-sequence = %{version}-%{release}
%description    util-options
%_desc

This package contains options utility classes.

%package        util-sequence
Summary:        Flexmark sequence utilities
Requires:       %{name}-util-collection = %{version}-%{release}
Requires:       %{name}-util-data = %{version}-%{release}
Requires:       %{name}-util-misc = %{version}-%{release}
%description    util-sequence
%_desc

This package contains sequence utility classes.

%package        util-visitor
Summary:        Flexmark visitor utilities
%description    util-visitor
%_desc

This package contains visitor utility classes.

%package        youtrack-converter
Summary:        Flexmark extension for YouTrack conversion
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-ext-gfm-strikethrough = %{version}-%{release}
Requires:       %{name}-ext-tables = %{version}-%{release}
Requires:       %{name}-util = %{version}-%{release}
%description    youtrack-converter
%_desc

This package contains an extension that renders flexmark AST as YouTrack
formatted text (before YouTrack implemented Markdown comment option).

%prep

%autosetup -p1

%conf
# Remove prebuilt jars
rm lib/*.jar

# Not needed for an RPM build
%pom_remove_plugin org.codehaus.mojo:versions-maven-plugin

# We do not want to run benchmarks
%pom_remove_dep -r org.openjdk.jmh:jmh-core
%pom_remove_dep -r org.openjdk.jmh:jmh-generator-annprocess
rm flexmark-core-test/src/test/java/com/vladsch/flexmark/core/test/util/parser/SpecBenchmark.java

# Pegdown is not available in Fedora
%pom_remove_dep -r org.pegdown:pegdown
%pom_remove_dep com.vladsch.flexmark:flexmark-profile-pegdown flexmark-all
%pom_remove_dep com.vladsch.flexmark:flexmark-profile-pegdown flexmark-osgi
%pom_disable_module flexmark-profile-pegdown
rm flexmark-integration-test/src/test/java/com/vladsch/flexmark/integration/test/PegDownBenchmark.java

# Disable due to missing docx4j dependency
%pom_disable_module flexmark-docx-converter

# Disable due to missing openhtmltopdf dependency
%pom_disable_module flexmark-pdf-converter
%pom_remove_dep com.vladsch.flexmark:flexmark-pdf-converter flexmark-all

%build

%mvn_build -s
%install
%mvn_install
for m in core-test integration-test test-specs; do
  rm %{buildroot}%{_javadir}/flexmark-java/flexmark-$m.jar
  rm %{buildroot}%{_mavenpomdir}/flexmark-java/flexmark-$m.pom
  rm %{buildroot}%{_datadir}/maven-metadata/flexmark-java-flexmark-$m.xml
done
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n flexmark-java-all -f %{oreon_filedir}/flexmark-java-all.list
%files -n flexmark-java-ext-abbreviation -f %{oreon_filedir}/flexmark-java-ext-abbreviation.list
%files -n flexmark-java-ext-admonition -f %{oreon_filedir}/flexmark-java-ext-admonition.list
%files -n flexmark-java-ext-anchorlink -f %{oreon_filedir}/flexmark-java-ext-anchorlink.list
%files -n flexmark-java-ext-aside -f %{oreon_filedir}/flexmark-java-ext-aside.list
%files -n flexmark-java-ext-attributes -f %{oreon_filedir}/flexmark-java-ext-attributes.list
%files -n flexmark-java-ext-autolink -f %{oreon_filedir}/flexmark-java-ext-autolink.list
%files -n flexmark-java-ext-definition -f %{oreon_filedir}/flexmark-java-ext-definition.list
%files -n flexmark-java-ext-emoji -f %{oreon_filedir}/flexmark-java-ext-emoji.list
%files -n flexmark-java-ext-enumerated-reference -f %{oreon_filedir}/flexmark-java-ext-enumerated-reference.list
%files -n flexmark-java-ext-escaped-character -f %{oreon_filedir}/flexmark-java-ext-escaped-character.list
%files -n flexmark-java-ext-footnotes -f %{oreon_filedir}/flexmark-java-ext-footnotes.list
%files -n flexmark-java-ext-gfm-issues -f %{oreon_filedir}/flexmark-java-ext-gfm-issues.list
%files -n flexmark-java-ext-gfm-strikethrough -f %{oreon_filedir}/flexmark-java-ext-gfm-strikethrough.list
%files -n flexmark-java-ext-gfm-tasklist -f %{oreon_filedir}/flexmark-java-ext-gfm-tasklist.list
%files -n flexmark-java-ext-gfm-users -f %{oreon_filedir}/flexmark-java-ext-gfm-users.list
%files -n flexmark-java-ext-gitlab -f %{oreon_filedir}/flexmark-java-ext-gitlab.list
%files -n flexmark-java-ext-ins -f %{oreon_filedir}/flexmark-java-ext-ins.list
%files -n flexmark-java-ext-jekyll-front-matter -f %{oreon_filedir}/flexmark-java-ext-jekyll-front-matter.list
%files -n flexmark-java-ext-jekyll-tag -f %{oreon_filedir}/flexmark-java-ext-jekyll-tag.list
%files -n flexmark-java-ext-macros -f %{oreon_filedir}/flexmark-java-ext-macros.list
%files -n flexmark-java-ext-media-tags -f %{oreon_filedir}/flexmark-java-ext-media-tags.list
%files -n flexmark-java-ext-resizable-image -f %{oreon_filedir}/flexmark-java-ext-resizable-image.list
%files -n flexmark-java-ext-spec-example -f %{oreon_filedir}/flexmark-java-ext-spec-example.list
%files -n flexmark-java-ext-superscript -f %{oreon_filedir}/flexmark-java-ext-superscript.list
%files -n flexmark-java-ext-tables -f %{oreon_filedir}/flexmark-java-ext-tables.list
%files -n flexmark-java-ext-toc -f %{oreon_filedir}/flexmark-java-ext-toc.list
%files -n flexmark-java-ext-typographic -f %{oreon_filedir}/flexmark-java-ext-typographic.list
%files -n flexmark-java-ext-wikilink -f %{oreon_filedir}/flexmark-java-ext-wikilink.list
%files -n flexmark-java-ext-xwiki-macros -f %{oreon_filedir}/flexmark-java-ext-xwiki-macros.list
%files -n flexmark-java-ext-yaml-front-matter -f %{oreon_filedir}/flexmark-java-ext-yaml-front-matter.list
%files -n flexmark-java-ext-youtube-embedded -f %{oreon_filedir}/flexmark-java-ext-youtube-embedded.list
%files -n flexmark-java-ext-zzzzzz -f %{oreon_filedir}/flexmark-java-ext-zzzzzz.list
%files -n flexmark-java-html2md-converter -f %{oreon_filedir}/flexmark-java-html2md-converter.list
%files -n flexmark-java-jira-converter -f %{oreon_filedir}/flexmark-java-jira-converter.list
%files -n flexmark-java-osgi -f %{oreon_filedir}/flexmark-java-osgi.list
%files -n flexmark-java-test-util -f %{oreon_filedir}/flexmark-java-test-util.list
%files -n flexmark-java-tree-iteration -f %{oreon_filedir}/flexmark-java-tree-iteration.list
%files -n flexmark-java-util -f %{oreon_filedir}/flexmark-java-util.list
%files -n flexmark-java-util-ast -f %{oreon_filedir}/flexmark-java-util-ast.list
%files -n flexmark-java-util-builder -f %{oreon_filedir}/flexmark-java-util-builder.list
%files -n flexmark-java-util-collection -f %{oreon_filedir}/flexmark-java-util-collection.list
%files -n flexmark-java-util-data -f %{oreon_filedir}/flexmark-java-util-data.list
%files -n flexmark-java-util-dependency -f %{oreon_filedir}/flexmark-java-util-dependency.list
%files -n flexmark-java-util-experimental -f %{oreon_filedir}/flexmark-java-util-experimental.list
%files -n flexmark-java-util-format -f %{oreon_filedir}/flexmark-java-util-format.list
%files -n flexmark-java-util-html -f %{oreon_filedir}/flexmark-java-util-html.list
%files -n flexmark-java-util-misc -f %{oreon_filedir}/flexmark-java-util-misc.list
%files -n flexmark-java-util-options -f %{oreon_filedir}/flexmark-java-util-options.list
%files -n flexmark-java-util-sequence -f %{oreon_filedir}/flexmark-java-util-sequence.list
%files -n flexmark-java-util-visitor -f %{oreon_filedir}/flexmark-java-util-visitor.list
%files -n flexmark-java-youtrack-converter -f %{oreon_filedir}/flexmark-java-youtrack-converter.list

%changelog

%autochangelog
