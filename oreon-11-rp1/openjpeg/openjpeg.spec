# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash a695fbe19c0165f295a8531b1e4e855cd94d0875d2f88ec4b61080677e27188a

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global api_version 2.5

Name:           openjpeg
Version:        2.5.4
Release:        1%{?dist}
Summary:        JPEG 2000 codec library
License:        BSD-2-Clause AND MIT AND BSD-3-Clause
URL:            https://www.openjpeg.org/
Source0:        https://github.com/uclouvain/openjpeg/archive/v%{version}/openjpeg-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  lcms2-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  make
BuildRequires:  oreon-rpm-macros
BuildRequires:  zlib-devel

Provides:       openjpeg2 = %{version}-%{release}
Provides:       openjpeg2%{?_isa} = %{version}-%{release}

%description
OpenJPEG is an open-source JPEG 2000 codec written in C. It has been
developed in order to promote the use of JPEG 2000, a still-image compression
standard from the Joint Photographic Experts Group (JPEG).

%package        devel
Summary:        Development files for OpenJPEG
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig
Provides:       openjpeg2-devel = %{version}-%{release}
Provides:       openjpeg2-devel%{?_isa} = %{version}-%{release}

%description    devel
The development files for the OpenJPEG JPEG 2000 library.

%package        tools
Summary:        OpenJPEG command line tools
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       openjpeg2-tools = %{version}-%{release}
Provides:       openjpeg2-tools%{?_isa} = %{version}-%{release}

%description    tools
Command line tools to compress, decompress and dump JPEG 2000 images.

%package        doc
Summary:        OpenJPEG API documentation
BuildArch:      noarch

%description    doc
The HTML API documentation of the OpenJPEG library.

%prep
%oreon_sha256
%autosetup

%build
%cmake \
        -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_DOCDIR=%{_docdir}/openjpeg-doc \
        -DBUILD_STATIC_LIBS=OFF \
        -DBUILD_DOC=ON \
        -DBUILD_UNIT_TESTS=ON \
        -DBUILD_THIRDPARTY=OFF
%cmake_build

%install
%cmake_install

%check
%{_vpath_builddir}/bin/test_sparse_array

mkdir roundtrip
cd roundtrip
printf 'P6\n16 16\n255\n' > in.ppm
head -c 768 /dev/urandom >> in.ppm
LD_LIBRARY_PATH=%{buildroot}%{_libdir}:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH
%{buildroot}%{_bindir}/opj_compress -i in.ppm -o out.j2k
%{buildroot}%{_bindir}/opj_decompress -i out.j2k -o out.ppm
cmp in.ppm out.ppm
%{buildroot}%{_bindir}/opj_dump -i out.j2k | grep -q 'numcomps=3'

%ldconfig_scriptlets

%files
%license LICENSE
%doc AUTHORS.md CHANGELOG.md NEWS.md README.md THANKS.md
%{_libdir}/libopenjp2.so.7*
%{_libdir}/libopenjp2.so.%{version}

%files devel
%{_includedir}/openjpeg-%{api_version}
%{_libdir}/libopenjp2.so
%{_libdir}/cmake/openjpeg-%{api_version}
%{_libdir}/pkgconfig/libopenjp2.pc
%{_mandir}/man3/libopenjp2.3*

%files tools
%{_bindir}/opj_compress
%{_bindir}/opj_decompress
%{_bindir}/opj_dump
%{_mandir}/man1/opj_compress.1*
%{_mandir}/man1/opj_decompress.1*
%{_mandir}/man1/opj_dump.1*

%files doc
%{_docdir}/openjpeg-doc

%changelog
%autochangelog
