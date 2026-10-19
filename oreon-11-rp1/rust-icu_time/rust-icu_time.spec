%global source0_hash af37e1c3b9f3ab564b619fdf4b22de169f6381eb0f7048e3ca454290c438126b
%bcond check 1
%global debug_package %{nil}
%global crate icu_time
Name:           rust-icu_time
Version:        2.3.0
Release:        1%{?dist}
Summary:        Processing of dates, times, and time zones with a focus on i18n and interop
License:        Unicode-3.0
URL:            https://crates.io/crates/icu_time
Source0:        https://static.crates.io/crates/icu_time/icu_time-%{version}.crate
Patch10:        0001-In-icu_time-limit-use-of-the-icu-crate-to-doctests.patch
Patch11:        0001-Downstream-only-omit-a-test-that-would-require-icu_p.patch
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
Summary:        Processing of dates, times, and time zones with a focus on i18n and interop
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Processing of dates, times, and time zones with a focus on i18n and interop
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+compiled_data-devel
Summary:        Processing of dates, times, and time zones with a focus on i18n and interop
BuildArch:      noarch
%description -n %{name}+compiled_data-devel

This package contains library source intended for building other packages which
use the "compiled_data" feature of the "%{crate}" crate.

%package     -n %{name}+datagen-devel
Summary:        Processing of dates, times, and time zones with a focus on i18n and interop
BuildArch:      noarch
%description -n %{name}+datagen-devel

This package contains library source intended for building other packages which
use the "datagen" feature of the "%{crate}" crate.

%package     -n %{name}+ixdtf-devel
Summary:        Processing of dates, times, and time zones with a focus on i18n and interop
BuildArch:      noarch
%description -n %{name}+ixdtf-devel

This package contains library source intended for building other packages which
use the "ixdtf" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Processing of dates, times, and time zones with a focus on i18n and interop
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

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

%cargo_test -a -- --lib
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-icu_time-devel -f %{oreon_filedir}/rust-icu_time-devel.list

%changelog

%autochangelog
