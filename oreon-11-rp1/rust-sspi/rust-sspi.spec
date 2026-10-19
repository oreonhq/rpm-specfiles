%global source0_hash c0f37d923437132ca241de0f792298f2443a85e95fd64c19585944cbf8805daf
%bcond check 1
%global debug_package %{nil}
%global crate sspi
Name:           rust-sspi
Version:        0.22.0
Release:        1%{?dist}
Summary:        Rust implementation of the Security Support Provider Interface
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/sspi
Source0:        https://static.crates.io/crates/sspi/sspi-%{version}.crate
Patch:          sspi-fix-metadata-auto.diff
Patch:          sspi-fix-metadata.diff
Patch10:        sspi-0.16.1-whoami2.patch
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
Summary:        Rust implementation of the Security Support Provider Interface
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+__install-crypto-provider-devel
Summary:        Rust implementation of the Security Support Provider Interface
BuildArch:      noarch
%description -n %{name}+__install-crypto-provider-devel

This package contains library source intended for building other packages which
use the "__install-crypto-provider" feature of the "%{crate}" crate.

%package     -n %{name}+__rustls-used-devel
Summary:        Rust implementation of the Security Support Provider Interface
BuildArch:      noarch
%description -n %{name}+__rustls-used-devel

This package contains library source intended for building other packages which
use the "__rustls-used" feature of the "%{crate}" crate.

%package     -n %{name}+dns_resolver-devel
Summary:        Rust implementation of the Security Support Provider Interface
BuildArch:      noarch
%description -n %{name}+dns_resolver-devel

This package contains library source intended for building other packages which
use the "dns_resolver" feature of the "%{crate}" crate.

%package     -n %{name}+network_client-devel
Summary:        Rust implementation of the Security Support Provider Interface
BuildArch:      noarch
%description -n %{name}+network_client-devel

This package contains library source intended for building other packages which
use the "network_client" feature of the "%{crate}" crate.

%package     -n %{name}+ring-devel
Summary:        Rust implementation of the Security Support Provider Interface
BuildArch:      noarch
%description -n %{name}+ring-devel

This package contains library source intended for building other packages which
use the "ring" feature of the "%{crate}" crate.

%package     -n %{name}+tsssp-devel
Summary:        Rust implementation of the Security Support Provider Interface
BuildArch:      noarch
%description -n %{name}+tsssp-devel

This package contains library source intended for building other packages which
use the "tsssp" feature of the "%{crate}" crate.

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
%files -n rust-sspi-devel -f %{oreon_filedir}/rust-sspi-devel.list

%changelog

%autochangelog
