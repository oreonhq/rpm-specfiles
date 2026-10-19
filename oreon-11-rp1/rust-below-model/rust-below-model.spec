%global source0_hash 0602660db608bc70ce133137fd1c914d7531915b07d7785beba45092e9a50a6c
%bcond check 1
%global debug_package %{nil}
%global crate below-model
%global unsupported_arches %{ix86}
Name:           rust-below-model
Version:        0.9.0
Release:        1%{?dist}
Summary:        Model crate for below
License:        Apache-2.0
URL:            https://crates.io/crates/below-model
Source0:        https://static.crates.io/crates/below-model/below-model-%{version}.crate
Patch:          below-model-fix-metadata.diff
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
Summary:        Model crate for below
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%ifnarch %{unsupported_arches}
%cargo_build
%endif
%install
%cargo_install
%if %{with check}
%ifnarch %{unsupported_arches}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%cargo_test
%endif
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-below-model-devel -f %{oreon_filedir}/rust-below-model-devel.list

%changelog

%autochangelog
