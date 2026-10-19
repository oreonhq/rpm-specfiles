%global source0_hash b57acb10231b9493c8472b20cb57317d0679a49e0bdbee44b3b803a6473af164
%bcond check 0
%global debug_package %{nil}
%global crate which
Name:           rust-which2
Version:        2.0.1
Release:        1%{?dist}
Summary:        A Rust equivalent of Unix command "which". Locate installed execuable...
License:        MIT
URL:            https://crates.io/crates/which
Source0:        https://static.crates.io/crates/which/which-%{version}.crate
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
Summary:        A Rust equivalent of Unix command "which". Locate installed execuable...
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
%files -n rust-which2-devel -f %{oreon_filedir}/rust-which2-devel.list

%changelog

%autochangelog
