%global source0_hash 8b1581020d7a273442f5b45074a6a57d5757ad0a47dac0e9f0bd57b81936f3db
%bcond check 1
%global debug_package %{nil}
%global crate tracing-error
Name:           rust-tracing-error
Version:        0.2.1
Release:        1%{?dist}
Summary:        Utilities for enriching errors with tracing
License:        MIT
URL:            https://crates.io/crates/tracing-error
Source0:        https://static.crates.io/crates/tracing-error/tracing-error-%{version}.crate
Patch:          tracing-error-fix-metadata.diff
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
Summary:        Utilities for enriching errors with tracing
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+traced-error-devel
Summary:        Utilities for enriching errors with tracing
BuildArch:      noarch
%description -n %{name}+traced-error-devel

This package contains library source intended for building other packages which
use the "traced-error" feature of the "%{crate}" crate.

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
%files -n rust-tracing-error-devel -f %{oreon_filedir}/rust-tracing-error-devel.list

%changelog

%autochangelog
