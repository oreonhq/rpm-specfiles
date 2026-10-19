%global source0_hash 7ba18343f71e7f135c56454a7d16e9b11f9a1b86c79f2ebab5cce7582c9a64e9
%bcond check 0
%global debug_package %{nil}
%global crate trycmd
Name:           rust-trycmd
Version:        1.2.1
Release:        1%{?dist}
Summary:        Snapshot testing for a herd of CLI tests
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/trycmd
Source0:        https://static.crates.io/crates/trycmd/trycmd-%{version}.crate
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
Summary:        Snapshot testing for a herd of CLI tests
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+color-devel
Summary:        Snapshot testing for a herd of CLI tests
BuildArch:      noarch
%description -n %{name}+color-devel

This package contains library source intended for building other packages which
use the "color" feature of the "%{crate}" crate.

%package     -n %{name}+color-auto-devel
Summary:        Snapshot testing for a herd of CLI tests
BuildArch:      noarch
%description -n %{name}+color-auto-devel

This package contains library source intended for building other packages which
use the "color-auto" feature of the "%{crate}" crate.

%package     -n %{name}+debug-devel
Summary:        Snapshot testing for a herd of CLI tests
BuildArch:      noarch
%description -n %{name}+debug-devel

This package contains library source intended for building other packages which
use the "debug" feature of the "%{crate}" crate.

%package     -n %{name}+diff-devel
Summary:        Snapshot testing for a herd of CLI tests
BuildArch:      noarch
%description -n %{name}+diff-devel

This package contains library source intended for building other packages which
use the "diff" feature of the "%{crate}" crate.

%package     -n %{name}+examples-devel
Summary:        Snapshot testing for a herd of CLI tests
BuildArch:      noarch
%description -n %{name}+examples-devel

This package contains library source intended for building other packages which
use the "examples" feature of the "%{crate}" crate.

%package     -n %{name}+filesystem-devel
Summary:        Snapshot testing for a herd of CLI tests
BuildArch:      noarch
%description -n %{name}+filesystem-devel

This package contains library source intended for building other packages which
use the "filesystem" feature of the "%{crate}" crate.

%package     -n %{name}+schema-devel
Summary:        Snapshot testing for a herd of CLI tests
BuildArch:      noarch
%description -n %{name}+schema-devel

This package contains library source intended for building other packages which
use the "schema" feature of the "%{crate}" crate.

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
%files -n rust-trycmd-devel -f %{oreon_filedir}/rust-trycmd-devel.list

%changelog

%autochangelog
