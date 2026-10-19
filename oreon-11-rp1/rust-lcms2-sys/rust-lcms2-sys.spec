%global source0_hash 593265f9a3172180024fb62580ee31348f31be924b19416da174ebb7fb623d2e
%bcond check 0
%global debug_package %{nil}
%global crate lcms2-sys
Name:           rust-lcms2-sys
Version:        4.0.5
Release:        1%{?dist}
Summary:        Bindings for liblcms2
License:        MIT
URL:            https://crates.io/crates/lcms2-sys
Source0:        https://static.crates.io/crates/lcms2-sys/lcms2-sys-%{version}.crate
Patch:          lcms2-sys-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  lcms2-devel
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       lcms2-devel
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Bindings for liblcms2
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+cc-devel
Summary:        Bindings for liblcms2
BuildArch:      noarch
%description -n %{name}+cc-devel

This package contains library source intended for building other packages which
use the "cc" feature of the "%{crate}" crate.

%package     -n %{name}+dynamic-devel
Summary:        Bindings for liblcms2
BuildArch:      noarch
%description -n %{name}+dynamic-devel

This package contains library source intended for building other packages which
use the "dynamic" feature of the "%{crate}" crate.

%package     -n %{name}+lcms2-strict-cgats-devel
Summary:        Bindings for liblcms2
BuildArch:      noarch
%description -n %{name}+lcms2-strict-cgats-devel

This package contains library source intended for building other packages which
use the "lcms2-strict-cgats" feature of the "%{crate}" crate.

%package     -n %{name}+parallel-devel
Summary:        Bindings for liblcms2
BuildArch:      noarch
%description -n %{name}+parallel-devel

This package contains library source intended for building other packages which
use the "parallel" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
cp -p vendor/LICENSE .
rm -r vendor/
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
%files -n rust-lcms2-sys-devel -f %{oreon_filedir}/rust-lcms2-sys-devel.list

%changelog

%autochangelog
