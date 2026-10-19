%global source0_hash 15cdd26707701c53297e2fa6afb323d55fbc1d0810c3aec078ae3ef0424c3c15
%bcond check 0
%global debug_package %{nil}
%global crate humantime
Name:           rust-humantime
Version:        2.4.0
Release:        1%{?dist}
Summary:        Parser and formatter for std::time::{Duration, SystemTime}
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/humantime
Source0:        https://static.crates.io/crates/humantime/humantime-%{version}.crate
Patch:          humantime-fix-metadata.diff
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
Summary:        Parser and formatter for std::time::{Duration, SystemTime}
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+mu-devel
Summary:        Parser and formatter for std::time::{Duration, SystemTime}
BuildArch:      noarch
%description -n %{name}+mu-devel

This package contains library source intended for building other packages which
use the "mu" feature of the "%{crate}" crate.

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
%files -n rust-humantime-devel -f %{oreon_filedir}/rust-humantime-devel.list

%changelog

%autochangelog
