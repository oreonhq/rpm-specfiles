%global source0_hash c941b6b45f784c1e6c6f316f59256fabd604ac392db405cf7fd99de2686aaab0

Name:     libevdevPlus
Version:  0.1.1
Release:  20%{?dist}
Summary:  A C++ wrapper around libevdev
License:  MIT
URL:      https://github.com/YukiWorkshop/libevdevPlus
Source0:  %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:   libevdevPlus-patch0-fix-version

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: make

%description
A c++ wrapper around libevdev (required for ydotool).

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
This package contains header files for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} ..
%cmake_build

%install
cd %{_target_platform}; %cmake_install
rm -f %{buildroot}%{_libdir}/%{name}.a

%files
%{_libdir}/%{name}.so.0*

%doc README.md

%license LICENSE

%files devel
%{_libdir}/%{name}.so
%{_includedir}/evdevPlus/
%{_libdir}/pkgconfig/*

%changelog
%autochangelog
