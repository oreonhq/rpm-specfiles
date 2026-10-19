%global source0_hash f639046355ee4f37944e44f60642c6f3a7efa3cf6b78c78a0d989a8ce6c396a1
%bcond check 0
%global debug_package %{nil}
%global crate errno
Name:           rust-errno0.2
Version:        0.2.8
Release:        1%{?dist}
Summary:        Cross-platform interface to the `errno` variable.
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/errno
Source0:        https://static.crates.io/crates/errno/errno-%{version}.crate
Patch:          errno-fix-metadata-auto.diff
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
Summary:        Cross-platform interface to the `errno` variable.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Cross-platform interface to the `errno` variable.
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
%files -n rust-errno0.2-devel -f %{oreon_filedir}/rust-errno0.2-devel.list

%changelog

%autochangelog
