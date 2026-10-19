%global source0_hash 351339c4d45e6bdf2defef3ef1ce0b153810bd59b171b92b6a42e7bb0f32a4ad
%bcond check 0
%global debug_package %{nil}
%global crate openssh-keys
Name:           rust-openssh-keys
Version:        0.6.5
Release:        1%{?dist}
Summary:        read and write OpenSSH public keys
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/openssh-keys
Source0:        https://static.crates.io/crates/openssh-keys/openssh-keys-%{version}.crate
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
Summary:        read and write OpenSSH public keys
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
%files -n rust-openssh-keys-devel -f %{oreon_filedir}/rust-openssh-keys-devel.list

%changelog

%autochangelog
