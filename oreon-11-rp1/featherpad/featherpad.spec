%global source0_hash 9753796b2a525a4d6b13696681e9fbb094edcc20e8aadffcd5bb6fe22d0a5fdb

%global github_name FeatherPad

Name:           featherpad
Version:        1.6.2
Release:        3%{?dist}
Summary:        Lightweight Qt Plain-Text Editor

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/tsujan/%{github_name}
Source0:        %{url}/archive/V%{version}.tar.gz#/%{github_name}-%{version}.tar.xz

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(hunspell) >= 1.6
BuildRequires:  pkgconfig(xext)

Requires:       hicolor-icon-theme

%description
FeatherPad is a lightweight Qt plain-text editor for Linux. It is independent
of any desktop environment and has:

* Drag-and-drop support, including tab detachment and attachment;
* X11 virtual desktop awareness (using tabs on current desktop but opening a
  new window on another);
* An optionally permanent search-bar with a different search entry
  for each tab;
* Instant highlighting of found matches when searching;
* A docked window for text replacement;
* Support for showing line numbers and jumping to a specific line;
* Automatic detection of text encoding as far as possible and optional saving
  with encoding;
* Syntax highlighting for common programming languages;
* Printing;
* Text zooming;
* Appropriate but non-interrupting prompts;

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{github_name}-%{version} -p 1

%build
%cmake
%cmake_build

%install
%cmake_install
%find_lang %{name} --with-qt

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files -f %{name}.lang
%license COPYING
%doc ChangeLog INSTALL NEWS README.md
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/help
%dir %{_datadir}/%{name}/translations
%{_datadir}/metainfo/featherpad.metainfo.xml

%changelog
%autochangelog
