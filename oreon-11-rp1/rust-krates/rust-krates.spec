%global source0_hash c432bb7d7a968a338f6c7cbd8782f38ffd87a793ff06c3a20257f45e1d003f6d
%bcond check 1
%global debug_package %{nil}
%global crate krates
Name:           rust-krates
Version:        0.20.0
Release:        1%{?dist}
Summary:        Create graphs of crates gathered from cargo metadata
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/krates
Source0:        https://static.crates.io/crates/krates/krates-%{version}.crate
Patch:          krates-fix-metadata.diff
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
Summary:        Create graphs of crates gathered from cargo metadata
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+metadata-devel
Summary:        Create graphs of crates gathered from cargo metadata
BuildArch:      noarch
%description -n %{name}+metadata-devel

This package contains library source intended for building other packages which
use the "metadata" feature of the "%{crate}" crate.

%package     -n %{name}+serialize-devel
Summary:        Create graphs of crates gathered from cargo metadata
BuildArch:      noarch
%description -n %{name}+serialize-devel

This package contains library source intended for building other packages which
use the "serialize" feature of the "%{crate}" crate.

%package     -n %{name}+targets-devel
Summary:        Create graphs of crates gathered from cargo metadata
BuildArch:      noarch
%description -n %{name}+targets-devel

This package contains library source intended for building other packages which
use the "targets" feature of the "%{crate}" crate.

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
%files -n rust-krates-devel -f %{oreon_filedir}/rust-krates-devel.list

%changelog

%autochangelog
