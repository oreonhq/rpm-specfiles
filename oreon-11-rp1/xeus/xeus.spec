%global source0_hash ea19c4e742b8c0f62cfcd7660dfc65e2ae5fba9579a08385e8bd8ae4951ff70a

Name:           xeus
Version:        5.2.6
Release:        %autorelease
Summary:        C++ implementation of the Jupyter kernel protocol

License:        BSD-3-Clause
URL:            https://github.com/jupyter-xeus/xeus
Source0:        https://github.com/jupyter-xeus/xeus/archive/%{version}/%{name}-%{version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

BuildRequires:  cmake >= 3.8
BuildRequires:  cmake(nlohmann_json) >= 3.11.0
BuildRequires:  doctest-devel
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  libuuid-devel
BuildRequires:  make
BuildRequires:  pkgconfig(uuid)
BuildRequires:  python3dist(breathe)
BuildRequires:  python3dist(jupyter-kernel-test)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)

%description
xeus is a library meant to facilitate the implementation of kernels for
Jupyter. It takes the burden of implementing the Jupyter Kernel protocol so
developers can focus on implementing the interpreter part of the kernel.

%package devel
Summary:        %{summary}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for %{name} library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake -DXEUS_BUILD_STATIC_LIBS=OFF -DXEUS_DISABLE_ARCH_NATIVE=ON -DXEUS_BUILD_TESTS=ON
%cmake_build

make -C docs SPHINXBUILD=sphinx-build-3 html
rm docs/build/html/.buildinfo

%install
%cmake_install

%check
%ctest

%files
%doc README.md docs/build/html
%license LICENSE
%{_libdir}/libxeus.so.13{,.*}

%files devel
%{_includedir}/xeus/
%{_libdir}/cmake/xeus/
%{_libdir}/libxeus.so

%changelog
%autochangelog
