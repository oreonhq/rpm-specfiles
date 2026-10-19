%global source0_hash 420c6c161b5d6883d8195584a802b114af6c884ed56d937d994e30f7f81d54ec
%bcond check 0
%global debug_package %{nil}
%global crate sev
Name:           rust-sev
Version:        6.3.1
Release:        1%{?dist}
Summary:        Library for AMD SEV
License:        Apache-2.0
URL:            https://crates.io/crates/sev
Source0:        https://static.crates.io/crates/sev/sev-%{version}.crate
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
Summary:        Library for AMD SEV
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+crypto_nossl-devel
Summary:        Library for AMD SEV
BuildArch:      noarch
%description -n %{name}+crypto_nossl-devel

This package contains library source intended for building other packages which
use the "crypto_nossl" feature of the "%{crate}" crate.

%package     -n %{name}+dangerous_hw_tests-devel
Summary:        Library for AMD SEV
BuildArch:      noarch
%description -n %{name}+dangerous_hw_tests-devel

This package contains library source intended for building other packages which
use the "dangerous_hw_tests" feature of the "%{crate}" crate.

%package     -n %{name}+hw_tests-devel
Summary:        Library for AMD SEV
BuildArch:      noarch
%description -n %{name}+hw_tests-devel

This package contains library source intended for building other packages which
use the "hw_tests" feature of the "%{crate}" crate.

%package     -n %{name}+openssl-devel
Summary:        Library for AMD SEV
BuildArch:      noarch
%description -n %{name}+openssl-devel

This package contains library source intended for building other packages which
use the "openssl" feature of the "%{crate}" crate.

%package     -n %{name}+p384-devel
Summary:        Library for AMD SEV
BuildArch:      noarch
%description -n %{name}+p384-devel

This package contains library source intended for building other packages which
use the "p384" feature of the "%{crate}" crate.

%package     -n %{name}+rdrand-devel
Summary:        Library for AMD SEV
BuildArch:      noarch
%description -n %{name}+rdrand-devel

This package contains library source intended for building other packages which
use the "rdrand" feature of the "%{crate}" crate.

%package     -n %{name}+reqwest-devel
Summary:        Library for AMD SEV
BuildArch:      noarch
%description -n %{name}+reqwest-devel

This package contains library source intended for building other packages which
use the "reqwest" feature of the "%{crate}" crate.

%package     -n %{name}+rsa-devel
Summary:        Library for AMD SEV
BuildArch:      noarch
%description -n %{name}+rsa-devel

This package contains library source intended for building other packages which
use the "rsa" feature of the "%{crate}" crate.

%package     -n %{name}+sev-devel
Summary:        Library for AMD SEV
BuildArch:      noarch
%description -n %{name}+sev-devel

This package contains library source intended for building other packages which
use the "sev" feature of the "%{crate}" crate.

%package     -n %{name}+sha2-devel
Summary:        Library for AMD SEV
BuildArch:      noarch
%description -n %{name}+sha2-devel

This package contains library source intended for building other packages which
use the "sha2" feature of the "%{crate}" crate.

%package     -n %{name}+snp-devel
Summary:        Library for AMD SEV
BuildArch:      noarch
%description -n %{name}+snp-devel

This package contains library source intended for building other packages which
use the "snp" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-devel
Summary:        Library for AMD SEV
BuildArch:      noarch
%description -n %{name}+tokio-devel

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

%package     -n %{name}+x509-cert-devel
Summary:        Library for AMD SEV
BuildArch:      noarch
%description -n %{name}+x509-cert-devel

This package contains library source intended for building other packages which
use the "x509-cert" feature of the "%{crate}" crate.

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
%files -n rust-sev-devel -f %{oreon_filedir}/rust-sev-devel.list

%changelog

%autochangelog
