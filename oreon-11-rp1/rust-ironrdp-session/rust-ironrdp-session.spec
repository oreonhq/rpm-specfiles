%global source0_hash 9a8283108c85814152cc8308b4a406d38ee00a6a472d2f3d9cad265266fb693a
%bcond check 1
%global debug_package %{nil}
%global crate ironrdp-session
Name:           rust-ironrdp-session
Version:        0.5.0
Release:        1%{?dist}
Summary:        State machines to drive an RDP session
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/ironrdp-session
Source0:        https://static.crates.io/crates/ironrdp-session/ironrdp-session-%{version}.crate
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
Summary:        State machines to drive an RDP session
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
%files -n rust-ironrdp-session-devel -f %{oreon_filedir}/rust-ironrdp-session-devel.list

%changelog

%autochangelog
