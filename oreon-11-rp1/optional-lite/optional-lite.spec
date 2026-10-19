%global source0_hash 2be17fcfc764809612282c3e728cabc42afe703b9dc333cc87c48d882fcfc2c2
Name:           optional-lite
Version:        3.6.0
Release:        1%{?dist}
Summary:        Represent optional (nullable) objects and pass them by value
License:        BSL-1.0
URL:            https://github.com/martinmoene/optional-lite
Source0:        https://github.com/martinmoene/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
%global debug_package %{nil}
%global common_description %{expand:
A single-file header-only version of a C++17-like optional, a nullable object
for C++98, C++11 and later.}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  lest-devel
BuildRequires:  lest-static
# /oreon:deps
%description %{common_description}

%package devel
Summary:        Development files for %{name}
Provides:       %{name}-static = %{version}-%{release}
%description devel %{common_description}

The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n optional-lite-%{version}

# Unbundle lest
rm -rvf test/lest
ln -s /usr/include/lest test/lest

%conf
%cmake

%build

%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n optional-lite-devel -f %{oreon_filedir}/optional-lite-devel.list

%changelog

%autochangelog
