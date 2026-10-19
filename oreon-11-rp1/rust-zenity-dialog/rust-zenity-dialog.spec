%global source3_hash 30fefc3a7d6a0041541858293bcbea2dde4caa4c0a5802f996a7f7e8c0085652
%global source2_hash a60eea817514531668d7e00765731449fe14d059d3249e0bc93b36de45f759f2
%global source0_hash e58a030e8e052cb54f6793de1b5e1e1489825704c9ac41b6f06ab25d4bfee118
%bcond check 1
%global debug_package %{nil}
%global crate zenity-dialog
Name:           rust-zenity-dialog
Version:        0.3.6
Release:        1%{?dist}
Summary:        Statically typed wrapper around the Zenity dialog rendering tool for Linux
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/zenity-dialog
Source0:        https://static.crates.io/crates/zenity-dialog/zenity-dialog-%{version}.crate
Source2:        https://github.com/toadslop/zenity-dialog/raw/31157cc353b147f81f84d69cc51fbc14d198d1dd/LICENSE-APACHE
Source3:        https://github.com/toadslop/zenity-dialog/raw/31157cc353b147f81f84d69cc51fbc14d198d1dd/LICENSE-MIT
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
Summary:        Statically typed wrapper around the Zenity dialog rendering tool for Linux
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+calendar-devel
Summary:        Statically typed wrapper around the Zenity dialog rendering tool for Linux
BuildArch:      noarch
%description -n %{name}+calendar-devel

This package contains library source intended for building other packages which
use the "calendar" feature of the "%{crate}" crate.

%package     -n %{name}+chrono-devel
Summary:        Statically typed wrapper around the Zenity dialog rendering tool for Linux
BuildArch:      noarch
%description -n %{name}+chrono-devel

This package contains library source intended for building other packages which
use the "chrono" feature of the "%{crate}" crate.

%package     -n %{name}+entry-devel
Summary:        Statically typed wrapper around the Zenity dialog rendering tool for Linux
BuildArch:      noarch
%description -n %{name}+entry-devel

This package contains library source intended for building other packages which
use the "entry" feature of the "%{crate}" crate.

%package     -n %{name}+error-devel
Summary:        Statically typed wrapper around the Zenity dialog rendering tool for Linux
BuildArch:      noarch
%description -n %{name}+error-devel

This package contains library source intended for building other packages which
use the "error" feature of the "%{crate}" crate.

%package     -n %{name}+info-devel
Summary:        Statically typed wrapper around the Zenity dialog rendering tool for Linux
BuildArch:      noarch
%description -n %{name}+info-devel

This package contains library source intended for building other packages which
use the "info" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
cp -p %SOURCE2 %SOURCE3 .
%oreon_vendor_cargo
%build

%cargo_build
%install
%cargo_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test -- --lib
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-zenity-dialog-devel -f %{oreon_filedir}/rust-zenity-dialog-devel.list

%changelog

%autochangelog
