%global source0_hash adbc8eda5105c8dd6a2b231165c5446fc062b566272b40493a4dcd0bfc511e5b
%define cid io.github.torrent_file_editor.Torrent-file-editor
Name:           torrent-file-editor
Version:        1.0.2
Release:        1%{?dist}
Summary:        Edit and create torrent files
License:        GPL-3.0-or-later AND BSD-2-Clause
URL:            https://torrent-file-editor.github.io
Source0:        https://github.com/%{name}/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Patch1:         0001-unsupported-appstream-tags.patch
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  qt5-qttools-devel
# /oreon:deps
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

%build

%cmake -DDISABLE_DONATION=ON
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/%{cid}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{cid}.metainfo.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
