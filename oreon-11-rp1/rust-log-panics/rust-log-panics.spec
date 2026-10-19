%global source0_hash 68f9dd8546191c1850ecf67d22f5ff00a935b890d0e84713159a55495cc2ac5f
%bcond check 1
%global debug_package %{nil}
%global crate log-panics
Name:           rust-log-panics
Version:        2.1.0
Release:        1%{?dist}
Summary:        Panic hook which logs panic messages rather than printing them
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/log-panics
Source0:        https://static.crates.io/crates/log-panics/log-panics-%{version}.crate
Patch:          log-panics-fix-metadata.diff
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
Summary:        Panic hook which logs panic messages rather than printing them
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+backtrace-devel
Summary:        Panic hook which logs panic messages rather than printing them
BuildArch:      noarch
%description -n %{name}+backtrace-devel

This package contains library source intended for building other packages which
use the "backtrace" feature of the "%{crate}" crate.

%package     -n %{name}+with-backtrace-devel
Summary:        Panic hook which logs panic messages rather than printing them
BuildArch:      noarch
%description -n %{name}+with-backtrace-devel

This package contains library source intended for building other packages which
use the "with-backtrace" feature of the "%{crate}" crate.

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
%files -n rust-log-panics-devel -f %{oreon_filedir}/rust-log-panics-devel.list

%changelog

%autochangelog
