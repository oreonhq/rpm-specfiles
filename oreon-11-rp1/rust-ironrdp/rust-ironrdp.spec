%global source0_hash 04f41c014700b23e4b243c357c08af501f0158641bf556dcb0386329caef5c96
%bcond check 1
%global debug_package %{nil}
%global crate ironrdp
Name:           rust-ironrdp
Version:        0.11.0
Release:        1%{?dist}
Summary:        Meta crate re-exporting IronRDP crates for convenience
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/ironrdp
Source0:        https://static.crates.io/crates/ironrdp/ironrdp-%{version}.crate
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
Summary:        Meta crate re-exporting IronRDP crates for convenience
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+acceptor-devel
Summary:        Meta crate re-exporting IronRDP crates for convenience
BuildArch:      noarch
%description -n %{name}+acceptor-devel

This package contains library source intended for building other packages which
use the "acceptor" feature of the "%{crate}" crate.

%package     -n %{name}+cliprdr-devel
Summary:        Meta crate re-exporting IronRDP crates for convenience
BuildArch:      noarch
%description -n %{name}+cliprdr-devel

This package contains library source intended for building other packages which
use the "cliprdr" feature of the "%{crate}" crate.

%package     -n %{name}+connector-devel
Summary:        Meta crate re-exporting IronRDP crates for convenience
BuildArch:      noarch
%description -n %{name}+connector-devel

This package contains library source intended for building other packages which
use the "connector" feature of the "%{crate}" crate.

%package     -n %{name}+core-devel
Summary:        Meta crate re-exporting IronRDP crates for convenience
BuildArch:      noarch
%description -n %{name}+core-devel

This package contains library source intended for building other packages which
use the "core" feature of the "%{crate}" crate.

%package     -n %{name}+displaycontrol-devel
Summary:        Meta crate re-exporting IronRDP crates for convenience
BuildArch:      noarch
%description -n %{name}+displaycontrol-devel

This package contains library source intended for building other packages which
use the "displaycontrol" feature of the "%{crate}" crate.

%package     -n %{name}+dvc-devel
Summary:        Meta crate re-exporting IronRDP crates for convenience
BuildArch:      noarch
%description -n %{name}+dvc-devel

This package contains library source intended for building other packages which
use the "dvc" feature of the "%{crate}" crate.

%package     -n %{name}+graphics-devel
Summary:        Meta crate re-exporting IronRDP crates for convenience
BuildArch:      noarch
%description -n %{name}+graphics-devel

This package contains library source intended for building other packages which
use the "graphics" feature of the "%{crate}" crate.

%package     -n %{name}+input-devel
Summary:        Meta crate re-exporting IronRDP crates for convenience
BuildArch:      noarch
%description -n %{name}+input-devel

This package contains library source intended for building other packages which
use the "input" feature of the "%{crate}" crate.

%package     -n %{name}+pdu-devel
Summary:        Meta crate re-exporting IronRDP crates for convenience
BuildArch:      noarch
%description -n %{name}+pdu-devel

This package contains library source intended for building other packages which
use the "pdu" feature of the "%{crate}" crate.

%package     -n %{name}+rdpdr-devel
Summary:        Meta crate re-exporting IronRDP crates for convenience
BuildArch:      noarch
%description -n %{name}+rdpdr-devel

This package contains library source intended for building other packages which
use the "rdpdr" feature of the "%{crate}" crate.

%package     -n %{name}+rdpsnd-devel
Summary:        Meta crate re-exporting IronRDP crates for convenience
BuildArch:      noarch
%description -n %{name}+rdpsnd-devel

This package contains library source intended for building other packages which
use the "rdpsnd" feature of the "%{crate}" crate.

%package     -n %{name}+server-devel
Summary:        Meta crate re-exporting IronRDP crates for convenience
BuildArch:      noarch
%description -n %{name}+server-devel

This package contains library source intended for building other packages which
use the "server" feature of the "%{crate}" crate.

%package     -n %{name}+session-devel
Summary:        Meta crate re-exporting IronRDP crates for convenience
BuildArch:      noarch
%description -n %{name}+session-devel

This package contains library source intended for building other packages which
use the "session" feature of the "%{crate}" crate.

%package     -n %{name}+svc-devel
Summary:        Meta crate re-exporting IronRDP crates for convenience
BuildArch:      noarch
%description -n %{name}+svc-devel

This package contains library source intended for building other packages which
use the "svc" feature of the "%{crate}" crate.

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
%files -n rust-ironrdp-devel -f %{oreon_filedir}/rust-ironrdp-devel.list

%changelog

%autochangelog
