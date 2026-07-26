%global source0_hash da68d7a65f44dcf6ce6e4e630b6f6dd9897249d34425920bfdd4e07ff1866a72

# workaround for GCC 10. upstream is inactive,
# delaying fixing the code itself.
%define _legacy_common_support 1
%define _gcc_lto_cflags %{nil}

Name:           gnugo
Version:        3.8
Release:        38%{?dist}

Summary:        Text based go program

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://www.gnu.org/software/gnugo/gnugo.html
Source0:        http://ftp.gnu.org/gnu/gnugo/gnugo-%{version}.tar.gz
Patch0:         gnugo-3.8-format-security.patch

BuildRequires:  gcc
BuildRequires:  ncurses-devel readline-devel
BuildRequires:  texinfo
BuildRequires: make

%description
This software is a free program that plays the game of Go. GNU Go has played
thousands of games on the NNGS Go server. GNU Go is now also playing regularly
on the Legend Go Server in Taiwan and the WING server in Japan.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# convert docs to UTF-8
for f in AUTHORS THANKS; do
  iconv -f iso8859-1 -t utf-8 $f > $f.conv
  touch -r $f $f.conv
  mv $f.conv $f
done

%build
%configure --enable-color --with-readline
%make_build

%install
%make_install
rm -f ${RPM_BUILD_ROOT}/%{_infodir}/dir

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README TODO THANKS doc/newlogo.jpg doc/oldlogo.jpg
%doc %{_mandir}/man6/*
%{_bindir}/*
%{_infodir}/gnugo.*

%changelog
%autochangelog
