%global source0_hash d9f0c14694cbd524c8720dd69b0e3179344f04ebb5f90f2e4a440c6ea3b2f1ee
%bcond check 0
%global debug_package %{nil}
%global crate fern
Name:           rust-fern0.6
Version:        0.6.2
Release:        1%{?dist}
Summary:        Simple, efficient logging
License:        MIT
URL:            https://crates.io/crates/fern
Source0:        https://static.crates.io/crates/fern/fern-%{version}.crate
Patch:          fern-fix-metadata-auto.diff
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

%package     -n %{name}+chrono-devel
Summary:        Simple, efficient logging
BuildArch:      noarch
%description -n %{name}+chrono-devel

This package contains library source intended for building other packages which
use the "chrono" feature of the "%{crate}" crate.

%package     -n %{name}+colored-devel
Summary:        Simple, efficient logging
BuildArch:      noarch
%description -n %{name}+colored-devel

This package contains library source intended for building other packages which
use the "colored" feature of the "%{crate}" crate.

%package     -n %{name}+date-based-devel
Summary:        Simple, efficient logging
BuildArch:      noarch
%description -n %{name}+date-based-devel

This package contains library source intended for building other packages which
use the "date-based" feature of the "%{crate}" crate.

%package     -n %{name}+meta-logging-in-format-devel
Summary:        Simple, efficient logging
BuildArch:      noarch
%description -n %{name}+meta-logging-in-format-devel

This package contains library source intended for building other packages which
use the "meta-logging-in-format" feature of the "%{crate}" crate.

%package     -n %{name}+reopen-03-devel
Summary:        Simple, efficient logging
BuildArch:      noarch
%description -n %{name}+reopen-03-devel

This package contains library source intended for building other packages which
use the "reopen-03" feature of the "%{crate}" crate.

%package     -n %{name}+reopen-1-devel
Summary:        Simple, efficient logging
BuildArch:      noarch
%description -n %{name}+reopen-1-devel

This package contains library source intended for building other packages which
use the "reopen-1" feature of the "%{crate}" crate.

%package     -n %{name}+syslog-3-devel
Summary:        Simple, efficient logging
BuildArch:      noarch
%description -n %{name}+syslog-3-devel

This package contains library source intended for building other packages which
use the "syslog-3" feature of the "%{crate}" crate.

%package     -n %{name}+syslog-4-devel
Summary:        Simple, efficient logging
BuildArch:      noarch
%description -n %{name}+syslog-4-devel

This package contains library source intended for building other packages which
use the "syslog-4" feature of the "%{crate}" crate.

%package     -n %{name}+syslog-6-devel
Summary:        Simple, efficient logging
BuildArch:      noarch
%description -n %{name}+syslog-6-devel

This package contains library source intended for building other packages which
use the "syslog-6" feature of the "%{crate}" crate.

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
%files -n rust-fern0.6-devel -f %{oreon_filedir}/rust-fern0.6-devel.list

%changelog

%autochangelog
