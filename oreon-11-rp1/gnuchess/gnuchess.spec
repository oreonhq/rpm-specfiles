%global source0_hash 0b37bec2098c2ad695b7443e5d7944dc6dc8284f8d01fcc30bdb94dd033ca23a
Summary:        The GNU chess program
Name: gnuchess
Version: 6.3.0
Release:        2%{?dist}
License: GPL-3.0-or-later
URL: https://www.gnu.org/software/chess/
Source0:        http://ftp.gnu.org/pub/gnu/chess/%{name}-%{version}.tar.gz
Source1: book_1.02.dat.gz
Provides: chessprogram
# oreon:deps
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  help2man
BuildRequires:  make
# /oreon:deps
%description
The gnuchess package contains the GNU chess program.  By default,
GNU chess uses a curses text-based interface.  Alternatively, GNU chess
can be used in conjunction with the xboard user interface and the X
Window System for play using a graphical chess board.

Install the gnuchess package if you would like to play chess on your
computer.  If you'd like to use a graphical interface with GNU chess,
you'll also need to install the xboard package and the X Window System.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}
gzip -dc %{SOURCE1} > book.dat

%build

%configure
%make_build
%install
mkdir -p $RPM_BUILD_ROOT%{_var}/lib/games/gnuchess $RPM_BUILD_ROOT%{_bindir}
install -m 755 -p src/gnuchess $RPM_BUILD_ROOT%{_bindir}
install -m 644 -p book.dat $RPM_BUILD_ROOT%{_var}/lib/games/gnuchess
mkdir -p $RPM_BUILD_ROOT%{_datadir}/gnuchess/
install -m 644 doc/gnuchess.ini $RPM_BUILD_ROOT%{_datadir}/gnuchess/
%make_install
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
