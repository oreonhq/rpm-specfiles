%global source0_hash ecbd51fb6c020672543641167efa4e6417ff7ad76849ed556ace3595e72de03a
%bcond check 0
%global debug_package %{nil}
%global crate diesel_derives
Name:           rust-diesel_derives
Version:        2.3.10
Release:        1%{?dist}
Summary:        You should not use this crate directly, it is internal to Diesel.
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/diesel_derives
Source0:        https://static.crates.io/crates/diesel_derives/diesel_derives-%{version}.crate
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
Summary:        You should not use this crate directly, it is internal to Diesel.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+128-column-tables-devel
Summary:        You should not use this crate directly, it is internal to Diesel.
BuildArch:      noarch
%description -n %{name}+128-column-tables-devel

This package contains library source intended for building other packages which
use the "128-column-tables" feature of the "%{crate}" crate.

%package     -n %{name}+32-column-tables-devel
Summary:        You should not use this crate directly, it is internal to Diesel.
BuildArch:      noarch
%description -n %{name}+32-column-tables-devel

This package contains library source intended for building other packages which
use the "32-column-tables" feature of the "%{crate}" crate.

%package     -n %{name}+64-column-tables-devel
Summary:        You should not use this crate directly, it is internal to Diesel.
BuildArch:      noarch
%description -n %{name}+64-column-tables-devel

This package contains library source intended for building other packages which
use the "64-column-tables" feature of the "%{crate}" crate.

%package     -n %{name}+chrono-devel
Summary:        You should not use this crate directly, it is internal to Diesel.
BuildArch:      noarch
%description -n %{name}+chrono-devel

This package contains library source intended for building other packages which
use the "chrono" feature of the "%{crate}" crate.

%package     -n %{name}+mysql-devel
Summary:        You should not use this crate directly, it is internal to Diesel.
BuildArch:      noarch
%description -n %{name}+mysql-devel

This package contains library source intended for building other packages which
use the "mysql" feature of the "%{crate}" crate.

%package     -n %{name}+nightly-devel
Summary:        You should not use this crate directly, it is internal to Diesel.
BuildArch:      noarch
%description -n %{name}+nightly-devel

This package contains library source intended for building other packages which
use the "nightly" feature of the "%{crate}" crate.

%package     -n %{name}+numeric-devel
Summary:        You should not use this crate directly, it is internal to Diesel.
BuildArch:      noarch
%description -n %{name}+numeric-devel

This package contains library source intended for building other packages which
use the "numeric" feature of the "%{crate}" crate.

%package     -n %{name}+postgres-devel
Summary:        You should not use this crate directly, it is internal to Diesel.
BuildArch:      noarch
%description -n %{name}+postgres-devel

This package contains library source intended for building other packages which
use the "postgres" feature of the "%{crate}" crate.

%package     -n %{name}+r2d2-devel
Summary:        You should not use this crate directly, it is internal to Diesel.
BuildArch:      noarch
%description -n %{name}+r2d2-devel

This package contains library source intended for building other packages which
use the "r2d2" feature of the "%{crate}" crate.

%package     -n %{name}+sqlite-devel
Summary:        You should not use this crate directly, it is internal to Diesel.
BuildArch:      noarch
%description -n %{name}+sqlite-devel

This package contains library source intended for building other packages which
use the "sqlite" feature of the "%{crate}" crate.

%package     -n %{name}+time-devel
Summary:        You should not use this crate directly, it is internal to Diesel.
BuildArch:      noarch
%description -n %{name}+time-devel

This package contains library source intended for building other packages which
use the "time" feature of the "%{crate}" crate.

%package     -n %{name}+with-deprecated-devel
Summary:        You should not use this crate directly, it is internal to Diesel.
BuildArch:      noarch
%description -n %{name}+with-deprecated-devel

This package contains library source intended for building other packages which
use the "with-deprecated" feature of the "%{crate}" crate.

%package     -n %{name}+without-deprecated-devel
Summary:        You should not use this crate directly, it is internal to Diesel.
BuildArch:      noarch
%description -n %{name}+without-deprecated-devel

This package contains library source intended for building other packages which
use the "without-deprecated" feature of the "%{crate}" crate.

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
%files -n rust-diesel_derives-devel -f %{oreon_filedir}/rust-diesel_derives-devel.list

%changelog

%autochangelog
