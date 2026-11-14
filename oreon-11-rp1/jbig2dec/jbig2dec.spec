# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 7b63ff6470289547e7a3a0f145cb8ea6c2afffdd65645b7d87d3b7febc96fb3a

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           jbig2dec
Version:        0.20
Release:        1%{?dist}
Summary:        A decoder implementation of the JBIG2 image compression format
License:        AGPL-3.0-or-later
URL:            https://jbig2dec.com/
Source0:        https://github.com/ArtifexSoftware/jbig2dec/releases/download/%{version}/jbig2dec-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  libpng-devel
BuildRequires:  make
BuildRequires:  oreon-rpm-macros

%description
jbig2dec is a decoder library and example utility implementing the JBIG2
bi-level image compression spec. Also known as ITU T.88 and ISO IEC 14492,
and included by reference in Adobe's PDF version 1.4 and later.

%package        libs
Summary:        Library for decoding JBIG2 images

%description    libs
The jbig2dec shared library for decoding JBIG2 images.

%package        devel
Summary:        Development files for the jbig2dec library
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
Header files and the shared library link for developing applications that
use the jbig2dec library.

%prep
%oreon_sha256
%autosetup

%build
%configure --disable-static
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -delete -print

%check
%make_build check

%ldconfig_scriptlets libs

%files
%license COPYING
%doc CHANGES README
%{_bindir}/jbig2dec
%{_mandir}/man1/jbig2dec.1*

%files libs
%license COPYING
%{_libdir}/libjbig2dec.so.0*

%files devel
%{_includedir}/jbig2.h
%{_libdir}/libjbig2dec.so
%{_libdir}/pkgconfig/jbig2dec.pc

%changelog
%autochangelog
