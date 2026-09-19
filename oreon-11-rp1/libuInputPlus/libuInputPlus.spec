%global source0_hash a537e156d11ad00c643b93cbd9b712d3ec9d0ae8e40731ff763fe9a6ffe97458

Name:     libuInputPlus
Version:  0.1.4
Release:  20%{?dist}
Summary:  A C++ wrapper around libuinput
License:  MIT
URL:      https://github.com/YukiWorkshop/libuInputPlus
Source0:  %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:   libuInputPlus-patch0-fix-version

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: make

%description
A c++ wrapper around libuinput (required for ydotool).

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
%{_includedir}/uInputPlus/
%{_libdir}/pkgconfig/*

%changelog
%autochangelog
