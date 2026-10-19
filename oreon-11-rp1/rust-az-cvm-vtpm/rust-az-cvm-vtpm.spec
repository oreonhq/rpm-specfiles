%global source0_hash 2044bf018f8ff574c82c5c7d672716ff0076b2be07ed6f91afd1ae41b1f8889d
%bcond check 1
%global debug_package %{nil}
%global crate az-cvm-vtpm
%global supported_arches x86_64
Name:           rust-az-cvm-vtpm
Version:        0.8.2
Release:        1%{?dist}
Summary:        Package with shared code for Azure Confidential VMs
License:        MIT
URL:            https://crates.io/crates/az-cvm-vtpm
Source0:        https://static.crates.io/crates/az-cvm-vtpm/az-cvm-vtpm-%{version}.crate
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
Summary:        Package with shared code for Azure Confidential VMs
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+attester-devel
Summary:        Package with shared code for Azure Confidential VMs
BuildArch:      noarch
%description -n %{name}+attester-devel

This package contains library source intended for building other packages which
use the "attester" feature of the "%{crate}" crate.

%package     -n %{name}+openssl-devel
Summary:        Package with shared code for Azure Confidential VMs
BuildArch:      noarch
%description -n %{name}+openssl-devel

This package contains library source intended for building other packages which
use the "openssl" feature of the "%{crate}" crate.

%package     -n %{name}+tpm-devel
Summary:        Package with shared code for Azure Confidential VMs
BuildArch:      noarch
%description -n %{name}+tpm-devel

This package contains library source intended for building other packages which
use the "tpm" feature of the "%{crate}" crate.

%package     -n %{name}+tss-esapi-devel
Summary:        Package with shared code for Azure Confidential VMs
BuildArch:      noarch
%description -n %{name}+tss-esapi-devel

This package contains library source intended for building other packages which
use the "tss-esapi" feature of the "%{crate}" crate.

%package     -n %{name}+verifier-devel
Summary:        Package with shared code for Azure Confidential VMs
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

%cargo_test
%endif
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-az-cvm-vtpm-devel -f %{oreon_filedir}/rust-az-cvm-vtpm-devel.list

%changelog

%autochangelog
