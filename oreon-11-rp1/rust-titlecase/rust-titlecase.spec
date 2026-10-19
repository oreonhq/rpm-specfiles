%global source0_hash eb567088a91d59b492520c8149e2be5ce10d5deb2d9a383f3378df3259679d40
%bcond check 1
%global debug_package %{nil}
%global cargo_install_bin 0
%global crate titlecase
Name:           rust-titlecase
Version:        3.6.0
Release:        1%{?dist}
Summary:        Capitalize text according to the Daring Fireball style
License:        MIT
URL:            https://crates.io/crates/titlecase
Source0:        https://static.crates.io/crates/titlecase/titlecase-%{version}.crate
Patch:          titlecase-fix-metadata.diff
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
Summary:        Capitalize text according to the Daring Fireball style
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+perf-devel
Summary:        Capitalize text according to the Daring Fireball style
BuildArch:      noarch
%description -n %{name}+perf-devel

This package contains library source intended for building other packages which
use the "perf" feature of the "%{crate}" crate.

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
%files -n rust-titlecase-devel -f %{oreon_filedir}/rust-titlecase-devel.list

%changelog

%autochangelog
