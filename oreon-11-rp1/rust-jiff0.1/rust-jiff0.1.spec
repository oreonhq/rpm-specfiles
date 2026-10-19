%global source0_hash c04ef77ae73f3cf50510712722f0c4e8b46f5aaa1bf5ffad2ae213e6495e78e5
%bcond check 0
%global debug_package %{nil}
%global crate jiff
Name:           rust-jiff0.1
Version:        0.1.29
Release:        1%{?dist}
Summary:        A date-time library that encourages you to jump into the pit of success.
License:        Unlicense OR MIT
URL:            https://crates.io/crates/jiff
Source0:        https://static.crates.io/crates/jiff/jiff-%{version}.crate
Patch:          jiff-fix-metadata-auto.diff
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
Summary:        A date-time library that encourages you to jump into the pit of success.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        A date-time library that encourages you to jump into the pit of success.
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+jiff-tzdb-devel
Summary:        A date-time library that encourages you to jump into the pit of success.
BuildArch:      noarch
%description -n %{name}+jiff-tzdb-devel

This package contains library source intended for building other packages which
use the "jiff-tzdb" feature of the "%{crate}" crate.

%package     -n %{name}+js-devel
Summary:        A date-time library that encourages you to jump into the pit of success.
BuildArch:      noarch
%description -n %{name}+js-devel

This package contains library source intended for building other packages which
use the "js" feature of the "%{crate}" crate.

%package     -n %{name}+log-devel
Summary:        A date-time library that encourages you to jump into the pit of success.
BuildArch:      noarch
%description -n %{name}+log-devel

This package contains library source intended for building other packages which
use the "log" feature of the "%{crate}" crate.

%package     -n %{name}+logging-devel
Summary:        A date-time library that encourages you to jump into the pit of success.
BuildArch:      noarch
%description -n %{name}+logging-devel

This package contains library source intended for building other packages which
use the "logging" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        A date-time library that encourages you to jump into the pit of success.
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        A date-time library that encourages you to jump into the pit of success.
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+tz-system-devel
Summary:        A date-time library that encourages you to jump into the pit of success.
BuildArch:      noarch
%description -n %{name}+tz-system-devel

This package contains library source intended for building other packages which
use the "tz-system" feature of the "%{crate}" crate.

%package     -n %{name}+tzdb-bundle-always-devel
Summary:        A date-time library that encourages you to jump into the pit of success.
BuildArch:      noarch
%description -n %{name}+tzdb-bundle-always-devel

This package contains library source intended for building other packages which
use the "tzdb-bundle-always" feature of the "%{crate}" crate.

%package     -n %{name}+tzdb-bundle-platform-devel
Summary:        A date-time library that encourages you to jump into the pit of success.
BuildArch:      noarch
%description -n %{name}+tzdb-bundle-platform-devel

This package contains library source intended for building other packages which
use the "tzdb-bundle-platform" feature of the "%{crate}" crate.

%package     -n %{name}+tzdb-concatenated-devel
Summary:        A date-time library that encourages you to jump into the pit of success.
BuildArch:      noarch
%description -n %{name}+tzdb-concatenated-devel

This package contains library source intended for building other packages which
use the "tzdb-concatenated" feature of the "%{crate}" crate.

%package     -n %{name}+tzdb-zoneinfo-devel
Summary:        A date-time library that encourages you to jump into the pit of success.
BuildArch:      noarch
%description -n %{name}+tzdb-zoneinfo-devel

This package contains library source intended for building other packages which
use the "tzdb-zoneinfo" feature of the "%{crate}" crate.

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
%files -n rust-jiff0.1-devel -f %{oreon_filedir}/rust-jiff0.1-devel.list

%changelog

%autochangelog
