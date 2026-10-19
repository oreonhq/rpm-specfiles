%global source0_hash feda4b74ded511c6d8543db00166f70f572ca7e5eb72f4817bf08628b5bbc1f4
%bcond check 0
%global debug_package %{nil}
%global crate openssl-kdf
Name:           rust-openssl-kdf
Version:        0.4.2
Release:        1%{?dist}
Summary:        OpenSSL KDF function abstraction
License:        MIT
URL:            https://crates.io/crates/openssl-kdf
Source0:        https://static.crates.io/crates/openssl-kdf/openssl-kdf-%{version}.crate
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
Summary:        OpenSSL KDF function abstraction
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+allow_custom-devel
Summary:        OpenSSL KDF function abstraction
BuildArch:      noarch
%description -n %{name}+allow_custom-devel

This package contains library source intended for building other packages which
use the "allow_custom" feature of the "%{crate}" crate.

%package     -n %{name}+deny_custom-devel
Summary:        OpenSSL KDF function abstraction
BuildArch:      noarch
%description -n %{name}+deny_custom-devel

This package contains library source intended for building other packages which
use the "deny_custom" feature of the "%{crate}" crate.

%package     -n %{name}+force_custom-devel
Summary:        OpenSSL KDF function abstraction
BuildArch:      noarch
%description -n %{name}+force_custom-devel

This package contains library source intended for building other packages which
use the "force_custom" feature of the "%{crate}" crate.

%package     -n %{name}+warn_custom-devel
Summary:        OpenSSL KDF function abstraction
BuildArch:      noarch
%description -n %{name}+warn_custom-devel

This package contains library source intended for building other packages which
use the "warn_custom" feature of the "%{crate}" crate.

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
%files -n rust-openssl-kdf-devel -f %{oreon_filedir}/rust-openssl-kdf-devel.list

%changelog

%autochangelog
