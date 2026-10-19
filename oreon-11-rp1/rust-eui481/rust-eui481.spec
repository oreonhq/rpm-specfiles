%global source0_hash 887418ac5e8d57c2e66e04bdc2fe15f9a5407be20b54a82c86bd0e368b709701
%bcond check 0
%global debug_package %{nil}
%global crate eui48
Name:           rust-eui481
Version:        1.1.0
Release:        1%{?dist}
Summary:        A library to generate and parse IEEE EUI-48 and EUI-64, also known as...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/eui48
Source0:        https://static.crates.io/crates/eui48/eui48-%{version}.crate
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
Summary:        A library to generate and parse IEEE EUI-48 and EUI-64, also known as...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+disp_hexstring-devel
Summary:        A library to generate and parse IEEE EUI-48 and EUI-64, also known as...
BuildArch:      noarch
%description -n %{name}+disp_hexstring-devel

This package contains library source intended for building other packages which
use the "disp_hexstring" feature of the "%{crate}" crate.

%package     -n %{name}+rustc-serialize-devel
Summary:        A library to generate and parse IEEE EUI-48 and EUI-64, also known as...
BuildArch:      noarch
%description -n %{name}+rustc-serialize-devel

This package contains library source intended for building other packages which
use the "rustc-serialize" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        A library to generate and parse IEEE EUI-48 and EUI-64, also known as...
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+serde_bytes-devel
Summary:        A library to generate and parse IEEE EUI-48 and EUI-64, also known as...
BuildArch:      noarch
%description -n %{name}+serde_bytes-devel

This package contains library source intended for building other packages which
use the "serde_bytes" feature of the "%{crate}" crate.

%package     -n %{name}+serde_json-devel
Summary:        A library to generate and parse IEEE EUI-48 and EUI-64, also known as...
BuildArch:      noarch
%description -n %{name}+serde_json-devel

This package contains library source intended for building other packages which
use the "serde_json" feature of the "%{crate}" crate.

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
%files -n rust-eui481-devel -f %{oreon_filedir}/rust-eui481-devel.list

%changelog

%autochangelog
