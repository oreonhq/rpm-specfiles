%global source2_hash 3f3d9e0024b1921b067d6f7f88deb4a60cbe7a78e76c64e3f1d7fc3b779b9d04
%global source0_hash 66534846dec7a11d7c50a74b7cdb208b9a581cad890b7866430d438455847c85
%bcond check 0
%global debug_package %{nil}
%global crate x509-certificate
Name:           rust-x509-certificate
Version:        0.23.1
Release:        1%{?dist}
Summary:        X.509 certificate parser and utility functionality
License:        MPL-2.0
URL:            https://crates.io/crates/x509-certificate
Source0:        https://static.crates.io/crates/x509-certificate/x509-certificate-%{version}.crate
Source2:        https://github.com/indygreg/cryptography-rs/raw/cfaafe05892ce5c617dcac593a9224613bf88a0e/LICENSE
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
Summary:        X.509 certificate parser and utility functionality
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+test-devel
Summary:        X.509 certificate parser and utility functionality
BuildArch:      noarch
%description -n %{name}+test-devel

This package contains library source intended for building other packages which
use the "test" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
cp -p %SOURCE2 .
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
%files -n rust-x509-certificate-devel -f %{oreon_filedir}/rust-x509-certificate-devel.list

%changelog

%autochangelog
