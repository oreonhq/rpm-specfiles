%global source0_hash 23a7f29c617e791dfcb50b75eef41464e4bf3fca15b19da395a64373ff5d8456

Name:           sonivox
Version:        3.6.12
Release:        %{autorelease}
Summary:        Fork of the AOSP 'platform_external_sonivox' to use out of Android

# migrated to SPDX
License:        Apache-2.0
URL:            https://github.com/pedrolcl/sonivox
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gtest-devel

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

%autosetup

%build
%cmake -DBUILD_SONIVOX_STATIC=OFF
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSE
%doc README.md
%{_libdir}/lib%{name}.so.3*

%files devel
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/cmake/%{name}

%changelog
%autochangelog
