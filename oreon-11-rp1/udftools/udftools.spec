%global source0_hash 750dcf5c797765eb42265e0a56d1a99f97f94b7f6f4534263a5410503f0caf59
Summary:        Linux UDF Filesystem userspace utilities
Name: udftools
Version: 2.3
Release:        1%{?dist}
License: GPL-2.0-or-later
URL: http://sourceforge.net/projects/linux-udf/
Source0:        https://github.com/pali/udftools/releases/download/%{version}/udftools-%{version}.tar.gz
Patch1: udftools-2.3-backported_fixes.patch
Requires: udev
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  perl-Carp
BuildRequires:  readline-devel
BuildRequires:  udev
# /oreon:deps
%description
Linux UDF Filesystem userspace utilities.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure
%make_build
%install
%make_install
rm -rf %{buildroot}%{_bindir}/udffsck
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.3-13
- Prepare for Oreon 11 (RP1)
