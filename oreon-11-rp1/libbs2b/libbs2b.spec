# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash b97164dd98fda4b05722fd68ffed2427b980dfb8316bbbbcfc0cde3ae5238cd5
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:		libbs2b
Version:	3.1.0
Release:	1%{?dist}
Summary:	Bauer stereophonic-to-binaural DSP library

License:	MIT
URL:		http://bs2b.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/bs2b/libbs2b/%{version}/%{name}-%{version}.tar.lzma
Patch0:		libbs2b-security.patch
Patch1:		libbs2b-dont-clip-samples.patch

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc-c++
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libsndfile-devel
BuildRequires:	make

%package devel
Summary:	Development files for libbs2b
Requires:	%{name} = %{version}-%{release}
Requires:	pkgconfig

%description
The Bauer stereophonic-to-binaural DSP (bs2b) library and plugins is designed
to improve headphone listening of stereo audio records. Recommended for
headphone prolonged listening to disable superstereo fatigue without essential
distortions.

%description devel
This package contains the development files for the Bauer
stereophonic-to-binaural (bs2b) DSP effect library.

%prep
%oreon_sha256
%autosetup -p1

sed -i -e 's/lzma/xz/g' configure.ac
autoreconf -vif

%build
%configure --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build

%install
make install DESTDIR=%{buildroot}
rm %{buildroot}/%{_libdir}/%{name}.la

%files
%doc AUTHORS ChangeLog README
%license COPYING
%{_bindir}/*
%{_libdir}/%{name}.so.*

%files devel
%{_includedir}/*
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%ldconfig_scriptlets

%changelog
%autochangelog
