%global source0_hash 9e98c25665909853c07874301124482754434520ab572ac6a22e90366de6685b
%ifarch %{ix86}
%bcond check 1
%else
%bcond check 0
%endif
%global debug_package %{nil}
%global crate rio
Name:           rust-rio
Version:        0.9.4
Release:        1%{?dist}
Summary:        Rust bindings for io_uring
License:        GPL-3.0-or-later
URL:            https://crates.io/crates/rio
Source0:        https://static.crates.io/crates/rio/rio-%{version}.crate
Patch:          rio-fix-metadata.diff
Patch2:        rio-pointer-size.patch
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
Summary:        Rust bindings for io_uring
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+no_metrics-devel
Summary:        Rust bindings for io_uring
BuildArch:      noarch
%description -n %{name}+no_metrics-devel

This package contains library source intended for building other packages which
use the "no_metrics" feature of the "%{crate}" crate.

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
%files -n rust-rio-devel -f %{oreon_filedir}/rust-rio-devel.list

%changelog

%autochangelog
