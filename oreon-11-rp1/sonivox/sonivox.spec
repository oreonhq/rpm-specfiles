%global source0_hash 5c513d7a6fa0ebf61afd3b96da881e3014edf53acfb8d08a63dd853fca37c1fa
Name:           sonivox
Version:        4.0.2
Release:        1%{?dist}
Summary:        Fork of the AOSP 'platform_external_sonivox' to use out of Android
License:        Apache-2.0
URL:            https://github.com/pedrolcl/sonivox
Source0:        https://github.com/pedrolcl/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gtest-devel
# /oreon:deps
%description
This is a Wave Table synthesizer, not using external soundfont files but
embedded samples instead. It is also a real time GM synthesizer.

It consumes very little resources, so it may be indicated in projects for small
embedded devices. There is neither MIDI input nor Audio output facilities
included in the library. You need to provide your own input/output.

%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
Header files and libraries for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake -DBUILD_SONIVOX_STATIC=OFF
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n sonivox-devel -f %{oreon_filedir}/sonivox-devel.list

%changelog

%autochangelog
