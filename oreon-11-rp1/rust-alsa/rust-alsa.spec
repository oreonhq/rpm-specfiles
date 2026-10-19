%global source0_hash 7c88dbbce13b232b26250e1e2e6ac18b6a891a646b8148285036ebce260ac5c3
%bcond check 0
%global debug_package %{nil}
%global crate alsa
Name:           rust-alsa
Version:        0.10.0
Release:        1%{?dist}
Summary:        Thin but safe wrappers for ALSA (Linux sound API)
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/alsa
Source0:        https://static.crates.io/crates/alsa/alsa-%{version}.crate
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
Summary:        Thin but safe wrappers for ALSA (Linux sound API)
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

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
%files -n rust-alsa-devel -f %{oreon_filedir}/rust-alsa-devel.list

%changelog

%autochangelog
