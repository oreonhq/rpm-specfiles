%global source0_hash 76ddbf406e9d9b772ec73af2bf925b38b290b4390cc4064720a08d4b4bca0aa9
%global debug_package %{nil}
Name:           half
Version:        2.2.1
Release:        1%{?dist}
Summary:        A C++ half-precision floating point type
License:        MIT
URL:            http://sourceforge.net/projects/half
Source0:        http://sourceforge.net/projects/%{name}/files/%{name}/%{version}/%{name}-%{version}.zip
BuildArch:      noarch
# oreon:deps
BuildRequires:  unzip
# /oreon:deps
%description
This is a C++ header-only library to provide an IEEE-754 conformant
half-precision floating point type along with corresponding arithmetic
operators, type conversions and common mathematical functions. It aims
for both efficiency and ease of use, trying to accurately mimic the
behaviour of the builtin floating point types at the best performance
possible. It automatically uses and provides C++11 features when
possible, but stays completely C++98-compatible when neccessary.

%package devel
Summary:        A C++ half-precision floating point type
Provides:       %{name}-static = %{version}-%{release}
%description devel
This is a C++ header-only library to provide an IEEE-754 conformant
half-precision floating point type along with corresponding arithmetic
operators, type conversions and common mathematical functions. It aims
for both efficiency and ease of use, trying to accurately mimic the
behaviour of the builtin floating point types at the best performance
possible. It automatically uses and provides C++11 features when
possible, but stays completely C++98-compatible when neccessary.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

rm -rf %{name}-%{version}
unzip -d %{name}-%{version} %{SOURCE0}
cd %{name}-%{version}
# change dos endings to unix
sed -i "s|\r||g" include/half.hpp
sed -i "s|\r||g" LICENSE.txt
sed -i "s|\r||g" README.txt

%install
cd %{name}-%{version}
mkdir -p %{buildroot}%{_includedir}
install -m 644 include/half.hpp %{buildroot}%{_includedir}
mkdir -p %{buildroot}%{_docdir}/%{name}/
install -m 644 LICENSE.txt %{buildroot}%{_docdir}/%{name}/
install -m 644 README.txt %{buildroot}%{_docdir}/%{name}/
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n half-devel -f %{oreon_filedir}/half-devel.list

%changelog

%autochangelog
