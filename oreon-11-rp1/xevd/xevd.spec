# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 1ff5910bd50307a5fc164ee87f8e3a1ef3fc3be4fbfd6ed622c929ee05265c93
%global source1_hash f6d04c0cb839d53587c368ff64474a81ab0f8317b16c08a6c16534e3b72a5502
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           xevd
Version:        0.8.0
Release:        %{autorelease}
Summary:        Reference MPEG-5 Part 1 (EVC) decoder

License:        BSD-3-Clause
URL:            https://github.com/mpeg5/xevd
Source0:        %{name}-free-%{version}.tar.gz
Source1:        %{name}_gen_free_tarball.sh
Patch0:         %{name}-format-overflow.patch

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires:  cmake >= 3.12
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description
The eXtra-fast Essential Video Decoder (XEVD) is an
opensource and fast MPEG-5 EVC decoder.

MPEG-5 Essential Video Coding (EVC) is a video compression
standard of ISO/IEC Moving Picture Experts Group (MPEG).
The main goal of the EVC is to provide a significantly
improved compression capability over existing video coding
standards with timely publication of terms.

EVC defines two profiles, including "Baseline Profile" and "Main Profile".

The "Baseline profile" contains only technologies that are older than
20 years or otherwise freely available for use in the standard.
In addition, the "Main profile" adds a small number of additional tools,
each of which can be either cleanly disabled or switched to the
corresponding baseline tool on an individual basis.

This package only includes the "Baseline profile".

%package        libs
Summary:        Library files for %{name}

%description    libs
The %{name}-libs package contains libraries for applications to use
%{name}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
%autosetup -p1

echo "v%{version}" > version.txt

%build
%cmake -DSET_PROF=BASE
%cmake_build

%install
%cmake_install

rm -rfv %{buildroot}%{_libdir}/%{name}*

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}*

%files libs
%license COPYING
%{_libdir}/lib%{name}*.so.0{,.*}

%files devel
%{_libdir}/lib%{name}*.so
%{_includedir}/%{name}*/
%{_libdir}/pkgconfig/%{name}*.pc

%changelog
%autochangelog
