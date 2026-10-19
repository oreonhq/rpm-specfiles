%global source0_hash cd62e6b5e86ea8eeeb8db1de02880a6abc01a397b2ebb64b5d74ac255318f5cb
%bcond check 1
%global debug_package %{nil}
%global crate if_chain
Name:           rust-if_chain
Version:        1.0.3
Release:        1%{?dist}
Summary:        Macro for writing nested if let expressions
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/if_chain
Source0:        https://static.crates.io/crates/if_chain/if_chain-%{version}.crate
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
Summary:        Macro for writing nested if let expressions
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
%files -n rust-if_chain-devel -f %{oreon_filedir}/rust-if_chain-devel.list

%changelog

%autochangelog
