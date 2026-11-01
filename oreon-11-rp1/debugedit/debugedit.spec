%global source0_hash 3b8c6396fe235e0270c9b9c0d244cfd0e86c284fc27e820acc58360e7cfa08c2
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: debugedit
Version: 5.3
Release: 1%{?dist}
Summary: Tools for altering debuginfo and creating debug source packages
License: GPL-3.0-or-later AND GPL-2.0-or-later AND LGPL-2.0-or-later
URL: https://sourceware.org/debugedit/
Source0: https://sourceware.org/pub/debugedit/%{version}/debugedit-%{version}.tar.xz
Source1: debugedit-%{version}.tar.xz.sig
Source2: debugedit-key.gpg
Patch0: debugedit-5.3-elflint-test.patch

Requires: dwz
Requires: elfutils
Requires: binutils
Requires: xz

BuildRequires: oreon-rpm-macros
BuildRequires: gnupg2
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: make
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: help2man
BuildRequires: pkgconfig(libelf)
BuildRequires: pkgconfig(libdw)
BuildRequires: xxhash-devel
BuildRequires: dwz
%endif

%description
debugedit rewrites debug paths and find-debuginfo builds separate debuginfo.

%prep
%oreon_sha256
%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}
%autosetup -p1
autoreconf -fi

%build
%oreon_configure
%oreon_make

%install
%oreon_make_install
ln -s find-debuginfo %{buildroot}%{_bindir}/find-debuginfo.sh
%oreon_filelist

%files -f %{_builddir}/%{name}.files
%license COPYING COPYING3 COPYING.LIB
