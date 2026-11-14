# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 6549c0b3e41d1ebe0c94a1be63c25eec918191462b602ab6f47d4a5fa709c3e4

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           pam_wrapper
Version:        1.1.8
Release:        1%{?dist}
Summary:        A tool to test PAM applications and PAM modules
License:        GPL-3.0-or-later
URL:            https://cwrap.org/
Source0:        https://ftp.samba.org/pub/cwrap/%{name}-%{version}.tar.gz
Source1:        pam_wrapper-1.1.8.tar.gz.asc
Source2:        pam_wrapper.keyring

BuildRequires:  oreon-rpm-macros
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  libcmocka-devel
BuildRequires:  pam-devel
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Recommends:     cmake
Recommends:     pkgconfig

%description
This component of cwrap allows you to either test your PAM (Linux-PAM
and OpenPAM) application or module.

For testing PAM applications, simple PAM module called pam_matrix is
included. If you plan to test a PAM module you can use the pamtest library,
which simplifies testing of modules. You can combine it with the cmocka
unit testing framework or you can use the provided Python bindings to
write tests for your module in Python.

%package -n libpamtest
Summary:        Library for testing PAM modules
License:        GPL-3.0-or-later
Requires:       pam_wrapper%{?_isa} = %{version}-%{release}

%description -n libpamtest
If you plan to test a PAM module you can use this library, which simplifies
testing of modules.

%package -n libpamtest-devel
Summary:        Development files for libpamtest
License:        GPL-3.0-or-later
Requires:       pam_wrapper%{?_isa} = %{version}-%{release}
Requires:       libpamtest%{?_isa} = %{version}-%{release}
Recommends:     cmake
Recommends:     pkgconfig

%description -n libpamtest-devel
If you plan to develop tests for a PAM module you can use this library,
which simplifies testing of modules. This sub package includes the header
files for libpamtest.

%package -n libpamtest-doc
Summary:        The libpamtest API documentation
License:        GPL-3.0-or-later
BuildArch:      noarch

%description -n libpamtest-doc
Documentation for libpamtest development.

%package -n python3-libpamtest
Summary:        A python wrapper for libpamtest
License:        GPL-3.0-or-later
Requires:       pam_wrapper%{?_isa} = %{version}-%{release}
Requires:       libpamtest%{?_isa} = %{version}-%{release}

%description -n python3-libpamtest
If you plan to develop python tests for a PAM module you can use this
Python module to quickly write tests in Python.

%prep
%oreon_sha256
%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}
%autosetup -p1

%build
%cmake \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DUNIT_TESTING=ON \
  -DPYTHON_INSTALL_SITEARCH=%{python3_sitearch}
%cmake_build
%__cmake --build %{__cmake_builddir} --target doc

%install
%cmake_install

%check
%ctest

%ldconfig_scriptlets

%ldconfig_scriptlets -n libpamtest

%files
%license LICENSE
%{_libdir}/libpam_wrapper.so*
%{_libdir}/pkgconfig/pam_wrapper.pc
%dir %{_libdir}/cmake/pam_wrapper
%{_libdir}/cmake/pam_wrapper/pam_wrapper-config-version.cmake
%{_libdir}/cmake/pam_wrapper/pam_wrapper-config.cmake
%dir %{_libdir}/pam_wrapper
%{_libdir}/pam_wrapper/pam_chatty.so
%{_libdir}/pam_wrapper/pam_matrix.so
%{_libdir}/pam_wrapper/pam_get_items.so
%{_libdir}/pam_wrapper/pam_set_items.so
%{_mandir}/man1/pam_wrapper.1*
%{_mandir}/man8/pam_chatty.8*
%{_mandir}/man8/pam_matrix.8*
%{_mandir}/man8/pam_get_items.8*
%{_mandir}/man8/pam_set_items.8*

%files -n libpamtest
%{_libdir}/libpamtest.so.*

%files -n libpamtest-devel
%{_libdir}/libpamtest.so
%{_libdir}/pkgconfig/libpamtest.pc
%dir %{_libdir}/cmake/pamtest
%{_libdir}/cmake/pamtest/pamtest-config-relwithdebinfo.cmake
%{_libdir}/cmake/pamtest/pamtest-config-version.cmake
%{_libdir}/cmake/pamtest/pamtest-config.cmake
%{_includedir}/libpamtest.h

%files -n libpamtest-doc
%doc %{__cmake_builddir}/doc/html

%files -n python3-libpamtest
%{python3_sitearch}/pypamtest.so

%changelog
%autochangelog
