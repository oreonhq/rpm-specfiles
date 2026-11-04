%global source0_hash f87cee69eec2b4fcbf60a396b030ad6aa3415f192aa5f7ee84cad5e11f7f5ae3

%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global gnulib_ver 20180203

Summary: Utility for modifying/upgrading files
Name: patch
Version:        2.8
Release:        1%{?dist}
License: GPL-3.0-or-later
URL: https://savannah.gnu.org/projects/patch/
Source0:        https://mirrors.kernel.org/gnu/patch/patch-%{version}.tar.xz
Patch:        0008-patch:Absolute-in-tree-symlink-target-resolved-relative-to-symlink-parent.patch
Patch:        0008-patch:Absolute-in-tree-symlink-target-resolved-relative-to-symlink-parent.patch
Patch:        0008-patch:Absolute-in-tree-symlink-target-resolved-relative-to-symlink-parent.patch
Patch:        0008-patch:Absolute-in-tree-symlink-target-resolved-relative-to-symlink-parent.patch
Patch:        0008-patch:Absolute-in-tree-symlink-target-resolved-relative-to-symlink-parent.patch
Patch:        0008-patch:Absolute-in-tree-symlink-target-resolved-relative-to-symlink-parent.patch
Patch:        0008-patch:Absolute-in-tree-symlink-target-resolved-relative-to-symlink-parent.patch
Patch:        0008-patch:Absolute-in-tree-symlink-target-resolved-relative-to-symlink-parent.patch

BuildRequires: make
BuildRequires: gcc
BuildRequires: libselinux-devel
BuildRequires: libattr-devel
BuildRequires: ed
BuildRequires: autoconf automake
BuildRequires:  oreon-rpm-macros

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
%oreon_sha256

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

