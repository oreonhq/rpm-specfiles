# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 66d511b9e6e334c0e62279eb234fbfb2b3110b1479c09b95b44c7afca8cff9e7
%global source1_hash 9264d3673cc1c633f77ab1469627864836e6500cb9b3823c571dcb1c10ba13cb

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
# configuration on the builders
%bcond tests 1

Name:           libuv
Epoch:          1
Version:        1.52.1
Release:        1%{?dist}
Summary:        Platform layer for node.js

# Code is MIT
# Documentation is CC-BY-4.0
# src/inet.c is ISC
# include/uv/tree.h is BSD-2-Clause
License:        MIT AND CC-BY-4.0 AND ISC AND BSD-2-Clause
URL:            http://libuv.org/
Source0:        http://dist.libuv.org/dist/v%{version}/libuv-v%{version}.tar.gz
Source1:        https://dist.libuv.org/dist/v%{version}/libuv-v%{version}.tar.gz.sign
# mkdir temp
# gpg --no-default-keyring --keyring temp/keyring.gpg --keyserver keyserver.ubuntu.com \
#  --recv-keys D77B1E34243FBAF05F8E9CC34F55C8C846AB89B9  \
#  FDF519364458319FA8233DC9410E5553AE9BC059 94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \
#  57353E0DBDAAA7E839B66A1AFF47D5E4AD8B4FDC AEAD0A4B686767751A0E4AEF34A25FB128246514 \
#  CFBB9CA9A5BEAFD70E2B3C5A79A67C55A3679C8B C82FA3AE1CBEDC6BE46B9360C43CEC45C17AB93C \
#  612F0EAD9401622379DF4402F28C3C8DA33C03BE \
#  && gpg --no-default-keyring --keyring temp/keyring.gpg --output temp/keysuv.gpg --export
# cp temp/keysuv.gpg .
Source2:        keysuv.gpg
Source3:        libuv.abignore
Source10:       https://files.pythonhosted.org/packages/source/m/markupsafe/markupsafe-3.0.4.tar.gz
Patch0:         libuv-udp-reuseport-burst.patch

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gnupg2
# Documentation
BuildRequires:  make
BuildRequires:  python3-sphinx
BuildRequires:  python3-markupsafe
BuildRequires:  oreon-rpm-macros


%description
libuv is a new platform layer for Node. Its purpose is to abstract IOCP on
Windows and libev on Unix systems. We intend to eventually contain all platform
differences in this library.

%package devel
Summary:        Development libraries for libuv
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       %{name}-static%{?_isa} = %{epoch}:%{version}-%{release}


%description devel
Development libraries for libuv

%package static
Summary:        Platform layer for node.js - static library
Requires:       %{name}-devel%{?_isa} = %{epoch}:%{version}-%{release}

%description static
Static library (.a) version of libuv.


%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -

gpgv2 --keyring %{SOURCE2} %{SOURCE1} %{SOURCE0}
%autosetup -n %{name}-v%{version} -p1

%build
%if %{with tests}
%cmake -DBUILD_TESTING=ON
%else
%cmake -DBUILD_TESTING=OFF
%endif
%cmake_build
# Build Documentation
echo '2e9ad7dd851bf45fab9f75cbff4cb493fee9979e8d8c7c9c3ee119022518edd6  %{SOURCE10}' | sha256sum -c -
tar -xzf %{SOURCE10} -C %{_builddir}
export PYTHONPATH="%{_builddir}/markupsafe-3.0.4/src${PYTHONPATH:+:$PYTHONPATH}"
cd docs
make man
cd ..

%install
%cmake_install
# install documentation
mkdir -p  %{buildroot}/%{_mandir}/man1/
install -p -m 644 docs/build/man/libuv.1 %{buildroot}/%{_mandir}/man1/
mkdir -p %{buildroot}%{_libdir}/libuv/
install -Dm0644 -t %{buildroot}%{_libdir}/libuv/ %{SOURCE3}
# Remove packaged license files
rm %{buildroot}/%{_docdir}/libuv/LICENSE
rm %{buildroot}/%{_docdir}/libuv/LICENSE-extra


%check
%if %{with tests}
env UV_TEST_TIMEOUT_MULTIPLIER=10 ./%{__cmake_builddir}/uv_run_tests
env UV_TEST_TIMEOUT_MULTIPLIER=10 ./%{__cmake_builddir}/uv_run_tests_a
%endif


%files
%doc README.md AUTHORS CONTRIBUTING.md MAINTAINERS.md SUPPORTED_PLATFORMS.md
%doc ChangeLog
%license LICENSE LICENSE-docs LICENSE-extra
%{_libdir}/%{name}.so.1
%{_libdir}/%{name}.so.1.*
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/libuv.abignore
%{_mandir}/man1/%{name}.1*

%files devel
%{_includedir}/uv.h
%dir %{_includedir}/uv
%{_includedir}/uv/*.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%dir %{_libdir}/cmake/%{name}
%{_libdir}/cmake/%{name}/*.cmake

%files static
%{_libdir}/%{name}.a
%{_libdir}/pkgconfig/%{name}-static.pc

