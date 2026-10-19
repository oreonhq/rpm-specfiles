%global source0_hash e91c71b58f59d08c7b8289be8f687866863d934dfaa528e4be30b178139ae863
Name:           hedley
Summary:        A C/C++ header to help move #ifdefs out of your code
Version:        15
Release:        1%{?dist}
URL:            https://nemequ.github.io/hedley/
%global forgeurl https://github.com/nemequ/hedley
Source0:        %{forgeurl}/archive/v%{version}/%{name}-%{version}.tar.gz
License:        CC0-1.0
%global debug_package %{nil}
%global common_description %{expand:
Hedley is a single C/C++ header you can include in your project to enable
compiler-specific features while retaining compatibility with all compilers. It
contains dozens of macros to help make your code easier to use, harder to
misuse, safer, faster, and more portable.
You can safely include Hedley in your public API, and it works with virtually
any C or C++ compiler.}
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  make
# /oreon:deps
%description %{common_description}

%package devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       hedley-static = %{version}-%{release}
%description devel %{common_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%install
install -t %{buildroot}%{_includedir} -p -m 0644 -D hedley.h
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%make_build -C test
%files -f %{oreon_filedir}/main.list
%files -n hedley-devel -f %{oreon_filedir}/hedley-devel.list

%changelog

%autochangelog
