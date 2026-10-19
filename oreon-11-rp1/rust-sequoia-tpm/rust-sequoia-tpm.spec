%global source0_hash 332f347252752709faa136ea0d2896c734e960630fe7b342151561dd6751d858
%bcond check 0
%global debug_package %{nil}
%global crate sequoia-tpm
Name:           rust-sequoia-tpm
Version:        0.1.1
Release:        1%{?dist}
Summary:        Machinery for working with TPM from Sequoia
License:        LGPL-2.0-or-later AND Apache-2.0
URL:            https://crates.io/crates/sequoia-tpm
Source0:        https://static.crates.io/crates/sequoia-tpm/sequoia-tpm-%{version}.crate
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
Summary:        Machinery for working with TPM from Sequoia
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
%files -n rust-sequoia-tpm-devel -f %{oreon_filedir}/rust-sequoia-tpm-devel.list

%changelog

%autochangelog
