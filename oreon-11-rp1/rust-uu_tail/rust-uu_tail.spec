%global source0_hash 88cb366f24aecb51aa9b03c2ae8b40538aa5081351822a6dfec883f95cc744d3
%bcond check 1
%global debug_package %{nil}
%global cargo_install_bin 0
%global crate uu_tail
Name:           rust-uu_tail
Version:        0.7.0
Release:        1%{?dist}
Summary:        tail ~ (uutils) display the last lines of input
License:        MIT
URL:            https://crates.io/crates/uu_tail
Source0:        https://static.crates.io/crates/uu_tail/uu_tail-%{version}.crate
Patch:          uu_tail-fix-metadata-auto.diff
Patch:          uu_tail-fix-metadata.diff
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
Summary:        tail ~ (uutils) display the last lines of input
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
%files -n rust-uu_tail-devel -f %{oreon_filedir}/rust-uu_tail-devel.list

%changelog

%autochangelog
