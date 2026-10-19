%global source0_hash ab72a761e6085828cc8f0e05ed332b2554701368c5dc54de551bfaec466518ba
%bcond check 1
%global debug_package %{nil}
%global crate astral_async_zip
Name:           rust-astral_async_zip
Version:        0.0.17
Release:        1%{?dist}
Summary:        Asynchronous ZIP archive reading/writing crate
License:        MIT
URL:            https://crates.io/crates/astral_async_zip
Source0:        https://static.crates.io/crates/astral_async_zip/astral_async_zip-%{version}.crate
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
Summary:        Asynchronous ZIP archive reading/writing crate
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+async-compression-devel
Summary:        Asynchronous ZIP archive reading/writing crate
BuildArch:      noarch
%description -n %{name}+async-compression-devel

This package contains library source intended for building other packages which
use the "async-compression" feature of the "%{crate}" crate.

%package     -n %{name}+bzip2-devel
Summary:        Asynchronous ZIP archive reading/writing crate
BuildArch:      noarch
%description -n %{name}+bzip2-devel

This package contains library source intended for building other packages which
use the "bzip2" feature of the "%{crate}" crate.

%package     -n %{name}+deflate-devel
Summary:        Asynchronous ZIP archive reading/writing crate
BuildArch:      noarch
%description -n %{name}+deflate-devel

This package contains library source intended for building other packages which
use the "deflate" feature of the "%{crate}" crate.

%package     -n %{name}+deflate64-devel
Summary:        Asynchronous ZIP archive reading/writing crate
BuildArch:      noarch
%description -n %{name}+deflate64-devel

This package contains library source intended for building other packages which
use the "deflate64" feature of the "%{crate}" crate.

%package     -n %{name}+full-devel
Summary:        Asynchronous ZIP archive reading/writing crate
BuildArch:      noarch
%description -n %{name}+full-devel

This package contains library source intended for building other packages which
use the "full" feature of the "%{crate}" crate.

%package     -n %{name}+lzma-devel
Summary:        Asynchronous ZIP archive reading/writing crate
BuildArch:      noarch
%description -n %{name}+lzma-devel

This package contains library source intended for building other packages which
use the "lzma" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-devel
Summary:        Asynchronous ZIP archive reading/writing crate
BuildArch:      noarch
%description -n %{name}+tokio-devel

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-fs-devel
Summary:        Asynchronous ZIP archive reading/writing crate
BuildArch:      noarch
%description -n %{name}+tokio-fs-devel

This package contains library source intended for building other packages which
use the "tokio-fs" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-util-devel
Summary:        Asynchronous ZIP archive reading/writing crate
BuildArch:      noarch
%description -n %{name}+tokio-util-devel

This package contains library source intended for building other packages which
use the "tokio-util" feature of the "%{crate}" crate.

%package     -n %{name}+xz-devel
Summary:        Asynchronous ZIP archive reading/writing crate
BuildArch:      noarch
%description -n %{name}+xz-devel

This package contains library source intended for building other packages which
use the "xz" feature of the "%{crate}" crate.

%package     -n %{name}+zstd-devel
Summary:        Asynchronous ZIP archive reading/writing crate
BuildArch:      noarch
%description -n %{name}+zstd-devel

This package contains library source intended for building other packages which
use the "zstd" feature of the "%{crate}" crate.

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
%files -n rust-astral_async_zip-devel -f %{oreon_filedir}/rust-astral_async_zip-devel.list

%changelog

%autochangelog
