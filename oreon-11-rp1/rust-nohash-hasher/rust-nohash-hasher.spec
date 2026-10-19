%global source0_hash 2bf50223579dc7cdcfb3bfcacf7069ff68243f8c363f62ffa99cf000a6b9c451
%bcond check 1
%global debug_package %{nil}
%global crate nohash-hasher
Name:           rust-nohash-hasher
Version:        0.2.0
Release:        1%{?dist}
Summary:        Implementation of std::hash::Hasher which does not hash at all
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/nohash-hasher
Source0:        https://static.crates.io/crates/nohash-hasher/nohash-hasher-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Implementation of std::hash::Hasher which does not hash at all
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Implementation of std::hash::Hasher which does not hash at all
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build
%install
%cargo_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-nohash-hasher-devel -f %{oreon_filedir}/rust-nohash-hasher-devel.list

%changelog

%autochangelog
