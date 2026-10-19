%global source0_hash de671bd27a75a797dc9ae289ba1e77276e75e2026408aab65185384e2d5cd3f6
%bcond check 1
%global debug_package %{nil}
%global crate env_logger
Name:           rust-env_logger
Version:        0.11.11
Release:        2%{?dist}
Summary:        Logging implementation for log which is configured via an environment variable
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/env_logger
Source0:        https://static.crates.io/crates/env_logger/env_logger-%{version}.crate
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
Summary:        Logging implementation for log which is configured via an environment variable
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+auto-color-devel
Summary:        Logging implementation for log which is configured via an environment variable
BuildArch:      noarch
%description -n %{name}+auto-color-devel

This package contains library source intended for building other packages which
use the "auto-color" feature of the "%{crate}" crate.

%package     -n %{name}+color-devel
Summary:        Logging implementation for log which is configured via an environment variable
BuildArch:      noarch
%description -n %{name}+color-devel

This package contains library source intended for building other packages which
use the "color" feature of the "%{crate}" crate.

%package     -n %{name}+humantime-devel
Summary:        Logging implementation for log which is configured via an environment variable
BuildArch:      noarch
%description -n %{name}+humantime-devel

This package contains library source intended for building other packages which
use the "humantime" feature of the "%{crate}" crate.

%package     -n %{name}+kv-devel
Summary:        Logging implementation for log which is configured via an environment variable
BuildArch:      noarch
%description -n %{name}+kv-devel

This package contains library source intended for building other packages which
use the "kv" feature of the "%{crate}" crate.

%package     -n %{name}+regex-devel
Summary:        Logging implementation for log which is configured via an environment variable
BuildArch:      noarch
%description -n %{name}+regex-devel

This package contains library source intended for building other packages which
use the "regex" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-kv-devel
Summary:        Logging implementation for log which is configured via an environment variable
BuildArch:      noarch
%description -n %{name}+unstable-kv-devel

This package contains library source intended for building other packages which
use the "unstable-kv" feature of the "%{crate}" crate.

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
%files -n rust-env_logger-devel -f %{oreon_filedir}/rust-env_logger-devel.list

%changelog

%autochangelog
