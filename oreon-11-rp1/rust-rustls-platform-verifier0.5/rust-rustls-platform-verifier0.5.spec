%global source0_hash 19787cda76408ec5404443dc8b31795c87cd8fec49762dc75fa727740d34acc1
%bcond check 1
%global debug_package %{nil}
%global crate rustls-platform-verifier
Name:           rust-rustls-platform-verifier0.5
Version:        0.5.3
Release:        1%{?dist}
Summary:        Verify TLS certificates in rustls with the operating system verifier
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/rustls-platform-verifier
Source0:        https://static.crates.io/crates/rustls-platform-verifier/rustls-platform-verifier-%{version}.crate
Patch:          rustls-platform-verifier-fix-metadata-auto.diff
Patch:          rustls-platform-verifier-fix-metadata.diff
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
Summary:        Verify TLS certificates in rustls with the operating system verifier
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+base64-devel
Summary:        Verify TLS certificates in rustls with the operating system verifier
BuildArch:      noarch
%description -n %{name}+base64-devel

This package contains library source intended for building other packages which
use the "base64" feature of the "%{crate}" crate.

%package     -n %{name}+cert-logging-devel
Summary:        Verify TLS certificates in rustls with the operating system verifier
BuildArch:      noarch
%description -n %{name}+cert-logging-devel

This package contains library source intended for building other packages which
use the "cert-logging" feature of the "%{crate}" crate.

%package     -n %{name}+dbg-devel
Summary:        Verify TLS certificates in rustls with the operating system verifier
BuildArch:      noarch
%description -n %{name}+dbg-devel

This package contains library source intended for building other packages which
use the "dbg" feature of the "%{crate}" crate.

%package     -n %{name}+ffi-testing-devel
Summary:        Verify TLS certificates in rustls with the operating system verifier
BuildArch:      noarch
%description -n %{name}+ffi-testing-devel

This package contains library source intended for building other packages which
use the "ffi-testing" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
chmod -x src/tests/verification_real_world/update_valid_ee_certs.rs
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
%files -n rust-rustls-platform-verifier0.5-devel -f %{oreon_filedir}/rust-rustls-platform-verifier0.5-devel.list

%changelog

%autochangelog
