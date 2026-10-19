%global source0_hash bea12d80384007fe321eb6b36c9225be9559c655fd581458a6a1386c1774d729
%bcond check 1
%global debug_package %{nil}
%global crate ironrdp-async
Name:           rust-ironrdp-async
Version:        0.10.0
Release:        1%{?dist}
Summary:        Futures wrapping the IronRDP state machines conveniently
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/ironrdp-async
Source0:        https://static.crates.io/crates/ironrdp-async/ironrdp-async-%{version}.crate
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
Summary:        Futures wrapping the IronRDP state machines conveniently
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
%files -n rust-ironrdp-async-devel -f %{oreon_filedir}/rust-ironrdp-async-devel.list

%changelog

%autochangelog
