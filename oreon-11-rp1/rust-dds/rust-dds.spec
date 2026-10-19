%global source0_hash e917a58e17b27d2f15626c490754ccced7f46592dc5b5f39a3013b89cba5f068
%bcond check 0
%global debug_package %{nil}
%global crate dds
Name:           rust-dds
Version:        0.2.0
Release:        1%{?dist}
Summary:        DDS de/encoder written in 100% safe Rust
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/dds
Source0:        https://static.crates.io/crates/dds/dds-%{version}.crate
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
Summary:        DDS de/encoder written in 100% safe Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+rayon-devel
Summary:        DDS de/encoder written in 100% safe Rust
BuildArch:      noarch
%description -n %{name}+rayon-devel

This package contains library source intended for building other packages which
use the "rayon" feature of the "%{crate}" crate.

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
%files -n rust-dds-devel -f %{oreon_filedir}/rust-dds-devel.list

%changelog

%autochangelog
