%global source0_hash 6f25a01f65079fdaf562930db1293d7a4abd4d98346a450cb7f37073af5c2b10
%bcond check 0
%global debug_package %{nil}
%global crate superluminal-perf
Name:           rust-superluminal-perf
Version:        0.4.0
Release:        1%{?dist}
Summary:        Superluminal Performance API for adding user events to profiler captures
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/superluminal-perf
Source0:        https://static.crates.io/crates/superluminal-perf/superluminal-perf-%{version}.crate
Patch:          superluminal-perf-fix-metadata-auto.diff
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
Summary:        Superluminal Performance API for adding user events to profiler captures
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+enable-devel
Summary:        Superluminal Performance API for adding user events to profiler captures
BuildArch:      noarch
%description -n %{name}+enable-devel

This package contains library source intended for building other packages which
use the "enable" feature of the "%{crate}" crate.

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
%files -n rust-superluminal-perf-devel -f %{oreon_filedir}/rust-superluminal-perf-devel.list

%changelog

%autochangelog
