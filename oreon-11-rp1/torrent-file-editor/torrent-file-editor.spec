%global source0_hash adbc8eda5105c8dd6a2b231165c5446fc062b566272b40493a4dcd0bfc511e5b

%define cid io.github.torrent_file_editor.Torrent-file-editor

Name:           torrent-file-editor
Version:        1.0.2
Release:        2%{?dist}
Summary:        Edit and create torrent files

# Most code licensed with GPL3+
# json-builder/json-parser licensed as BSD2
License:        GPL-3.0-or-later AND BSD-2-Clause
URL:            https://torrent-file-editor.github.io
Source0:        https://github.com/%{name}/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Patch1:         0001-unsupported-appstream-tags.patch

BuildRequires:  cmake
%if (0%{?fedora} >= 40 || 0%{?rhel} >= 10)
# BuildRequires:  pkgconfig(xcb-xkb)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  qt6-qttools-devel
%else
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  qt5-qttools-devel
%endif
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

# Package puts icons to hicolor-icon-theme folders
Requires:       hicolor-icon-theme

%description
A tool designed to create and edit torrent files. It shows the full contents of a
torrent files or any bencode file and allows changing any fields.

The main features:

  - Create torrent files from scratch
  - Edit torrent files in a user-friendly way
  - Edit torrent files in JSON format
  - Add, remove and reorder files in a torrent
  - Support for multiple encodings

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%if (0%{?rhel} > 0 && 0%{?rhel} <= 9)
%patch -P1 -p1
%endif

%build
%cmake -DDISABLE_DONATION=ON
%cmake_build

%install
%cmake_install

%check
# Menu file is being installed when make install
# so it need only to check this allready installed file
desktop-file-validate %{buildroot}%{_datadir}/applications/%{cid}.desktop

# Check AppData file
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{cid}.metainfo.xml

%files
%doc README.md
%license LICENSES/GPL-3.0-or-later.txt LICENSES/BSD-2-Clause
%{_bindir}/%{name}
%{_datadir}/applications/%{cid}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{cid}.svg
%{_datadir}/icons/hicolor/*/apps/%{cid}.png
%{_metainfodir}/%{cid}.metainfo.xml

%changelog
%autochangelog
