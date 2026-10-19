%global source0_hash 04849677b3c0704d4593d89940cde0dc0caad2202bf9fb29352e153782b91ff8
%bcond check 1
%global debug_package %{nil}
%global cargo_install_bin 0
%global crate az-tdx-vtpm
%global supported_arches x86_64
Name:           rust-az-tdx-vtpm
Version:        0.7.4
Release:        1%{?dist}
Summary:        VTPM based TDX attestation for Azure Confidential VMs
License:        MIT
URL:            https://crates.io/crates/az-tdx-vtpm
Source0:        https://static.crates.io/crates/az-tdx-vtpm/az-tdx-vtpm-%{version}.crate
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
Summary:        VTPM based TDX attestation for Azure Confidential VMs
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+attester-devel
Summary:        VTPM based TDX attestation for Azure Confidential VMs
BuildArch:      noarch
%description -n %{name}+attester-devel

This package contains library source intended for building other packages which
use the "attester" feature of the "%{crate}" crate.

%package     -n %{name}+verifier-devel
Summary:        VTPM based TDX attestation for Azure Confidential VMs
BuildArch:      noarch
%description -n %{name}+verifier-devel

This package contains library source intended for building other packages which
use the "verifier" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%ifarch %{supported_arches}
%cargo_build
%endif
%install
%cargo_install
%if %{with check}
%ifarch %{supported_arches}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

mkdir -p ../test
cp test/* ../test/
%cargo_test
%endif
rm -rf ../test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-az-tdx-vtpm-devel -f %{oreon_filedir}/rust-az-tdx-vtpm-devel.list

%changelog

%autochangelog
