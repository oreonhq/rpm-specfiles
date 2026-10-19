%global source0_hash 2de38e4c0f6b255a4979588f58d77bf45e481c4cbe46b7858150bbe129f1a827
%bcond check 0
%global debug_package %{nil}
%global crate aws-nitro-enclaves-image-format
Name:           rust-aws-nitro-enclaves-image-format
Version:        0.7.0
Release:        1%{?dist}
Summary:        Library provides the definition of the enclave image format
License:        Apache-2.0
URL:            https://crates.io/crates/aws-nitro-enclaves-image-format
Source0:        https://static.crates.io/crates/aws-nitro-enclaves-image-format/aws-nitro-enclaves-image-format-%{version}.crate
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
Summary:        Library provides the definition of the enclave image format
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
%files -n rust-aws-nitro-enclaves-image-format-devel -f %{oreon_filedir}/rust-aws-nitro-enclaves-image-format-devel.list

%changelog

%autochangelog
