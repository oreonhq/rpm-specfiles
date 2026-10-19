%global source0_hash a464143cc82dedcdc3928737445362466b7674b5db4e2eb8e869846d6d84f4f6
%bcond check 1
%global debug_package %{nil}
%global crate argh_shared
Name:           rust-argh_shared
Version:        0.1.13
Release:        1%{?dist}
Summary:        Derive-based argument parsing optimized for code size
License:        BSD-3-Clause
URL:            https://crates.io/crates/argh_shared
Source0:        https://static.crates.io/crates/argh_shared/argh_shared-%{version}.crate
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
Summary:        Derive-based argument parsing optimized for code size
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Derive-based argument parsing optimized for code size
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

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
%files -n rust-argh_shared-devel -f %{oreon_filedir}/rust-argh_shared-devel.list

%changelog

%autochangelog
