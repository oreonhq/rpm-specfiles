%global source0_hash 57f17d28a6e6acfe1733fe24bcd30774d13bffa4b8a22535b4c8c98423088d4e
%bcond check 1
%global debug_package %{nil}
%global crate reqwest-middleware
Name:           rust-reqwest-middleware0.4
Version:        0.4.2
Release:        1%{?dist}
Summary:        Wrapper around reqwest to allow for client middleware chains
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/reqwest-middleware
Source0:        https://static.crates.io/crates/reqwest-middleware/reqwest-middleware-%{version}.crate
Patch:          reqwest-middleware-fix-metadata.diff
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

%package     -n %{name}+rustls-tls-devel
Summary:        Wrapper around reqwest to allow for client middleware chains
BuildArch:      noarch
%description -n %{name}+rustls-tls-devel

This package contains library source intended for building other packages which
use the "rustls-tls" feature of the "%{crate}" crate.

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
%files -n rust-reqwest-middleware0.4-devel -f %{oreon_filedir}/rust-reqwest-middleware0.4-devel.list

%changelog

%autochangelog
