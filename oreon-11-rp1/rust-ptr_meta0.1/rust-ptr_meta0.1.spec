%global source0_hash 0738ccf7ea06b608c10564b31debd4f5bc5e197fc8bfe088f68ae5ce81e7a4f1
%bcond check 0
%global debug_package %{nil}
%global crate ptr_meta
Name:           rust-ptr_meta0.1
Version:        0.1.4
Release:        1%{?dist}
Summary:        Radioactive stabilization of the ptr_meta rfc
License:        MIT
URL:            https://crates.io/crates/ptr_meta
Source0:        https://static.crates.io/crates/ptr_meta/ptr_meta-%{version}.crate
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
Summary:        Radioactive stabilization of the ptr_meta rfc
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Radioactive stabilization of the ptr_meta rfc
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

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
%files -n rust-ptr_meta0.1-devel -f %{oreon_filedir}/rust-ptr_meta0.1-devel.list

%changelog

%autochangelog
