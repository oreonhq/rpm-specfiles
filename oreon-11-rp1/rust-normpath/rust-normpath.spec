%global source0_hash b9985ef7269fa99f3b12437bb698381da2428743ab90f20393f399fa14cab21a
%bcond check 0
%global debug_package %{nil}
%global crate normpath
Name:           rust-normpath
Version:        1.5.1
Release:        1%{?dist}
Summary:        More reliable path manipulation
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/normpath
Source0:        https://static.crates.io/crates/normpath/normpath-%{version}.crate
Patch:          normpath-fix-metadata-auto.diff
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

%package     -n %{name}+localization-devel
Summary:        More reliable path manipulation
BuildArch:      noarch
%description -n %{name}+localization-devel

This package contains library source intended for building other packages which
use the "localization" feature of the "%{crate}" crate.

%package     -n %{name}+print_bytes-devel
Summary:        More reliable path manipulation
BuildArch:      noarch
%description -n %{name}+print_bytes-devel

This package contains library source intended for building other packages which
use the "print_bytes" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        More reliable path manipulation
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+uniquote-devel
Summary:        More reliable path manipulation
BuildArch:      noarch
%description -n %{name}+uniquote-devel

This package contains library source intended for building other packages which
use the "uniquote" feature of the "%{crate}" crate.

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
%files -n rust-normpath-devel -f %{oreon_filedir}/rust-normpath-devel.list

%changelog

%autochangelog
