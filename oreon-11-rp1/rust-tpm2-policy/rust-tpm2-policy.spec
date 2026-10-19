%global source0_hash 07bd130084fd4b1d87e7d24a1334eb31136e88fea83b0ab08ac05e1d9e033a2a
%bcond check 1
%global debug_package %{nil}
%global crate tpm2-policy
Name:           rust-%{crate}
Version:        0.6.0
Release:        1%{?dist}
Summary:        Specify and send TPM2 policies to satisfy object authorization
License:        EUPL-1.2
URL:            https://crates.io/crates/tpm2-policy
Source0:        https://static.crates.io/crates/tpm2-policy/tpm2-policy-%{version}.crate
Patch0:         tpm2-policy-fix-metadata.diff
ExclusiveArch:  %{rust_arches}
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
Summary:        Specify and send TPM2 policies to satisfy object authorization
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build -a
%install
%cargo_install -a
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test -a
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-tpm2-policy-devel -f %{oreon_filedir}/rust-tpm2-policy-devel.list

%changelog

%autochangelog
