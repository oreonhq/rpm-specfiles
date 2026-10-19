%global source0_hash 2cfee923ac9a3e15bfbbc99001042e006db064587762d1586592de6b6b01ff17
%global commit b9c006f31b266408bd53079ce7ad57939a237d9a
%global snapdate 20260309
Name:           utest
Version:        0^%{snapdate}.%{sub %{commit} 1 7}
Release:        1%{?dist}
Summary:        Single header unit testing framework for C and C++
License:        Unlicense
URL:            https://github.com/sheredom/utest.h
Source0:        https://github.com/sheredom/%{name}.h/archive/%{commit}/%{name}.h-%{commit}.tar.gz
%global debug_package %{nil}
%global common_description %{expand:
A simple one header solution to unit testing for C/C++.}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
# /oreon:deps
%description %{common_description}

%package devel
Summary:        Development files for %{name}
BuildArch:      noarch
Provides:       %{name}-static = %{version}-%{release}
%description devel %{common_description}

The %{name}-devel package contains header files for developing applications
that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n utest.h-%{commit}

# -Werror is too strict for distribution packaging:
sed -r -i 's/-Werror//' test/CMakeLists.txt

%conf
cd test
%cmake

%build

cd test
%cmake_build
%install
install -t '%{buildroot}%{_includedir}' -D -p -m 0644 utest.h
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

cd test
cd %{_vpath_builddir}
for testbin in utest_test*
do
  printf '\n==== %s ====\n\n' "${testbin}" 1>&2
  "./${testbin}"
done
%files -f %{oreon_filedir}/main.list
%files -n utest-devel -f %{oreon_filedir}/utest-devel.list

%changelog

%autochangelog
