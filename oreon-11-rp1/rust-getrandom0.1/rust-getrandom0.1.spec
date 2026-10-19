%global source0_hash 8fc3cb4d91f53b50155bdcfd23f6a4c39ae1969c2ae85982b135750cccaf5fce
%bcond_without check
%global debug_package %{nil}
%global crate getrandom
Name:           rust-getrandom0.1
Version:        0.1.16
Release:        1%{?dist}
Summary:        Small cross-platform library for retrieving random data from system source
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/getrandom
Source0:        https://static.crates.io/crates/getrandom/getrandom-%{version}.crate
Patch:          getrandom-fix-metadata-auto.diff
Patch:          getrandom-fix-metadata.diff
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
Summary:        Small cross-platform library for retrieving random data from system source
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+dummy-devel
Summary:        Small cross-platform library for retrieving random data from system source
BuildArch:      noarch
%description -n %{name}+dummy-devel

This package contains library source intended for building other packages which
use the "dummy" feature of the "%{crate}" crate.

%package     -n %{name}+log-devel
Summary:        Small cross-platform library for retrieving random data from system source
BuildArch:      noarch
%description -n %{name}+log-devel

This package contains library source intended for building other packages which
use the "log" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Small cross-platform library for retrieving random data from system source
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version_no_tilde} -p1
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
%files -n rust-getrandom0.1-devel -f %{oreon_filedir}/rust-getrandom0.1-devel.list

%changelog

%autochangelog
