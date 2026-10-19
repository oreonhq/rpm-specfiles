%global source0_hash 221de5f6ef11b9be9d59b330c5b81799b3e7c51b18af84c1f235ef88998b00e1
%bcond check 1
%global debug_package %{nil}
%global crate proc-maps
Name:           rust-proc-maps
Version:        0.5.0
Release:        1%{?dist}
Summary:        Helper crate for getting virtual memory maps from processes
License:        MIT
URL:            https://crates.io/crates/proc-maps
Source0:        https://static.crates.io/crates/proc-maps/proc-maps-%{version}.crate
Patch:          proc-maps-fix-metadata-auto.diff
Patch:          proc-maps-fix-metadata.diff
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
Summary:        Helper crate for getting virtual memory maps from processes
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+generate-bindings-devel
Summary:        Helper crate for getting virtual memory maps from processes
BuildArch:      noarch
%description -n %{name}+generate-bindings-devel

This package contains library source intended for building other packages which
use the "generate-bindings" feature of the "%{crate}" crate.

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
%files -n rust-proc-maps-devel -f %{oreon_filedir}/rust-proc-maps-devel.list

%changelog

%autochangelog
