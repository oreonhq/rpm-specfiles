%global source0_hash 0398022d5f700414f6b899e10b8348231abf9173fa93144cbc1a43b9793c1fbc
%bcond check 1
%global debug_package %{nil}
%global crate unic-char-range
Name:           rust-unic-char-range
Version:        0.9.0
Release:        1%{?dist}
Summary:        UNIC — Unicode Character Tools — Character Range and Iteration
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/unic-char-range
Source0:        https://static.crates.io/crates/unic-char-range/unic-char-range-%{version}.crate
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
Summary:        UNIC — Unicode Character Tools — Character Range and Iteration
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+exact-size-is-empty-devel
Summary:        UNIC — Unicode Character Tools — Character Range and Iteration
BuildArch:      noarch
%description -n %{name}+exact-size-is-empty-devel

This package contains library source intended for building other packages which
use the "exact-size-is-empty" feature of the "%{crate}" crate.

%package     -n %{name}+fused-devel
Summary:        UNIC — Unicode Character Tools — Character Range and Iteration
BuildArch:      noarch
%description -n %{name}+fused-devel

This package contains library source intended for building other packages which
use the "fused" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        UNIC — Unicode Character Tools — Character Range and Iteration
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+trusted-len-devel
Summary:        UNIC — Unicode Character Tools — Character Range and Iteration
BuildArch:      noarch
%description -n %{name}+trusted-len-devel

This package contains library source intended for building other packages which
use the "trusted-len" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-devel
Summary:        UNIC — Unicode Character Tools — Character Range and Iteration
BuildArch:      noarch
%description -n %{name}+unstable-devel

This package contains library source intended for building other packages which
use the "unstable" feature of the "%{crate}" crate.

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
%files -n rust-unic-char-range-devel -f %{oreon_filedir}/rust-unic-char-range-devel.list

%changelog

%autochangelog
