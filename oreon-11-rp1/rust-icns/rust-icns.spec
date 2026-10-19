%global source0_hash 467efeb2c1e570cebb9863f9173447f8fe92303d66adc97cb89ac824b60e7a0f
%bcond check 0
%global debug_package %{nil}
%global crate icns
Name:           rust-icns
Version:        0.4.0
Release:        1%{?dist}
Summary:        Library for encoding/decoding Apple Icon Image (.icns) files
License:        MIT
URL:            https://crates.io/crates/icns
Source0:        https://static.crates.io/crates/icns/icns-%{version}.crate
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
Summary:        Library for encoding/decoding Apple Icon Image (.icns) files
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+hayro-jpeg2000-devel
Summary:        Library for encoding/decoding Apple Icon Image (.icns) files
BuildArch:      noarch
%description -n %{name}+hayro-jpeg2000-devel

This package contains library source intended for building other packages which
use the "hayro-jpeg2000" feature of the "%{crate}" crate.

%package     -n %{name}+jp2io-devel
Summary:        Library for encoding/decoding Apple Icon Image (.icns) files
BuildArch:      noarch
%description -n %{name}+jp2io-devel

This package contains library source intended for building other packages which
use the "jp2io" feature of the "%{crate}" crate.

%package     -n %{name}+png-devel
Summary:        Library for encoding/decoding Apple Icon Image (.icns) files
BuildArch:      noarch
%description -n %{name}+png-devel

This package contains library source intended for building other packages which
use the "png" feature of the "%{crate}" crate.

%package     -n %{name}+pngio-devel
Summary:        Library for encoding/decoding Apple Icon Image (.icns) files
BuildArch:      noarch
%description -n %{name}+pngio-devel

This package contains library source intended for building other packages which
use the "pngio" feature of the "%{crate}" crate.

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
%files -n rust-icns-devel -f %{oreon_filedir}/rust-icns-devel.list

%changelog

%autochangelog
