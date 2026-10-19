%global source0_hash 51fb07cbf6204adb9e71af7b689dc5caeca6147f9d9dd5c8f9ae3447147012c0
%bcond check 0
%global debug_package %{nil}
%global crate compress-tools
Name:           rust-compress-tools
Version:        0.16.1
Release:        1%{?dist}
Summary:        Utility functions for compressed and archive files handling
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/compress-tools
Source0:        https://static.crates.io/crates/compress-tools/compress-tools-%{version}.crate
Patch:          compress-tools-fix-metadata-auto.diff
Patch:          0001-backport-tests-port-from-unmaintained-crate-encoding.patch
ExclusiveArch:  %{rust_arches}
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(libarchive) >= 3.5.1
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Utility functions for compressed and archive files handling
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+async-trait-devel
Summary:        Utility functions for compressed and archive files handling
BuildArch:      noarch
%description -n %{name}+async-trait-devel

This package contains library source intended for building other packages which
use the "async-trait" feature of the "%{crate}" crate.

%package     -n %{name}+async_support-devel
Summary:        Utility functions for compressed and archive files handling
BuildArch:      noarch
%description -n %{name}+async_support-devel

This package contains library source intended for building other packages which
use the "async_support" feature of the "%{crate}" crate.

%package     -n %{name}+blocking-devel
Summary:        Utility functions for compressed and archive files handling
BuildArch:      noarch
%description -n %{name}+blocking-devel

This package contains library source intended for building other packages which
use the "blocking" feature of the "%{crate}" crate.

%package     -n %{name}+futures-channel-devel
Summary:        Utility functions for compressed and archive files handling
BuildArch:      noarch
%description -n %{name}+futures-channel-devel

This package contains library source intended for building other packages which
use the "futures-channel" feature of the "%{crate}" crate.

%package     -n %{name}+futures-core-devel
Summary:        Utility functions for compressed and archive files handling
BuildArch:      noarch
%description -n %{name}+futures-core-devel

This package contains library source intended for building other packages which
use the "futures-core" feature of the "%{crate}" crate.

%package     -n %{name}+futures-executor-devel
Summary:        Utility functions for compressed and archive files handling
BuildArch:      noarch
%description -n %{name}+futures-executor-devel

This package contains library source intended for building other packages which
use the "futures-executor" feature of the "%{crate}" crate.

%package     -n %{name}+futures-io-devel
Summary:        Utility functions for compressed and archive files handling
BuildArch:      noarch
%description -n %{name}+futures-io-devel

This package contains library source intended for building other packages which
use the "futures-io" feature of the "%{crate}" crate.

%package     -n %{name}+futures-util-devel
Summary:        Utility functions for compressed and archive files handling
BuildArch:      noarch
%description -n %{name}+futures-util-devel

This package contains library source intended for building other packages which
use the "futures-util" feature of the "%{crate}" crate.

%package     -n %{name}+futures_support-devel
Summary:        Utility functions for compressed and archive files handling
BuildArch:      noarch
%description -n %{name}+futures_support-devel

This package contains library source intended for building other packages which
use the "futures_support" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-devel
Summary:        Utility functions for compressed and archive files handling
BuildArch:      noarch
%description -n %{name}+tokio-devel

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-util-devel
Summary:        Utility functions for compressed and archive files handling
BuildArch:      noarch
%description -n %{name}+tokio-util-devel

This package contains library source intended for building other packages which
use the "tokio-util" feature of the "%{crate}" crate.

%package     -n %{name}+tokio_support-devel
Summary:        Utility functions for compressed and archive files handling
BuildArch:      noarch
%description -n %{name}+tokio_support-devel

This package contains library source intended for building other packages which
use the "tokio_support" feature of the "%{crate}" crate.

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

export LANG=C.UTF-8
%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-compress-tools-devel -f %{oreon_filedir}/rust-compress-tools-devel.list

%changelog

%autochangelog
