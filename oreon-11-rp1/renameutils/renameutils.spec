%global source0_hash cbd2f002027ccf5a923135c3f529c6d17fabbca7d85506a394ca37694a9eb4a3

Name:           renameutils
Version:        0.12.0
Release:        31%{?dist}
Summary:        A set of programs to make renaming and copying of files easier

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://www.nongnu.org/renameutils
Source0:        http://savannah.nongnu.org/download/%{name}/%{name}-%{version}.tar.gz
Patch0:         renameutils-0.12.0-install-typo.patch
# Based on patch from Debian. Also updates declarations.
# https://salsa.debian.org/debian/renameutils/-/blob/8d33a6d7ad3eafe997c8dcff5a17493e7f698a36/debian/patches/gcc15-fixes.patch
Patch1:         renameutils-0.12.0-gcc15-fixes.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  readline-devel
BuildRequires:  gettext
# Bundled library exception: https://fedorahosted.org/fpc/ticket/174
Provides:       bundled(gnulib) = 20120423

%description
The file renaming utilities (renameutils for short) are a set of
programs designed to make renaming of files faster and less
cumbersome.

The file renaming utilities consists of five programs - qmv, qcp, imv,
icp and deurlname.

The qmv ("quick move") program allows file names to be edited in a
text editor. The names of all files in a directory are written to a
text file, which is then edited by the user. The text file is read and
parsed, and the changes are applied to the files.

The qcp ("quick cp") program works like qmv, but copies files instead
of moving them.

The imv ("interactive move") program, is trivial but useful when you
are too lazy to type (or even complete) the name of the file to rename
twice. It allows a file name to be edited in the terminal using the
GNU Readline library. icp copies files.

The deurlname program removes URL encoded characters (such as %20
representing space) from file names. Some programs such as w3m tend to
keep those characters encoded in saved files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .install-typo
%patch -P1 -p1 -b .gcc15-fixes

%build
%configure
make %{?_smp_mflags}

%install
%make_install INSTALL="install -p"
%find_lang %{name}
%find_lang %{name}-gnulib

%files -f %{name}.lang -f %{name}-gnulib.lang
%doc README TODO COPYING NEWS AUTHORS
%{_bindir}/*
%{_mandir}/man1/*

%changelog
%autochangelog
