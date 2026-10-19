%global source0_hash ddc89da86595d272282ae8726cc7913867b9517eec6e765e66e6da860b58e2f9
Name:           ncmpcpp
Version:        0.10.1
Release:        1%{?dist}
Summary:        Featureful ncurses based MPD client inspired by ncmpc
License:        GPL-2.0-or-later
URL:            http://ncmpcpp.rybczak.net/
Source0:        https://github.com/%{name}/%{name}/archive/refs/tags/%{version}.tar.gz
Patch0:         ncmpcpp-0.10.1-boost_m4-bash53.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  boost-devel
BuildRequires:  curl-devel
BuildRequires:  fftw-devel
BuildRequires:  gcc-c++
BuildRequires:  libmpdclient-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  readline-devel
BuildRequires:  taglib-devel
# /oreon:deps
%description
A featureful ncurses based MPD client inspired by ncmpc. The main features are:

- tag editor
- playlist editor
- easy to use search engine
- media library
- music visualizer
- ability to fetch artist info from last.fm
- new display mode
- alternative user interface
- ability to browse and add files from outside of MPD music directory

.. and a lot more minor functions.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
autoreconf -fiv

%build

BOOST_LIB_SUFFIX=""; export BOOST_LIB_SUFFIX ;
%configure --disable-static --enable-clock --with-taglib --with-fftw --enable-visualizer --enable-outputs
%make_build
%install
%make_install
rm -f %{buildroot}/%{_docdir}/%{name}/COPYING
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
