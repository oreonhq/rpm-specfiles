%global source0_hash 105a72d51c7fbcc690c9b9a850f3743accbd9bf5dc51480b5ea283dfde96d61e
%global minor_version 0.6
%global thunar_version 4.18
%global xfceversion 4.18
Name:           thunar-media-tags-plugin
Version:        0.6.0
Release:        1%{?dist}
Summary:        Media Tags plugin for the Thunar file manager
License:        GPL-2.0-or-later
URL:            http://goodies.xfce.org/projects/thunar-plugins/%{name}
Source0:        http://archive.xfce.org/src/thunar-plugins/%{name}/%{minor_version}/%{name}-%{version}.tar.bz2
Requires:       Thunar >= %{thunar_version}
# oreon:deps
BuildRequires:  Thunar-devel
BuildRequires:  exo
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  libxfce4util-devel
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  taglib-devel
# /oreon:deps
%description
This plugin adds special features for media files to the Thunar file manager.
It includes a special media file page for the file properties dialog, a tag 
editor for ID3 or OGG/Vorbis tags and a so-called bulk renamer, which allows 
users to rename multiple audio files at once, based on their tags.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%configure
%make_build
%install
%make_install
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
