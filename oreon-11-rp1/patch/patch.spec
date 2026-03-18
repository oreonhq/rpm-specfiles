%global gnulib_ver 20180203

Summary: Utility for modifying/upgrading files
Name: patch
Version: 2.8
Release: 4%{?dist}
License: GPL-3.0-or-later
URL: https://savannah.gnu.org/projects/patch/
Source: https://ftp.gnu.org/gnu/patch/patch-%{version}.tar.xz
BuildRequires: make
BuildRequires: gcc
BuildRequires: libselinux-devel
BuildRequires: libattr-devel
BuildRequires: ed
BuildRequires: autoconf automake

Requires: ed

Provides: bundled(gnulib) = %{gnulib_ver}

%description
The patch program applies diff files to originals.  The diff command
is used to compare an original to a changed file.  Diff lists the
changes made to the file.  A person who has the original file can then
use the patch command with the diff file to add the changes to their
original file (patching the file).

Patch should be installed because it is a common way of upgrading
applications.

%prep
%autosetup -p1

%build
autoreconf
%configure --disable-silent-rules
%make_build

%check
make check

%install
%makeinstall

%files
%license COPYING
%doc NEWS README
%{_bindir}/*
%{_mandir}/*/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.8-4
- Prepare for Oreon 11 (RP1)
