# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 8c01fb69fc5ef1e33b654d811161c3df3759878c7c61c5d66a149751bd680516
%global source1_hash 509440924751fdd87ffaa5683ee3dddd937af5c833b9104ccce65d51614926c8
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%undefine __cmake_in_source_build
%global sover 0.5

Name:           lpcnetfreedv
Version:        0.5
Release:        1%{?dist}
Summary:        LPCNet for FreeDV

License:        LicenseRef-Callaway-BSD
URL:            https://github.com/drowe67/LPCNet
Source0:        https://github.com/drowe67/LPCNet/archive/v%{version}/LPCNet-%{version}.tar.gz
Source1:        http://rowetel.com/downloads/deep/lpcnet_191005_v1.0.tgz

Patch0:         lpcnetfreedv-libm.patch

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires:  cmake
%description
Experimental version of LPCNet that has been used to develop FreeDV 2020 - a HF
radio Digial Voice mode for over the air experimentation with Neural Net speech
coding. Possibly the first use of Neural Net speech coding in real world
operation.

%package devel
Requires:       %{name}%{?_isa} = %{version}-%{release}
Summary:        Development files and tools for LPCNet

%description devel
%{summary}.

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
%autosetup -p1 -n LPCNet-%{version}

%build
mkdir -p %{_vpath_builddir}
cp %{SOURCE1} %{__cmake_builddir}/

export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake
%cmake_build

%install
%cmake_install

%check

%files
%license COPYING
%doc README.md
%{_libdir}/lib%{name}.so.%{sover}

%files devel
%{_bindir}/*
%{_includedir}/lpcnet/
%{_libdir}/cmake/lpcnetfreedv/
%{_libdir}/lib%{name}.so

%changelog
%autochangelog
