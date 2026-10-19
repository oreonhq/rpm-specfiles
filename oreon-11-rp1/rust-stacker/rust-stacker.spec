%global source0_hash 707f49d46706bacf8a2b00d51dace3f9de527c13eec3778f570c411f89e69967
%bcond check 0
%global debug_package %{nil}
%global crate stacker
Name:           rust-stacker
Version:        0.1.25
Release:        1%{?dist}
Summary:        A stack growth library useful when implementing deeply recursive
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/stacker
Source0:        https://static.crates.io/crates/stacker/stacker-%{version}.crate
Patch:          stacker-fix-metadata-auto.diff
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
Summary:        A stack growth library useful when implementing deeply recursive
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
%files -n rust-stacker-devel -f %{oreon_filedir}/rust-stacker-devel.list

%changelog

%autochangelog
