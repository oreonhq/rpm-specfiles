%global source0_hash 327cfcb81ef0c42f4b1d5c24b25d56932b57d64ccd9f00ed919a893a43333411

%global appname olm

Name: libolm
Version: 3.2.16
Release: 11%{?dist}

Summary: Double Ratchet cryptographic library
License: Apache-2.0
URL: https://gitlab.matrix.org/matrix-org/%{appname}
Source0: https://gitlab.matrix.org/matrix-org/%{appname}/-/archive/%{version}/%{appname}-%{version}.tar.bz2

BuildRequires: ninja-build
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: gcc

BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3dist(cffi)
BuildRequires: python3dist(wheel)

%description
An implementation of the Double Ratchet cryptographic ratchet in C++.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%package python3
Summary: Python 3 bindings for %{name}
%{?python_provide:%python_provide python3-%{appname}}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%description python3
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{appname}-%{version} -p1
sed -e "s@/build@/%{_vpath_builddir}@g" -e 's@"build"@"%{_vpath_builddir}"@g' -i python/olm_build.py

%build
# TODO: Please submit an issue to upstream (rhbz#2380743)
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DOLM_TESTS=ON
%cmake_build

pushd python
%py3_build
popd

%check
pushd %{_vpath_builddir}/tests
    ctest --output-on-failure
popd

%install
%cmake_install

pushd python
%py3_install
popd

%files
%license LICENSE
%doc *.md *.rst docs/*.md
%{_libdir}/%{name}.so.3*

%files devel
%{_includedir}/%{appname}
%{_libdir}/%{name}.so
%{_libdir}/cmake/Olm
%{_libdir}/pkgconfig/%{appname}.pc

%files python3
%{python3_sitearch}/%{appname}
%{python3_sitearch}/_%{name}.abi3.so
%{python3_sitearch}/python_%{appname}-*.egg-info

%changelog
%autochangelog
