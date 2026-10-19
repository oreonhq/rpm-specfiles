%global source0_hash bf0a738ed5d6450a9fb96e86a23ad808de2b727fd1394585da5cdd6788ffe724
%bcond check 0
%global debug_package %{nil}
%global crate tracing-chrome
Name:           rust-tracing-chrome
Version:        0.7.2
Release:        1%{?dist}
Summary:        A Layer for tracing-subscriber that outputs Chrome-style traces.
License:        MIT
URL:            https://crates.io/crates/tracing-chrome
Source0:        https://static.crates.io/crates/tracing-chrome/tracing-chrome-%{version}.crate
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
Summary:        A Layer for tracing-subscriber that outputs Chrome-style traces.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

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
%files -n rust-tracing-chrome-devel -f %{oreon_filedir}/rust-tracing-chrome-devel.list

%changelog

%autochangelog
