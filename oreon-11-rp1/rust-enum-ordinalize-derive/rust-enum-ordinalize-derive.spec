%global source0_hash a65863d15a4ce2888bd2f0f543cc963d3879c3a022c8ee43f6141d479a3ac815
%bcond check 1
%global debug_package %{nil}
%global crate enum-ordinalize-derive
Name:           rust-enum-ordinalize-derive
Version:        4.4.2
Release:        1%{?dist}
Summary:        Enums can get and construct from ordinal values with a procedural macro
License:        MIT
URL:            https://crates.io/crates/enum-ordinalize-derive
Source0:        https://static.crates.io/crates/enum-ordinalize-derive/enum-ordinalize-derive-%{version}.crate
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
Summary:        Enums can get and construct from ordinal values with a procedural macro
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+traits-devel
Summary:        Enums can get and construct from ordinal values with a procedural macro
BuildArch:      noarch
%description -n %{name}+traits-devel

This package contains library source intended for building other packages which
use the "traits" feature of the "%{crate}" crate.

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
%files -n rust-enum-ordinalize-derive-devel -f %{oreon_filedir}/rust-enum-ordinalize-derive-devel.list

%changelog

%autochangelog
