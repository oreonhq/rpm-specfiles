%global source0_hash 77fe893cbe6973afa85c736bc50f2a96888ba238b29b6aec8ecb60f81e2e899d
%global debug_package %{nil}
%global forgeurl https://github.com/free-audio/clap
Version:        1.2.10
%global tag %{version}
%forgemeta
Name:           clap
Release:        1%{?dist}
Summary:        Audio Plugin API
License:        MIT
URL:            %{forgeurl}
Source0:        %{forgeurl}/archive/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
# /oreon:deps
%description
CLAP stands for CLever Audio Plugin. It is an interface that provides a stable
ABI to define a standard for Digital Audio Workstations and audio plugins
(synthesizers, audio effects, ...) to work together.

%package        devel
Summary:        Development files for CLAP
Provides:       %{name}-static = %{version}-%{release}
%description    devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n clap-devel -f %{oreon_filedir}/clap-devel.list

%changelog

%autochangelog
