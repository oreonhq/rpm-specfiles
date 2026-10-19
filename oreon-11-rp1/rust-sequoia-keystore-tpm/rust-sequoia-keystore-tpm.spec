%global source0_hash 6bab75ae186ec7697e403eb84e6a312472e7e497ec76b99a4a1ca9bd8ffbc54a
%bcond check 0
%global debug_package %{nil}
%global crate sequoia-keystore-tpm
Name:           rust-sequoia-keystore-tpm
Version:        0.2.0
Release:        1%{?dist}
Summary:        A TPM backend for Sequoia's private key store.
License:        LGPL-2.0-or-later
URL:            https://crates.io/crates/sequoia-keystore-tpm
Source0:        https://static.crates.io/crates/sequoia-keystore-tpm/sequoia-keystore-tpm-%{version}.crate
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
Summary:        A TPM backend for Sequoia's private key store.
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
%files -n rust-sequoia-keystore-tpm-devel -f %{oreon_filedir}/rust-sequoia-keystore-tpm-devel.list

%changelog

%autochangelog
