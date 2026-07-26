%global source0_hash ddc89da86595d272282ae8726cc7913867b9517eec6e765e66e6da860b58e2f9

Name:           ncmpcpp
Version:        0.10.1
Release:        9%{?dist}
Summary:        Featureful ncurses based MPD client inspired by ncmpc
License:        GPL-2.0-or-later
URL:            http://ncmpcpp.rybczak.net/
Source0:        https://github.com/%{name}/%{name}/archive/refs/tags/%{version}.tar.gz
# bash 5.3 treats cd with null directory as error as specified in POSIX.1-2024
# https://www.austingroupbugs.net/view.php?id=1047
# https://cgit.git.savannah.gnu.org/cgit/bash.git/commit/?h=devel&id=136cdf8108f2d6c6dd9710c544b1b7b6bd790617
Patch0:         ncmpcpp-0.10.1-boost_m4-bash53.patch

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  curl-devel
BuildRequires:  taglib-devel
BuildRequires:  ncurses-devel
BuildRequires:  libmpdclient-devel
BuildRequires:  boost-devel
BuildRequires:  fftw-devel
BuildRequires:  readline-devel
BuildRequires:  autoconf automake libtool

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

# Remove dupe
rm -f %{buildroot}/%{_docdir}/%{name}/COPYING

%files
%doc doc/config doc/bindings AUTHORS CHANGELOG.md README.md
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*

%changelog
%autochangelog
