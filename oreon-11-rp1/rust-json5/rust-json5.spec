%global source0_hash 96b0db21af676c1ce64250b5f40f3ce2cf27e4e47cb91ed91eb6fe9350b430c1
%bcond check 0
%global debug_package %{nil}
%global crate json5
Name:           rust-json5
Version:        0.4.1
Release:        1%{?dist}
Summary:        Rust JSON5 serializer and deserializer which speaks Serde
License:        ISC
URL:            https://crates.io/crates/json5
Source0:        https://static.crates.io/crates/json5/json5-%{version}.crate
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
Summary:        Rust JSON5 serializer and deserializer which speaks Serde
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
%files -n rust-json5-devel -f %{oreon_filedir}/rust-json5-devel.list

%changelog

%autochangelog
