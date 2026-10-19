%global source0_hash 62314a1546a2064e033665d658e88c620a62904be945f8147e6b16c3db9f8651
%bcond check 1
%global debug_package %{nil}
%global crate audiopus_sys
Name:           rust-audiopus_sys
Version:        0.2.2
Release:        1%{?dist}
Summary:        FFI-Binding to Opus, dynamically or statically linked for Windows and UNIX
License:        ISC
URL:            https://crates.io/crates/audiopus_sys
Source0:        https://static.crates.io/crates/audiopus_sys/audiopus_sys-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  pkgconfig(opus)
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(opus) >= 1.0.0
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        FFI-Binding to Opus, dynamically or statically linked for Windows and UNIX
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+dynamic-devel
Summary:        FFI-Binding to Opus, dynamically or statically linked for Windows and UNIX
BuildArch:      noarch
%description -n %{name}+dynamic-devel

This package contains library source intended for building other packages which
use the "dynamic" feature of the "%{crate}" crate.

%package     -n %{name}+static-devel
Summary:        FFI-Binding to Opus, dynamically or statically linked for Windows and UNIX
BuildArch:      noarch
%description -n %{name}+static-devel

This package contains library source intended for building other packages which
use the "static" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
rm -rf opus
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
%files -n rust-audiopus_sys-devel -f %{oreon_filedir}/rust-audiopus_sys-devel.list

%changelog

%autochangelog
