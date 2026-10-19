%global source0_hash 6fb5bfbe0c3445d371dd8acf7d6c912ece8baf2f61f7c571af85a1d7687c2d0f
%bcond check 0
%global debug_package %{nil}
%global crate pq-src
%global crate_version 0.3.11+libpq-18.3
%global crate_instdir %{cargo_registry}/%{crate}-%{crate_version}
Name:           rust-pq-src
Version:        0.3.11
Release:        1%{?dist}
Summary:        Bundled version of libpq
License:        PostgreSQL
URL:            https://crates.io/crates/pq-src
Source0:        https://static.crates.io/crates/pq-src/pq-src-%{version}.crate
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
Summary:        Bundled version of libpq
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+openssl-sys-devel
Summary:        Bundled version of libpq
BuildArch:      noarch
%description -n %{name}+openssl-sys-devel

This package contains library source intended for building other packages which
use the "openssl-sys" feature of the "%{crate}" crate.

%package     -n %{name}+with-asan-devel
Summary:        Bundled version of libpq
BuildArch:      noarch
%description -n %{name}+with-asan-devel

This package contains library source intended for building other packages which
use the "with-asan" feature of the "%{crate}" crate.

%package     -n %{name}+with-openssl-devel
Summary:        Bundled version of libpq
BuildArch:      noarch
%description -n %{name}+with-openssl-devel

This package contains library source intended for building other packages which
use the "with-openssl" feature of the "%{crate}" crate.

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
%files -n rust-pq-src-devel -f %{oreon_filedir}/rust-pq-src-devel.list

%changelog

%autochangelog
