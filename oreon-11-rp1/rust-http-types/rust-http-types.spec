%global source0_hash 6e9b187a72d63adbfba487f48095306ac823049cb504ee195541e91c7775f5ad
%bcond check 0
%global debug_package %{nil}
%global crate http-types
Name:           rust-http-types
Version:        2.12.0
Release:        1%{?dist}
Summary:        Common types for HTTP operations.
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/http-types
Source0:        https://static.crates.io/crates/http-types/http-types-%{version}.crate
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
Summary:        Common types for HTTP operations.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+async-std-devel
Summary:        Common types for HTTP operations.
BuildArch:      noarch
%description -n %{name}+async-std-devel

This package contains library source intended for building other packages which
use the "async-std" feature of the "%{crate}" crate.

%package     -n %{name}+async_std-devel
Summary:        Common types for HTTP operations.
BuildArch:      noarch
%description -n %{name}+async_std-devel

This package contains library source intended for building other packages which
use the "async_std" feature of the "%{crate}" crate.

%package     -n %{name}+cookie-devel
Summary:        Common types for HTTP operations.
BuildArch:      noarch
%description -n %{name}+cookie-devel

This package contains library source intended for building other packages which
use the "cookie" feature of the "%{crate}" crate.

%package     -n %{name}+cookie-secure-devel
Summary:        Common types for HTTP operations.
BuildArch:      noarch
%description -n %{name}+cookie-secure-devel

This package contains library source intended for building other packages which
use the "cookie-secure" feature of the "%{crate}" crate.

%package     -n %{name}+cookies-devel
Summary:        Common types for HTTP operations.
BuildArch:      noarch
%description -n %{name}+cookies-devel

This package contains library source intended for building other packages which
use the "cookies" feature of the "%{crate}" crate.

%package     -n %{name}+docs-devel
Summary:        Common types for HTTP operations.
BuildArch:      noarch
%description -n %{name}+docs-devel

This package contains library source intended for building other packages which
use the "docs" feature of the "%{crate}" crate.

%package     -n %{name}+fs-devel
Summary:        Common types for HTTP operations.
BuildArch:      noarch
%description -n %{name}+fs-devel

This package contains library source intended for building other packages which
use the "fs" feature of the "%{crate}" crate.

%package     -n %{name}+http-devel
Summary:        Common types for HTTP operations.
BuildArch:      noarch
%description -n %{name}+http-devel

This package contains library source intended for building other packages which
use the "http" feature of the "%{crate}" crate.

%package     -n %{name}+hyperium_http-devel
Summary:        Common types for HTTP operations.
BuildArch:      noarch
%description -n %{name}+hyperium_http-devel

This package contains library source intended for building other packages which
use the "hyperium_http" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-devel
Summary:        Common types for HTTP operations.
BuildArch:      noarch
%description -n %{name}+unstable-devel

This package contains library source intended for building other packages which
use the "unstable" feature of the "%{crate}" crate.

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
%files -n rust-http-types-devel -f %{oreon_filedir}/rust-http-types-devel.list

%changelog

%autochangelog
