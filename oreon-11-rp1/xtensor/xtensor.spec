%global source0_hash 117c192ae3b7c37c0156dedaa88038e0599a6b264666c3c6c2553154b500fe23

%undefine __cmake_in_source_build

Name:           xtensor
Version:        0.27.1
Release:        %autorelease
Summary:        C++ tensors with broadcasting and lazy computing
License:        BSD-3-Clause
URL:            http://xtensor.readthedocs.io/

%global github  https://github.com/QuantStack/xtensor
Source0:        %{github}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gtest-devel
BuildRequires:  xtl-devel
BuildRequires:  xsimd-devel
BuildRequires:  python3-numpy
BuildRequires:  doctest-devel
BuildRequires:  json-devel

# there is no actual arched content - this is a header only library
%global debug_package %{nil}

%global _description %{expand:
xtensor is a C++ library meant for numerical analysis with multi-dimensional
array expressions.

xtensor provides:
- an extensible expression system enabling lazy broadcasting.
- an API following the idioms of the C++ standard library.
- tools to manipulate array expressions and build upon xtensor.}


%description %_description

%package devel
Summary:        %{summary}
Provides:       %{name} = %{version}-%{release}
Provides:       %{name}-static = %{version}-%{release}
Requires:       xtl-devel
Requires:       xsimd-devel

%description devel %_description


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%ifarch s390x
find -name '*.npy' -exec %{__python3} -c "import numpy as np; arr = np.load('{}').byteswap() ; np.save('{}', arr.view(arr.dtype.newbyteorder()))" \;
%endif

%build
%cmake -DBUILD_TESTS=ON
%cmake_build

%install
%cmake_install
rm %{buildroot}%{_prefix}/etc/xeus-cpp/tags.d/xtensor.json
rm %{buildroot}%{_datadir}/xeus-cpp/tagfiles/xtensor.tag

%check
%cmake_build --target xtest

%files devel
%doc README.md
%license LICENSE
%{_includedir}/%{name}.hpp
%{_includedir}/%{name}/
%{_datadir}/cmake/%{name}/
%{_datadir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
