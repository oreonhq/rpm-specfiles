%global source0_hash ee855f1f400bd0e5c02d150ae5de3840039a3f54b025156404e34c23c03f47c3
%bcond check 0
%global debug_package %{nil}
%global crate tracing-log
Name:           rust-tracing-log
Version:        0.2.0
Release:        1%{?dist}
Summary:        Provides compatibility between `tracing` and the `log` crate.
License:        MIT
URL:            https://crates.io/crates/tracing-log
Source0:        https://static.crates.io/crates/tracing-log/tracing-log-%{version}.crate
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
Summary:        Provides compatibility between `tracing` and the `log` crate.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+ahash-devel
Summary:        Provides compatibility between `tracing` and the `log` crate.
BuildArch:      noarch
%description -n %{name}+ahash-devel

This package contains library source intended for building other packages which
use the "ahash" feature of the "%{crate}" crate.

%package     -n %{name}+interest-cache-devel
Summary:        Provides compatibility between `tracing` and the `log` crate.
BuildArch:      noarch
%description -n %{name}+interest-cache-devel

This package contains library source intended for building other packages which
use the "interest-cache" feature of the "%{crate}" crate.

%package     -n %{name}+log-tracer-devel
Summary:        Provides compatibility between `tracing` and the `log` crate.
BuildArch:      noarch
%description -n %{name}+log-tracer-devel

This package contains library source intended for building other packages which
use the "log-tracer" feature of the "%{crate}" crate.

%package     -n %{name}+lru-devel
Summary:        Provides compatibility between `tracing` and the `log` crate.
BuildArch:      noarch
%description -n %{name}+lru-devel

This package contains library source intended for building other packages which
use the "lru" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Provides compatibility between `tracing` and the `log` crate.
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

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
%files -n rust-tracing-log-devel -f %{oreon_filedir}/rust-tracing-log-devel.list

%changelog

%autochangelog
