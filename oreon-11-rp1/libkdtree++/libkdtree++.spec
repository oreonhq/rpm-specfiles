%global source0_hash 047c3c87062bdc6f5f1c828eca2fb9e0e74c8ca3ed1d81ebf666cb1d986d2de3

Name:           libkdtree++
Version:        0.7.5
Release:        2%{?dist}
Summary:        C++ template container implementation of kd-tree sorting
URL:            https://github.com/nvmd/libkdtree
License:        Artistic-2.0

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  python3-devel
BuildRequires:  swig

Source0:        https://github.com/nvmd/libkdtree/archive/v%{version}/%{name}-%{version}.tar.gz
# Fix python module build
Patch0:         libkdtree_cmake.patch
# Fix python test
Patch1:         libkdtree_pythontest.patch

%description
%{summary}.

%package devel
Summary:        C++ template container implementation of kd-tree sorting
BuildArch:      noarch

%description devel
%{summary}.

%package -n python3-libkdtree++
Summary:        Python3 language bindings for libkdtree++

%description -n python3-libkdtree++
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n libkdtree-%{version}

# convert files from ISO-8859-1 to UTF-8 encoding
for f in README.md
do
  iconv -fiso88591 -tutf8 $f >$f.new
  touch -r $f $f.new
  mv $f.new $f
done

%build
pushd python-bindings
%{__python3} gen-swig-hpp.py
popd
%cmake -DBUILD_PYTHON_BINDINGS=ON
%cmake_build

%install
%cmake_install

# Fix python module permission
chmod 0755 %{buildroot}%{python3_sitearch}/_kdtree.so

sed \
  -e 's|@prefix@|%{_prefix}|' \
  -e 's|@libdir@|%{_libdir}|' \
  -e 's|@includedir@|%{_includedir}/kdtree++|' \
  -e 's|@VERSION@|%{version}|' \
  pkgconfig/libkdtree++.pc.in > pkgconfig/libkdtree++.pc
install -Dpm 0644 pkgconfig/libkdtree++.pc %{buildroot}%{_datadir}/pkgconfig/libkdtree++.pc

%check
pushd %{_vpath_builddir}/examples
./test_find_within_range
./test_hayne
./test_kdtree
popd
pushd python-bindings
PYTHONPATH=%{buildroot}%{python3_sitearch} %{__python3} py-kdtree_test.py
popd

%files devel
%doc README.md
%license COPYING
%{_includedir}/kdtree++/
%{_datadir}/pkgconfig/libkdtree++.pc

%files -n python3-libkdtree++
%doc README.md
%license COPYING
%{python3_sitearch}/_kdtree.so
%{python3_sitearch}/kdtree.py
%{python3_sitearch}/__pycache__/*

%changelog
%autochangelog
