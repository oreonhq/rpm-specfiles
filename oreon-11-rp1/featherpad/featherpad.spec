%global source0_hash 1442f14aefdb0de26822562d69c446b0e2b4e607597925a2e0c2c7b063e1654e
%global github_name FeatherPad
Name:           featherpad
Version:        1.6.4
Release:        1%{?dist}
Summary:        Lightweight Qt Plain-Text Editor
License:        GPL-3.0-or-later
URL:            https://github.com/tsujan/%{github_name}
Source0:        https://github.com/tsujan/%{github_name}/archive/V%{version}.tar.gz#/%{github_name}-%{version}.tar.xz
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(hunspell)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xext)
# /oreon:deps
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
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
