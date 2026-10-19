%global source0_hash 36943ee01a6d67977dd3f84a5a1d2efeb4ada3a1ae771cadfaa535d9d9fc6507
%bcond check 0
%global debug_package %{nil}
%global crate tokio-util
Name:           rust-tokio-util0.6
Version:        0.6.10
Release:        1%{?dist}
Summary:        Additional utilities for working with Tokio.
License:        MIT
URL:            https://crates.io/crates/tokio-util
Source0:        https://static.crates.io/crates/tokio-util/tokio-util-%{version}.crate
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
Summary:        Additional utilities for working with Tokio.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+__docs_rs-devel
Summary:        Additional utilities for working with Tokio.
BuildArch:      noarch
%description -n %{name}+__docs_rs-devel

This package contains library source intended for building other packages which
use the "__docs_rs" feature of the "%{crate}" crate.

%package     -n %{name}+codec-devel
Summary:        Additional utilities for working with Tokio.
BuildArch:      noarch
%description -n %{name}+codec-devel

This package contains library source intended for building other packages which
use the "codec" feature of the "%{crate}" crate.

%package     -n %{name}+compat-devel
Summary:        Additional utilities for working with Tokio.
BuildArch:      noarch
%description -n %{name}+compat-devel

This package contains library source intended for building other packages which
use the "compat" feature of the "%{crate}" crate.

%package     -n %{name}+full-devel
Summary:        Additional utilities for working with Tokio.
BuildArch:      noarch
%description -n %{name}+full-devel

This package contains library source intended for building other packages which
use the "full" feature of the "%{crate}" crate.

%package     -n %{name}+futures-io-devel
Summary:        Additional utilities for working with Tokio.
BuildArch:      noarch
%description -n %{name}+futures-io-devel

This package contains library source intended for building other packages which
use the "futures-io" feature of the "%{crate}" crate.

%package     -n %{name}+futures-util-devel
Summary:        Additional utilities for working with Tokio.
BuildArch:      noarch
%description -n %{name}+futures-util-devel

This package contains library source intended for building other packages which
use the "futures-util" feature of the "%{crate}" crate.

%package     -n %{name}+io-devel
Summary:        Additional utilities for working with Tokio.
BuildArch:      noarch
%description -n %{name}+io-devel

This package contains library source intended for building other packages which
use the "io" feature of the "%{crate}" crate.

%package     -n %{name}+io-util-devel
Summary:        Additional utilities for working with Tokio.
BuildArch:      noarch
%description -n %{name}+io-util-devel

This package contains library source intended for building other packages which
use the "io-util" feature of the "%{crate}" crate.

%package     -n %{name}+net-devel
Summary:        Additional utilities for working with Tokio.
BuildArch:      noarch
%description -n %{name}+net-devel

This package contains library source intended for building other packages which
use the "net" feature of the "%{crate}" crate.

%package     -n %{name}+rt-devel
Summary:        Additional utilities for working with Tokio.
BuildArch:      noarch
%description -n %{name}+rt-devel

This package contains library source intended for building other packages which
use the "rt" feature of the "%{crate}" crate.

%package     -n %{name}+slab-devel
Summary:        Additional utilities for working with Tokio.
BuildArch:      noarch
%description -n %{name}+slab-devel

This package contains library source intended for building other packages which
use the "slab" feature of the "%{crate}" crate.

%package     -n %{name}+time-devel
Summary:        Additional utilities for working with Tokio.
BuildArch:      noarch
%description -n %{name}+time-devel

This package contains library source intended for building other packages which
use the "time" feature of the "%{crate}" crate.

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
%files -n rust-tokio-util0.6-devel -f %{oreon_filedir}/rust-tokio-util0.6-devel.list

%changelog

%autochangelog
