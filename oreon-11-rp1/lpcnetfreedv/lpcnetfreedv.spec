%global source1_hash 509440924751fdd87ffaa5683ee3dddd937af5c833b9104ccce65d51614926c8
%global source0_hash 8c01fb69fc5ef1e33b654d811161c3df3759878c7c61c5d66a149751bd680516
%undefine __cmake_in_source_build
%global sover 0.5
Name:           lpcnetfreedv
Version:        0.5
Release:        10%{?dist}
Summary:        LPCNet for FreeDV
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/drowe67/LPCNet
Source0:        https://github.com/drowe67/LPCNet/archive/v%{version}/LPCNet-%{version}.tar.gz
Source1:        http://rowetel.com/downloads/deep/lpcnet_191005_v1.0.tgz
Patch0:         lpcnetfreedv-libm.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
# /oreon:deps
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir LPCNet-%{version}
%oreon_prep
%build

mkdir -p %{_vpath_builddir}
cp %{SOURCE1} %{__cmake_builddir}/
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%files -f %{oreon_filedir}/main.list
%files -n lpcnetfreedv-devel -f %{oreon_filedir}/lpcnetfreedv-devel.list

%changelog

%autochangelog
