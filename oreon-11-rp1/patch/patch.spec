%global source0_hash f87cee69eec2b4fcbf60a396b030ad6aa3415f192aa5f7ee84cad5e11f7f5ae3
%global gnulib_ver 20180203
Summary:        Utility for modifying/upgrading files
Name: patch
Version: 2.8
Release:        1%{?dist}
License: GPL-3.0-or-later
URL: https://savannah.gnu.org/projects/patch/
Source0:        https://mirrors.kernel.org/gnu/patch/patch-%{version}.tar.xz
Requires: ed
Provides: bundled(gnulib) = %{gnulib_ver}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  ed
BuildRequires:  gcc
BuildRequires:  libattr-devel
BuildRequires:  libselinux-devel
BuildRequires:  make
# /oreon:deps
%description
The patch program applies diff files to originals.  The diff command
is used to compare an original to a changed file.  Diff lists the
changes made to the file.  A person who has the original file can then
use the patch command with the diff file to add the changes to their
original file (patching the file).

Patch should be installed because it is a common way of upgrading
applications.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf
%configure --disable-silent-rules
%make_build
%check

make check
%install
%makeinstall
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.8-4
- Prepare for Oreon 11 (RP1)
