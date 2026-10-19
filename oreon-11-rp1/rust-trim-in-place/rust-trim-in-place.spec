%global source0_hash 343e926fc669bc8cde4fa3129ab681c63671bae288b1f1081ceee6d9d37904fc
%bcond check 1
%global debug_package %{nil}
%global crate trim-in-place
Name:           rust-trim-in-place
Version:        0.1.7
Release:        1%{?dist}
Summary:        In-place trimming strings
License:        MIT
URL:            https://crates.io/crates/trim-in-place
Source0:        https://static.crates.io/crates/trim-in-place/trim-in-place-%{version}.crate
Patch:          trim-in-place-fix-metadata.diff
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
Summary:        In-place trimming strings
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
%files -n rust-trim-in-place-devel -f %{oreon_filedir}/rust-trim-in-place-devel.list

%changelog

%autochangelog
