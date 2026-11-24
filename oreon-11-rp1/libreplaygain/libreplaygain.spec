# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 8258bf785547ac2cda43bb195e07522f0a3682f55abe97753c974609ec232482
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global svn_release 475

Name:           libreplaygain
Version:        0
Release:        %{autorelease}
Summary:        Gain analysis library from Musepack

License:        LGPL-2.0-or-later
URL:            http://www.musepack.net/index.php
Source0:        http://files.musepack.net/source/%{name}_r%{svn_release}.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires:  cmake
%description
Gain analysis library used by Musepack utilities and libraries

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%oreon_sha256
%setup -q -n %{name}_r%{svn_release}

chmod 0644 include/replaygain/*.h src/gain_analysis.c
sed -ibackup 's/\r$//' include/replaygain/*.h src/gain_analysis.c

sed '5,9d' -ibackup CMakeLists.txt

%build
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake .
%cmake_build

%install
%cmake_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
rm $RPM_BUILD_ROOT/%{_libdir}/%{name}.a

mkdir -p $RPM_BUILD_ROOT/%{_includedir}/replaygain/
cp -v include/replaygain/*.h $RPM_BUILD_ROOT/%{_includedir}/replaygain/

%files
%{_libdir}/*.so.1
%{_libdir}/*.so.1.0.0

%files devel
%{_includedir}/replaygain
%{_libdir}/*.so

%changelog
%autochangelog
