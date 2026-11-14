# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 91204cd32f164bd3b7c992d4a6a8ce6519511aadab30f78b6982d0bf8d73e931

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Summary: C library for multiple precision complex arithmetic
Name: libmpc
Version: 1.4.1
Release: 1%{?dist}
License: LGPL-3.0-or-later AND FSFAP
URL: https://www.multiprecision.org/mpc/
Source0: https://ftp.gnu.org/gnu/mpc/mpc-%{version}.tar.xz
Source1: mpc-1.4.1.tar.xz.sig
Source2: enge.gpg

# BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: gmp-devel >= 5.0.0
BuildRequires: mpfr-devel >= 4.1.0
BuildRequires: make

Obsoletes: compat-libmpc < %{version}-1
Provides: compat-libmpc = %{version}-%{release}

%description
MPC is a C library for the arithmetic of complex numbers with arbitrarily high
precision and correct rounding of the result. It is built upon and follows
the same principles as Mpfr.

%package devel
Summary: Headers and shared development libraries for MPC
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: gmp-devel%{?_isa}
Requires: mpfr-devel%{?_isa}
Obsoletes: mpc-devel < %{version}-2

%description devel
Header files and shared library symlinks for the MPC library.

%package doc
Summary: Documentation for the MPC library
License: GFDL-1.3-no-invariants-or-later
BuildArch: noarch

%description doc
Documentation for the MPC library.

%prep
%oreon_sha256
%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}
%autosetup -n mpc-%{version}

%build
%configure --disable-static
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool
%make_build

%install
%make_install
rm -f %{buildroot}%{_infodir}/dir
rm -f %{buildroot}%{_libdir}/*.la

%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
%make_build check

%files
%license COPYING.LESSER
%doc AUTHORS NEWS README
%{_libdir}/libmpc.so.3{,.*}

%files devel
%{_libdir}/libmpc.so
%{_libdir}/pkgconfig/mpc.pc
%{_includedir}/mpc.h

%files doc
%doc AUTHORS
%{_infodir}/*.info*
