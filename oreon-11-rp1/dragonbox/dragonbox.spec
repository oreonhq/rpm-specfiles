%global source0_hash 09d63b05e9c594ec423778ab59b7a5aa1d76fdd71d25c7048b0258c4ec9c3384

# Header-only package
%global debug_package %{nil}

Name:           dragonbox
Version:        1.1.3
Release:        %autorelease
Summary:        Reference implementation of Dragonbox in C++

License:        Apache-2.0 WITH LLVM-exception OR BSL-1.0
URL:            https://github.com/jk-jeon/dragonbox
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires: gcc-c++
BuildRequires: cmake

%description
Dragonbox is a float-to-string conversion algorithm based on a beautiful
algorithm Schubfach, developed by Raffaello Giulietti in 2017-2018.
Dragonbox is further inspired by Grisu and Grisu-Exact.

%package devel
Summary:        Development files for %{name}
Provides:       %{name}-static = %{version}-%{release}

%description devel
Development files for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%cmake -DDRAGONBOX_INSTALL_TO_CHARS=OFF
%cmake_build

%check
# No tests provided

%install
%cmake_install

%files devel
%license LICENSE-Apache2-LLVM LICENSE-Boost
%doc README.md
%{_includedir}/%{name}-%{version}/
%{_libdir}/cmake/%{name}-%{version}/

%changelog
%autochangelog
