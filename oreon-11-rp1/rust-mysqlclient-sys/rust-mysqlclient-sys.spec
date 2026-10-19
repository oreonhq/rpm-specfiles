%global source0_hash b72511f8f6991fe4ac86421ea0625630fd94e360b906cc59720506499f9e8f3b
%bcond check 0
%global debug_package %{nil}
%global crate mysqlclient-sys
Name:           rust-mysqlclient-sys
Version:        0.5.2
Release:        1%{?dist}
Summary:        Auto-generated rust bindings for libmysqlclient
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/mysqlclient-sys
Source0:        https://static.crates.io/crates/mysqlclient-sys/mysqlclient-sys-%{version}.crate
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
Summary:        Auto-generated rust bindings for libmysqlclient
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+buildtime_bindgen-devel
Summary:        Auto-generated rust bindings for libmysqlclient
BuildArch:      noarch
%description -n %{name}+buildtime_bindgen-devel

This package contains library source intended for building other packages which
use the "buildtime_bindgen" feature of the "%{crate}" crate.

%package     -n %{name}+bundled-devel
Summary:        Auto-generated rust bindings for libmysqlclient
BuildArch:      noarch
%description -n %{name}+bundled-devel

This package contains library source intended for building other packages which
use the "bundled" feature of the "%{crate}" crate.

%package     -n %{name}+mysqlclient-src-devel
Summary:        Auto-generated rust bindings for libmysqlclient
BuildArch:      noarch
%description -n %{name}+mysqlclient-src-devel

This package contains library source intended for building other packages which
use the "mysqlclient-src" feature of the "%{crate}" crate.

%package     -n %{name}+openssl-sys-devel
Summary:        Auto-generated rust bindings for libmysqlclient
BuildArch:      noarch
%description -n %{name}+openssl-sys-devel

This package contains library source intended for building other packages which
use the "openssl-sys" feature of the "%{crate}" crate.

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
%files -n rust-mysqlclient-sys-devel -f %{oreon_filedir}/rust-mysqlclient-sys-devel.list

%changelog

%autochangelog
