%global source0_hash d512b3e61196d27562dcc71446a58ba8a93d3bed2a03a87f96101b9a17f1d378
%bcond check 0
%global debug_package %{nil}
%global crate appdirs
Name:           rust-appdirs
Version:        0.2.0
Release:        1%{?dist}
Summary:        Rust crate for determining platform-specific directories
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/appdirs
Source0:        https://static.crates.io/crates/appdirs/appdirs-%{version}.crate
Patch:          appdirs-fix-metadata-auto.diff
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
Summary:        Rust crate for determining platform-specific directories
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
%files -n rust-appdirs-devel -f %{oreon_filedir}/rust-appdirs-devel.list

%changelog

%autochangelog
