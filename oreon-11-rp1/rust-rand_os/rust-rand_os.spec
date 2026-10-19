%global source0_hash 7b75f676a1e053fc562eafbb47838d67c84801e38fc1ba459e8f180deabd5071
%bcond check 0
%global debug_package %{nil}
%global crate rand_os
Name:           rust-rand_os
Version:        0.1.3
Release:        1%{?dist}
Summary:        OS backed Random Number Generator
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/rand_os
Source0:        https://static.crates.io/crates/rand_os/rand_os-%{version}.crate
Patch:          rand_os-fix-metadata-auto.diff
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

%package     -n %{name}+log-devel
Summary:        OS backed Random Number Generator
BuildArch:      noarch
%description -n %{name}+log-devel

This package contains library source intended for building other packages which
use the "log" feature of the "%{crate}" crate.

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
%files -n rust-rand_os-devel -f %{oreon_filedir}/rust-rand_os-devel.list

%changelog

%autochangelog
