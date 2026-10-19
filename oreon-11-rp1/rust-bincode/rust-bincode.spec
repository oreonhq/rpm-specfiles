%global source0_hash b1f45e9417d87227c7a56d22e471c6206462cba514c7590c09aff4cf6d1ddcad
%bcond check 1
%global debug_package %{nil}
%global crate bincode
Name:           rust-bincode
Version:        1.3.3
Release:        1%{?dist}
Summary:        A binary serialization / deserialization strategy that uses Serde
License:        MIT
URL:            https://crates.io/crates/bincode
Source0:        https://static.crates.io/crates/bincode/bincode-%{version}.crate
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
Summary:        A binary serialization / deserialization strategy that uses Serde
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+i128-devel
Summary:        A binary serialization / deserialization strategy that uses Serde
BuildArch:      noarch
%description -n %{name}+i128-devel

This package contains library source intended for building other packages which
use the "i128" feature of the "%{crate}" crate.

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
%files -n rust-bincode-devel -f %{oreon_filedir}/rust-bincode-devel.list

%changelog

%autochangelog
