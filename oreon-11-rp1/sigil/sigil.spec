%global source0_hash none

Name:           sigil
Version:        2.7.6
Release:        1%{?dist}
Summary:        WYSIWYG ebook editor
# Automatically converted from old format: GPL-3.0-or-later AND Apache-2.0 - review is highly recommended.
License:        GPL-3.0-or-later AND Apache-2.0
URL:            https://sigil-ebook.com/
Source0:        https://github.com/Sigil-Ebook/Sigil/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.appdata.xml
Patch1:         %{name}-0.8.0-system-dicts.patch
Patch2:         %{name}-0.9.3-global-plugin-support.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1632199
# port to minizip 2.x for F-30+
Patch3:         %{name}-1.9.20-minizip2.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  cmake

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6WebEngineCore)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Svg)

BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(hunspell)
BuildRequires:  pkgconfig(libpcre2-16)
BuildRequires:  cmake(minizip)
BuildRequires:  pkgconfig(python3)
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

# For the plugins
Requires:       python3-pillow python3-cssselect python3-cssutils
Requires:       python3-html5lib python3-lxml python3-pyside6
Requires:       python3-regex python3-chardet python3-six
Requires:       hicolor-icon-theme
# See internal/about.md for rationale for this
Provides:       bundled(gumbo) = 0.9.2
Provides:       bundled(nodejs-mathjax) = 2.75

ExclusiveArch: %{qt6_qtwebengine_arches}
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:   %{ix86}

%description
Sigil is a multi-platform WYSIWYG ebook editor. It is designed to edit books
in ePub format.

Now what does it have to offer...

    * Full Unicode support: everything you see in Sigil is in UTF-16
    * Full EPUB spec support
    * WYSIWYG editing
    * Multiple Views: Book View, Code View and Split View
    * Metadata editor with full support for all possible metadata entries with
      full descriptions for each
    * Table Of Contents editor
    * Multi-level TOC support
    * Book View fully supports the display of any XHTML document possible under
      the OPS spec
    * SVG support
    * Basic XPGT support
    * Advanced automatic conversion of all imported documents to Unicode
    * Currently imports TXT, HTML and EPUB files; more will be added with time
    * Embedded HTML Tidy; all imported documents are thoroughly cleaned;
      changing views cleans the document so no matter how much you screw up
      your code, it will fix it (usually) 

%package doc
# Automatically converted from old format: CC-BY-SA - review is highly recommended.
License:        LicenseRef-Callaway-CC-BY-SA
Summary:        Documentation for Sigil ebook editor
BuildArch:      noarch

%description doc
%{summary}.

%prep
%autosetup -p1 -n Sigil-%{version}

# Fix hunspell library lookup from python
hver=$(ls -1 %{_libdir}/libhunspell*.so | sed 's/.*hunspell\(-.*\)\.so/\1/')
sed "s/find_library('hunspell')/find_library('hunspell$hver')/" \
  src/Resource_Files/plugin_launchers/python/pluginhunspell.py

#fixtimestamp src/Resource_Files/plugin_launchers/python/pluginhunspell.py

# remove unbundled libs
rm -rf 3rdparty/{minizip,zlib,hunspell,pcre2}

%build
%cmake -DUSE_SYSTEM_LIBS=1 -DSYSTEM_LIBS_REQUIRED=1 \
  -DDISABLE_UPDATE_CHECK=1 -DINSTALL_HICOLOR_ICONS=1 \
  -DINSTALL_BUNDLED_DICTS=0 -DSHARE_INSTALL_PREFIX:PATH=%{_prefix}
%cmake_build

%install
%cmake_install

# Make rpmlint happy
#chmod +x %{buildroot}%{_datadir}/%{name}/python3lib/*.py
#chmod +x %{buildroot}%{_datadir}/%{name}/plugin_launchers/python/*.py
#chmod -x %{buildroot}%{_datadir}/%{name}/plugin_launchers/python/sigil_gumbo_bs4_adapter.py

# fix shebang and byte compile
%py3_shebang_fix %{buildroot}%{_datadir}/%{name}/plugin_launchers/
%py3_shebang_fix %{buildroot}%{_datadir}/%{name}/python3lib/
%py_byte_compile %{python3} %{buildroot}%{_datadir}/%{name}/plugin_launchers/
%py_byte_compile %{python3} %{buildroot}%{_datadir}/%{name}/python3lib/

# desktop-file and appdata
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

mkdir -p %{buildroot}%{_datadir}/appdata
install -p -m 644 %{SOURCE1} %{buildroot}%{_datadir}/appdata

appstream-util validate-relax --nonet \
  %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml

%files
%doc ChangeLog.txt README.md
%license COPYING.txt
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_datadir}/%{name}/
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/*/apps/%{name}.svg

%files doc
%doc docs/*.epub

%changelog
%autochangelog
