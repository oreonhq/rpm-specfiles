%global source0_hash 1c00acbd29eabad4a2392fa0e921c874934dbbf4194312ad20f04a0ed67a3cb3
%bcond check 0
%global debug_package %{nil}
%global crate jobserver
Name:           rust-jobserver
Version:        0.1.35
Release:        1%{?dist}
Summary:        An implementation of the GNU Make jobserver for Rust.
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/jobserver
Source0:        https://static.crates.io/crates/jobserver/jobserver-%{version}.crate
Patch:          jobserver-fix-metadata-auto.diff
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
Summary:        An implementation of the GNU Make jobserver for Rust.
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
%files -n rust-jobserver-devel -f %{oreon_filedir}/rust-jobserver-devel.list

%changelog

%autochangelog
