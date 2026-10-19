%global source1_hash ce383c5c3460826de31fdc9824dbffef25860866ee917031207a595967ff559d
%global source0_hash 8ff0e0cae3ddead0bd92bbd2b396d62490336aa52fb5a6c81cf1f07eba3fdc3e
%global appid com.github.johnfactotum.Foliate
%global libadwaita_version 1.7
%global webkitgtk_version 2.40.1
%global commit1 052123beafed921a9a2a45ef6330c235289a634e
%global shortcommit1 %(c=%{commit1}; echo ${c:0:7})
Name:           foliate
Version:        3.3.0
Release:        1%{?dist}
Summary:        Simple and modern GTK eBook reader
License:        GPL-3.0-or-later
URL:            https://johnfactotum.github.io/foliate/
Source0:        https://github.com/johnfactotum/foliate/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/johnfactotum/foliate-js/archive/%{commit1}/%{name}-js-%{shortcommit1}.tar.gz
BuildArch:      noarch
Requires:       gjs >= 1.76
Requires:       hicolor-icon-theme
Requires:       libadwaita >= %{libadwaita_version}
Requires:       webkitgtk6.0 >= %{webkitgtk_version}
Recommends:     espeak-ng
Recommends:     python3 >= 3.4
Suggests:       espeak
Suggests:       festival
Provides:       bundled(%{name}-js) = 0~git%{shortcommit1}
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(gjs-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(iso-codes)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(webkitgtk-6.0)
# /oreon:deps
%description
A simple and modern GTK eBook viewer, built with GJS and Epub.js.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
%autosetup -p1 -a1
mv %{name}-js-%{commit1}/* src/%{name}-js

%build

%meson
%meson_build
%install
%meson_install
%find_lang %{appid}
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
%dnl desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
