%global source0_hash cae6561573e9996c2c26bf1c723b137a99c2d571a3276bd8f4ac52bfa44b3f2c
%bcond check 1
%global debug_package %{nil}
%global crate zlink-core
Name:           rust-zlink-core
Version:        0.4.0
Release:        1%{?dist}
Summary:        Core crate of the zlink project
License:        MIT
URL:            https://crates.io/crates/zlink-core
Source0:        https://static.crates.io/crates/zlink-core/zlink-core-%{version}.crate
Patch:          zlink-core-fix-metadata.diff
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
Summary:        Core crate of the zlink project
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+bytes-devel
Summary:        Core crate of the zlink project
BuildArch:      noarch
%description -n %{name}+bytes-devel

This package contains library source intended for building other packages which
use the "bytes" feature of the "%{crate}" crate.

%package     -n %{name}+chrono-devel
Summary:        Core crate of the zlink project
BuildArch:      noarch
%description -n %{name}+chrono-devel

This package contains library source intended for building other packages which
use the "chrono" feature of the "%{crate}" crate.

%package     -n %{name}+idl-devel
Summary:        Core crate of the zlink project
BuildArch:      noarch
%description -n %{name}+idl-devel

This package contains library source intended for building other packages which
use the "idl" feature of the "%{crate}" crate.

%package     -n %{name}+idl-parse-devel
Summary:        Core crate of the zlink project
BuildArch:      noarch
%description -n %{name}+idl-parse-devel

This package contains library source intended for building other packages which
use the "idl-parse" feature of the "%{crate}" crate.

%package     -n %{name}+indexmap-devel
Summary:        Core crate of the zlink project
BuildArch:      noarch
%description -n %{name}+indexmap-devel

This package contains library source intended for building other packages which
use the "indexmap" feature of the "%{crate}" crate.

%package     -n %{name}+introspection-devel
Summary:        Core crate of the zlink project
BuildArch:      noarch
%description -n %{name}+introspection-devel

This package contains library source intended for building other packages which
use the "introspection" feature of the "%{crate}" crate.

%package     -n %{name}+proxy-devel
Summary:        Core crate of the zlink project
BuildArch:      noarch
%description -n %{name}+proxy-devel

This package contains library source intended for building other packages which
use the "proxy" feature of the "%{crate}" crate.

%package     -n %{name}+server-devel
Summary:        Core crate of the zlink project
BuildArch:      noarch
%description -n %{name}+server-devel

This package contains library source intended for building other packages which
use the "server" feature of the "%{crate}" crate.

%package     -n %{name}+service-devel
Summary:        Core crate of the zlink project
BuildArch:      noarch
%description -n %{name}+service-devel

This package contains library source intended for building other packages which
use the "service" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Core crate of the zlink project
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+time-devel
Summary:        Core crate of the zlink project
BuildArch:      noarch
%description -n %{name}+time-devel

This package contains library source intended for building other packages which
use the "time" feature of the "%{crate}" crate.

%package     -n %{name}+tracing-devel
Summary:        Core crate of the zlink project
BuildArch:      noarch
%description -n %{name}+tracing-devel

This package contains library source intended for building other packages which
use the "tracing" feature of the "%{crate}" crate.

%package     -n %{name}+url-devel
Summary:        Core crate of the zlink project
BuildArch:      noarch
%description -n %{name}+url-devel

This package contains library source intended for building other packages which
use the "url" feature of the "%{crate}" crate.

%package     -n %{name}+uuid-devel
Summary:        Core crate of the zlink project
BuildArch:      noarch
%description -n %{name}+uuid-devel

This package contains library source intended for building other packages which
use the "uuid" feature of the "%{crate}" crate.

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
%files -n rust-zlink-core-devel -f %{oreon_filedir}/rust-zlink-core-devel.list

%changelog

%autochangelog
