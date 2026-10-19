%global source0_hash 297a1206e0ca6302a0eed35b700d292b275256f596e2f3fea7729d5e629b6ff4
%bcond check 0
%global debug_package %{nil}
%global crate tokio-fs
Name:           rust-tokio-fs
Version:        0.1.7
Release:        1%{?dist}
Summary:        Filesystem API for Tokio.
License:        MIT
URL:            https://crates.io/crates/tokio-fs
Source0:        https://static.crates.io/crates/tokio-fs/tokio-fs-%{version}.crate
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
Summary:        Filesystem API for Tokio.
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
%files -n rust-tokio-fs-devel -f %{oreon_filedir}/rust-tokio-fs-devel.list

%changelog

%autochangelog
