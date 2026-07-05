%global source0_hash e69a696068ccffd2b435539d583665981b6c6abed596a72832bffbe3e13e1f49
# Header-only library.
%global debug_package %{nil}

Name:           xtl
Version:        0.8.1
Release:        %autorelease
License:        BSD-3-Clause
Summary:        QuantStack tools library
Url:            https://github.com/QuantStack/xtl
Source0:        https://github.com/QuantStack/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  binutils
BuildRequires:  cmake
BuildRequires:  doctest-devel
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  cmake(nlohmann_json)
BuildRequires:  python3dist(breathe)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)

%description
Basic tools (containers, algorithms) used by other QuantStack packages.


%package devel
Summary:        %{summary}
Provides:       xtl-static = %{version}-%{release}
Requires:       cmake-filesystem

%description devel
Development files for %{name} library.


%package doc
Summary:        %{summary}

%description doc
Documentation files for %{name} library.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1


%build
%cmake -DBUILD_TESTS=ON
%cmake_build

pushd docs
make html SPHINXBUILD=sphinx-build-3
rm build/html/.buildinfo
popd

%install
%cmake_install

%check
%cmake_build --target xtest

%files devel
%doc README.md
%license LICENSE
%{_includedir}/xtl/
%{_datadir}/cmake/xtl/
%{_datadir}/pkgconfig/xtl.pc

%files doc
%doc docs/build/html

%changelog
%autochangelog
