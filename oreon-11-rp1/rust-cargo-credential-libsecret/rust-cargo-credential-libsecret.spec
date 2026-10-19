%global source0_hash 7a84968127ab001ecc938ea245ad6d93be6039eb7732ead0f16f9b83fc8d5334
%bcond check 0
%global debug_package %{nil}
%global crate cargo-credential-libsecret
Name:           rust-cargo-credential-libsecret
Version:        0.5.10
Release:        1%{?dist}
Summary:        A Cargo credential process that stores tokens with GNOME libsecret.
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/cargo-credential-libsecret
Source0:        https://static.crates.io/crates/cargo-credential-libsecret/cargo-credential-libsecret-%{version}.crate
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
Summary:        A Cargo credential process that stores tokens with GNOME libsecret.
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
%files -n rust-cargo-credential-libsecret-devel -f %{oreon_filedir}/rust-cargo-credential-libsecret-devel.list

%changelog

%autochangelog
