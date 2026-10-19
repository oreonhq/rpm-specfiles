%global source0_hash 26b52a9543ae338f279b96b0b9fed9c8093744685043739079ce85cd58f289a6
%bcond check 1
%global debug_package %{nil}
%global crate cbc
Name:           rust-cbc0.1
Version:        0.1.2
Release:        1%{?dist}
Summary:        Cipher Block Chaining (CBC) block cipher mode of operation
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/cbc
Source0:        https://static.crates.io/crates/cbc/cbc-%{version}.crate
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
Summary:        Cipher Block Chaining (CBC) block cipher mode of operation
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Cipher Block Chaining (CBC) block cipher mode of operation
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+block-padding-devel
Summary:        Cipher Block Chaining (CBC) block cipher mode of operation
BuildArch:      noarch
%description -n %{name}+block-padding-devel

This package contains library source intended for building other packages which
use the "block-padding" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Cipher Block Chaining (CBC) block cipher mode of operation
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+zeroize-devel
Summary:        Cipher Block Chaining (CBC) block cipher mode of operation
BuildArch:      noarch
%description -n %{name}+zeroize-devel

This package contains library source intended for building other packages which
use the "zeroize" feature of the "%{crate}" crate.

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
%files -n rust-cbc0.1-devel -f %{oreon_filedir}/rust-cbc0.1-devel.list

%changelog

%autochangelog
