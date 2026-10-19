%global source0_hash ac797e9505015068702fd7e20c0be27572af3a8dbbff8df9845c283daf97e8d8
%global commit1         0daa58349ab3373161a4a73c1ccd2822328d2c73
%global shortcommit1    %(c=%{commit1}; echo ${c:0:7})
%global commit2         a8b9e682ba65ca4a6d805c8be97c5232bae3c0c1
%global shortcommit2    %(c=%{commit2}; echo ${c:0:7})
%global url1    https://github.com/%{name}
Name:           polybar
Version:        3.7.2
Release:        1%{?dist}
Summary:        Fast and easy-to-use status bar
License:        LicenseRef-Callaway-MIT AND LicenseRef-Callaway-BSD
URL:            https://polybar.github.io/
Source0:        %{url1}/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        %{url1}/i3ipcpp/archive/%{commit1}/i3ipcpp-%{shortcommit1}.tar.gz
Source2:        %{url1}/xpp/archive/%{commit2}/xpp-%{shortcommit2}.tar.gz
Patch0:         0000-include-cstdint.patch
Patch1:         0001-link-freetype.patch
Provides:       bundled(i3ipcpp) = 0.7.1~git%{shortcommit1}
Provides:       bundled(xpp) = 1.4.0~git%{shortcommit2}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  i3-devel
BuildRequires:  libmpdclient-devel
BuildRequires:  libnl3-devel
BuildRequires:  make
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(jsoncpp)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libuv)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-proto)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  python3
BuildRequires:  python3-sphinx
BuildRequires:  xcb-util-cursor-devel
BuildRequires:  xcb-util-image-devel
BuildRequires:  xcb-util-wm-devel
BuildRequires:  xcb-util-xrm-devel
# /oreon:deps
%description
Polybar aims to help users build beautiful and highly customizable status bars
for their desktop environment, without the need of having a black belt in shell
scripting.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%setup -q -D -T -a1
%setup -q -D -T -a2

mv i3ipcpp-%{commit1}/* lib/i3ipcpp
mv xpp-%{commit2}/*     lib/xpp

%autopatch -p1

%build

%cmake
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
