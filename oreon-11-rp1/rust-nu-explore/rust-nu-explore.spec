%global source0_hash fe0dee023ff0befb5df4d3a3b720e252172079a82add53ebdfab7ea04f967383
%bcond check 1
%global debug_package %{nil}
%global crate nu-explore
Name:           rust-nu-explore
Version:        0.115.1
Release:        1%{?dist}
Summary:        Nushell table pager
License:        MIT
URL:            https://crates.io/crates/nu-explore
Source0:        https://static.crates.io/crates/nu-explore/nu-explore-%{version}.crate
Patch:          nu-explore-fix-metadata.diff
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
Summary:        Nushell table pager
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
%files -n rust-nu-explore-devel -f %{oreon_filedir}/rust-nu-explore-devel.list

%changelog

%autochangelog
