# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash c739578bf6b764aa0752db9a2fdadcfe921c78f1228c7ec0bb47fa804c55d17b

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
Version:        2.14

Name:		jansson
Release:        1%{?dist}
Summary:	C library for encoding, decoding and manipulating JSON data

License:	MIT AND LicenseRef-Oreon-Public-Domain
URL:		https://github.com/akheron/jansson
Source0:        https://github.com/akheron/jansson/archive/v%{version}/jansson-%{version}.tar.gz
Source10:       https://files.pythonhosted.org/packages/source/m/markupsafe/markupsafe-3.0.4.tar.gz

# Fix the tests.
# Upstream commit 0677666f65b988b2dd44d02966a08fea490d5883
Patch:        0001-Fix-the-check-exports-tests-for-versioned-symbols.patch

BuildRequires:	gcc
BuildRequires:	python3-sphinx
BuildRequires:	python3-markupsafe
BuildRequires:  make
BuildRequires:  autoconf, automake, libtool
BuildRequires:  oreon-rpm-macros

%description
Small library for parsing and writing JSON documents.

%package devel
Summary: Header files for jansson
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files for developing applications making use of jansson.

%package devel-doc
Summary: Development documentation for jansson
BuildArch: noarch

%description devel-doc
Development documentation for jansson.

%prep
%oreon_sha256

%autosetup -p1 -n jansson-%{version}


%build
autoreconf -f -i -v
%configure --disable-static
%make_build
echo '2e9ad7dd851bf45fab9f75cbff4cb493fee9979e8d8c7c9c3ee119022518edd6  %{SOURCE10}' | sha256sum -c -
tar -xzf %{SOURCE10} -C %{_builddir}
export PYTHONPATH="%{_builddir}/markupsafe-3.0.4/src${PYTHONPATH:+:$PYTHONPATH}"
make html

%check
make check

%install
%make_install
rm "$RPM_BUILD_ROOT%{_libdir}"/*.la

%files
%license LICENSE
%doc CHANGES
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/*

%files devel-doc
%doc doc/_build/html/*

