%global source0_hash 2e6dd3bed96479332c4c8e4cab2505699ade418a07797f64ee0d4fa394555032

%global forgeurl https://github.com/tevador/RandomX

Name:    randomx
Version: 1.2.1
Release: %autorelease
Summary: A proof-of-work algorithm that is optimized for general-purpose CPUs
License: BSD-3-Clause
URL:     %forgeurl

%forgemeta
Source0: %forgesource

# From Debian https://salsa.debian.org/cryptocoin-team/librandomx/-/blob/debian/latest/debian/patches/2001_shared-lib.patch
Patch0: randomx-sharedlib.patch

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: cmake >= 3.5

%description
RandomX is a proof-of-work (PoW) algorithm that is optimized for
general-purpose CPUs. RandomX uses random code execution (hence the name)
together with several memory-hard techniques to minimize the efficiency
advantage of specialized hardware.

%package devel
Requires: %{name}%{?_isa} = %{version}-%{release}
Summary: RandomX development files

%description devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_libdir}/librandomx.so.0
%{_libdir}/librandomx.so.0.0.0

%files devel
%license LICENSE
%doc README.md
%doc doc
%{_includedir}/randomx.h
%{_libdir}/librandomx.so

%changelog
%autochangelog
