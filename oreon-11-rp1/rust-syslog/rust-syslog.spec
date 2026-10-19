%global source0_hash dfc7e95b5b795122fafe6519e27629b5ab4232c73ebb2428f568e82b1a457ad3
%bcond check 1
%global debug_package %{nil}
%global crate syslog
Name:           rust-syslog
Version:        6.1.1
Release:        1%{?dist}
Summary:        Send log messages to syslog
License:        MIT
URL:            https://crates.io/crates/syslog
Source0:        https://static.crates.io/crates/syslog/syslog-%{version}.crate
Patch:          syslog-fix-metadata.diff
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
Summary:        Send log messages to syslog
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

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
%files -n rust-syslog-devel -f %{oreon_filedir}/rust-syslog-devel.list

%changelog

%autochangelog
