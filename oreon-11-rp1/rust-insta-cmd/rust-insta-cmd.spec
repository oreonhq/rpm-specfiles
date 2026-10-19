%global source0_hash ffeeefa927925cced49ccb01bf3e57c9d4cd132df21e576eb9415baeab2d3de6
%bcond check 0
%global debug_package %{nil}
%global cargo_install_bin 0
%global crate insta-cmd
Name:           rust-insta-cmd
Version:        0.6.0
Release:        1%{?dist}
Summary:        Command line extension to the insta testing library for Rust
License:        Apache-2.0
URL:            https://crates.io/crates/insta-cmd
Source0:        https://static.crates.io/crates/insta-cmd/insta-cmd-%{version}.crate
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
Summary:        Command line extension to the insta testing library for Rust
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
%files -n rust-insta-cmd-devel -f %{oreon_filedir}/rust-insta-cmd-devel.list

%changelog

%autochangelog
