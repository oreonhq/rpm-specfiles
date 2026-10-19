%global source0_hash 1ecbdf8d04b079f8a9404662708d2333d6b72b956effb0d5296d063db3a02b4e
%global debug_package %{nil}
%global common_sum  Portable and easy to integrate C directory and file reader
%global common_desc \
Lightweight, portable and easy to integrate C directory and file reader. \
TinyDir wraps dirent for POSIX and FindFirstFile for Windows.
Name:           tinydir
Version:        1.2.6
Release:        1%{?dist}
Summary:        Portable and easy to integrate C directory and file reader
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/cxong/%{name}
Source0:        https://github.com/cxong/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake3
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
# /oreon:deps
%description
%{common_desc}

%package devel
Summary:        %{common_sum} (header-only)
Provides:       %{name}-static == %{version}-%{release}
BuildArch:      noarch
%description devel
%{common_desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

export CTEST_OUTPUT_ON_FAILURE=1
for d in samples tests; do
  mkdir -p %{_target_platform}_${d}
  pushd %{_target_platform}_${d}
  cmake3 -DCMAKE_VERBOSE_MAKEFILE=ON ../${d}
  popd
  %make_build -C %{_target_platform}_${d}
done
%install
mkdir -p %{buildroot}%{_datadir}/pkgconfig %{buildroot}%{_includedir}
install -pm 0644 %{name}.h %{buildroot}%{_includedir}
cat << EOF > %{buildroot}%{_datadir}/pkgconfig/%{name}.pc
prefix=%{_prefix}
exec_prefix=\${prefix}
includedir=%{_includedir}
Name: %{name}
Version: %{version}
Description: %{common_sum}
EOF
rm -f samples/{.gitignore,CMakeLists.txt}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

pushd %{_target_platform}_tests
ctest3
popd
%files -f %{oreon_filedir}/main.list
%files -n tinydir-devel -f %{oreon_filedir}/tinydir-devel.list

%changelog

%autochangelog
