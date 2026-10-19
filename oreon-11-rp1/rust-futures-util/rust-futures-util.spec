%global source0_hash 0d50a92467f8ba5dd6e3ee5d4bd04d73ab2e4e1c44474a0674821dfce14b79bc
%bcond check 0
%global debug_package %{nil}
%global crate futures-util
Name:           rust-futures-util
Version:        0.3.34
Release:        1%{?dist}
Summary:        Common utilities and extension traits for the futures-rs library
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/futures-util
Source0:        https://static.crates.io/crates/futures-util/futures-util-%{version}.crate
Patch:          futures-util-fix-metadata.diff
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
Summary:        Common utilities and extension traits for the futures-rs library
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Common utilities and extension traits for the futures-rs library
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+async-await-devel
Summary:        Common utilities and extension traits for the futures-rs library
BuildArch:      noarch
%description -n %{name}+async-await-devel

This package contains library source intended for building other packages which
use the "async-await" feature of the "%{crate}" crate.

%package     -n %{name}+async-await-macro-devel
Summary:        Common utilities and extension traits for the futures-rs library
BuildArch:      noarch
%description -n %{name}+async-await-macro-devel

This package contains library source intended for building other packages which
use the "async-await-macro" feature of the "%{crate}" crate.

%package     -n %{name}+bilock-devel
Summary:        Common utilities and extension traits for the futures-rs library
BuildArch:      noarch
%description -n %{name}+bilock-devel

This package contains library source intended for building other packages which
use the "bilock" feature of the "%{crate}" crate.

%package     -n %{name}+cfg-target-has-atomic-devel
Summary:        Common utilities and extension traits for the futures-rs library
BuildArch:      noarch
%description -n %{name}+cfg-target-has-atomic-devel

This package contains library source intended for building other packages which
use the "cfg-target-has-atomic" feature of the "%{crate}" crate.

%package     -n %{name}+channel-devel
Summary:        Common utilities and extension traits for the futures-rs library
BuildArch:      noarch
%description -n %{name}+channel-devel

This package contains library source intended for building other packages which
use the "channel" feature of the "%{crate}" crate.

%package     -n %{name}+futures-channel-devel
Summary:        Common utilities and extension traits for the futures-rs library
BuildArch:      noarch
%description -n %{name}+futures-channel-devel

This package contains library source intended for building other packages which
use the "futures-channel" feature of the "%{crate}" crate.

%package     -n %{name}+futures-io-devel
Summary:        Common utilities and extension traits for the futures-rs library
BuildArch:      noarch
%description -n %{name}+futures-io-devel

This package contains library source intended for building other packages which
use the "futures-io" feature of the "%{crate}" crate.

%package     -n %{name}+futures-macro-devel
Summary:        Common utilities and extension traits for the futures-rs library
BuildArch:      noarch
%description -n %{name}+futures-macro-devel

This package contains library source intended for building other packages which
use the "futures-macro" feature of the "%{crate}" crate.

%package     -n %{name}+futures-sink-devel
Summary:        Common utilities and extension traits for the futures-rs library
BuildArch:      noarch
%description -n %{name}+futures-sink-devel

This package contains library source intended for building other packages which
use the "futures-sink" feature of the "%{crate}" crate.

%package     -n %{name}+io-devel
Summary:        Common utilities and extension traits for the futures-rs library
BuildArch:      noarch
%description -n %{name}+io-devel

This package contains library source intended for building other packages which
use the "io" feature of the "%{crate}" crate.

%package     -n %{name}+libc-devel
Summary:        Common utilities and extension traits for the futures-rs library
BuildArch:      noarch
%description -n %{name}+libc-devel

This package contains library source intended for building other packages which
use the "libc" feature of the "%{crate}" crate.

%package     -n %{name}+memchr-devel
Summary:        Common utilities and extension traits for the futures-rs library
BuildArch:      noarch
%description -n %{name}+memchr-devel

This package contains library source intended for building other packages which
use the "memchr" feature of the "%{crate}" crate.

%package     -n %{name}+sink-devel
Summary:        Common utilities and extension traits for the futures-rs library
BuildArch:      noarch
%description -n %{name}+sink-devel

This package contains library source intended for building other packages which
use the "sink" feature of the "%{crate}" crate.

%package     -n %{name}+slab-devel
Summary:        Common utilities and extension traits for the futures-rs library
BuildArch:      noarch
%description -n %{name}+slab-devel

This package contains library source intended for building other packages which
use the "slab" feature of the "%{crate}" crate.

%package     -n %{name}+spin-devel
Summary:        Common utilities and extension traits for the futures-rs library
BuildArch:      noarch
%description -n %{name}+spin-devel

This package contains library source intended for building other packages which
use the "spin" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Common utilities and extension traits for the futures-rs library
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-devel
Summary:        Common utilities and extension traits for the futures-rs library
BuildArch:      noarch
%description -n %{name}+unstable-devel

This package contains library source intended for building other packages which
use the "unstable" feature of the "%{crate}" crate.

%package     -n %{name}+write-all-vectored-devel
Summary:        Common utilities and extension traits for the futures-rs library
BuildArch:      noarch
%description -n %{name}+write-all-vectored-devel

This package contains library source intended for building other packages which
use the "write-all-vectored" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build -a
%install
%cargo_install -a
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-futures-util-devel -f %{oreon_filedir}/rust-futures-util-devel.list

%changelog

%autochangelog
