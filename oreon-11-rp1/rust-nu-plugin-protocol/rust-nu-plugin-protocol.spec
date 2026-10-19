%global source0_hash 8286126f53e1cec47e02d422474bb57e743ab2aa03f37b1c78eeb5b1e0b40cec
%bcond check 0
%global debug_package %{nil}
%global crate nu-plugin-protocol
Name:           rust-nu-plugin-protocol
Version:        0.99.1
Release:        1%{?dist}
Summary:        Protocol type definitions for Nushell plugins
License:        MIT
URL:            https://crates.io/crates/nu-plugin-protocol
Source0:        https://static.crates.io/crates/nu-plugin-protocol/nu-plugin-protocol-%{version}.crate
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
Summary:        Protocol type definitions for Nushell plugins
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+local-socket-devel
Summary:        Protocol type definitions for Nushell plugins
BuildArch:      noarch
%description -n %{name}+local-socket-devel

This package contains library source intended for building other packages which
use the "local-socket" feature of the "%{crate}" crate.

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
%files -n rust-nu-plugin-protocol-devel -f %{oreon_filedir}/rust-nu-plugin-protocol-devel.list

%changelog

%autochangelog
