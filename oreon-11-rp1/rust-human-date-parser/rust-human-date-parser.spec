%global source0_hash 406f83c56de4b2c9183be52ae9a4fefa22c0e0c3d3d7ef80be26eaee11c7110e
%bcond check 1
%global debug_package %{nil}
%global crate human-date-parser
Name:           rust-human-date-parser
Version:        0.3.1
Release:        1%{?dist}
Summary:        Parses strings that express dates in a human way into ones usable by code
License:        MIT
URL:            https://crates.io/crates/human-date-parser
Source0:        https://static.crates.io/crates/human-date-parser/human-date-parser-%{version}.crate
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
Summary:        Parses strings that express dates in a human way into ones usable by code
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
%files -n rust-human-date-parser-devel -f %{oreon_filedir}/rust-human-date-parser-devel.list

%changelog

%autochangelog
