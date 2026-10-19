%global source0_hash ff2abc00be7fca6ebc474524697ae276ad847ad0a6b3faa4bcb027e9a4614ad0
%bcond check 0
%global debug_package %{nil}
%global crate getrandom
Name:           rust-getrandom0.2
Version:        0.2.17
Release:        1%{?dist}
Summary:        A small cross-platform library for retrieving random data from
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/getrandom
Source0:        https://static.crates.io/crates/getrandom/getrandom-%{version}.crate
Patch:          getrandom-fix-metadata-auto.diff
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
Summary:        A small cross-platform library for retrieving random data from
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+custom-devel
Summary:        A small cross-platform library for retrieving random data from
BuildArch:      noarch
%description -n %{name}+custom-devel

This package contains library source intended for building other packages which
use the "custom" feature of the "%{crate}" crate.

%package     -n %{name}+js-devel
Summary:        A small cross-platform library for retrieving random data from
BuildArch:      noarch
%description -n %{name}+js-devel

This package contains library source intended for building other packages which
use the "js" feature of the "%{crate}" crate.

%package     -n %{name}+linux_disable_fallback-devel
Summary:        A small cross-platform library for retrieving random data from
BuildArch:      noarch
%description -n %{name}+linux_disable_fallback-devel

This package contains library source intended for building other packages which
use the "linux_disable_fallback" feature of the "%{crate}" crate.

%package     -n %{name}+rdrand-devel
Summary:        A small cross-platform library for retrieving random data from
BuildArch:      noarch
%description -n %{name}+rdrand-devel

This package contains library source intended for building other packages which
use the "rdrand" feature of the "%{crate}" crate.

%package     -n %{name}+rustc-dep-of-std-devel
Summary:        A small cross-platform library for retrieving random data from
BuildArch:      noarch
%description -n %{name}+rustc-dep-of-std-devel

This package contains library source intended for building other packages which
use the "rustc-dep-of-std" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        A small cross-platform library for retrieving random data from
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+test-in-browser-devel
Summary:        A small cross-platform library for retrieving random data from
BuildArch:      noarch
%description -n %{name}+test-in-browser-devel

This package contains library source intended for building other packages which
use the "test-in-browser" feature of the "%{crate}" crate.

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
%files -n rust-getrandom0.2-devel -f %{oreon_filedir}/rust-getrandom0.2-devel.list

%changelog

%autochangelog
