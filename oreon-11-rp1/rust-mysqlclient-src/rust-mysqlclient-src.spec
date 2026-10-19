%global source0_hash b5918bf2cec3b9a991a82fe9a9e0773997255b7bb6d11a50e8200bdfee9f2953
%bcond check 0
%global debug_package %{nil}
%global crate mysqlclient-src
%global crate_version 0.2.2+9.5.0
%global crate_instdir %{cargo_registry}/%{crate}-%{crate_version}
Name:           rust-mysqlclient-src
Version:        0.2.2
Release:        1%{?dist}
Summary:        Bundled version of libmysqlclient
License:        GPL-2.0-only
URL:            https://crates.io/crates/mysqlclient-src
Source0:        https://static.crates.io/crates/mysqlclient-src/mysqlclient-src-%{version}.crate
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
Summary:        Bundled version of libmysqlclient
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+with-asan-devel
Summary:        Bundled version of libmysqlclient
BuildArch:      noarch
%description -n %{name}+with-asan-devel

This package contains library source intended for building other packages which
use the "with-asan" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{crate_version} -p1
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
%files -n rust-mysqlclient-src-devel -f %{oreon_filedir}/rust-mysqlclient-src-devel.list

%changelog

%autochangelog
