%global source0_hash 98e1c6be25cfbf1bb4fea1a9da51bc05d3259a9062df4e53f54e5607895e33c9
%bcond check 1
%global debug_package %{nil}
%global crate astral-reqwest-middleware
Name:           rust-astral-reqwest-middleware
Version:        0.5.1
Release:        1%{?dist}
Summary:        Wrapper around reqwest to allow for client middleware chains
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/astral-reqwest-middleware
Source0:        https://static.crates.io/crates/astral-reqwest-middleware/astral-reqwest-middleware-%{version}.crate
Patch:          astral-reqwest-middleware-fix-metadata.diff
Patch10:        0001-Downstream-only-do-not-attempt-to-run-doctests-from-.patch
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
Summary:        Wrapper around reqwest to allow for client middleware chains
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+charset-devel
Summary:        Wrapper around reqwest to allow for client middleware chains
BuildArch:      noarch
%description -n %{name}+charset-devel

This package contains library source intended for building other packages which
use the "charset" feature of the "%{crate}" crate.

%package     -n %{name}+form-devel
Summary:        Wrapper around reqwest to allow for client middleware chains
BuildArch:      noarch
%description -n %{name}+form-devel

This package contains library source intended for building other packages which
use the "form" feature of the "%{crate}" crate.

%package     -n %{name}+http2-devel
Summary:        Wrapper around reqwest to allow for client middleware chains
BuildArch:      noarch
%description -n %{name}+http2-devel

This package contains library source intended for building other packages which
use the "http2" feature of the "%{crate}" crate.

%package     -n %{name}+json-devel
Summary:        Wrapper around reqwest to allow for client middleware chains
BuildArch:      noarch
%description -n %{name}+json-devel

This package contains library source intended for building other packages which
use the "json" feature of the "%{crate}" crate.

%package     -n %{name}+multipart-devel
Summary:        Wrapper around reqwest to allow for client middleware chains
BuildArch:      noarch
%description -n %{name}+multipart-devel

This package contains library source intended for building other packages which
use the "multipart" feature of the "%{crate}" crate.

%package     -n %{name}+query-devel
Summary:        Wrapper around reqwest to allow for client middleware chains
BuildArch:      noarch
%description -n %{name}+query-devel

This package contains library source intended for building other packages which
use the "query" feature of the "%{crate}" crate.

%package     -n %{name}+rustls-devel
Summary:        Wrapper around reqwest to allow for client middleware chains
BuildArch:      noarch
%description -n %{name}+rustls-devel

This package contains library source intended for building other packages which
use the "rustls" feature of the "%{crate}" crate.

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
%files -n rust-astral-reqwest-middleware-devel -f %{oreon_filedir}/rust-astral-reqwest-middleware-devel.list

%changelog

%autochangelog
