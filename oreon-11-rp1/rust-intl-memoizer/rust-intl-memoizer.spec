%global source0_hash 310da2e345f5eb861e7a07ee182262e94975051db9e4223e909ba90f392f163f
%bcond check 1
%global debug_package %{nil}
%global crate intl-memoizer
Name:           rust-intl-memoizer
Version:        0.5.3
Release:        1%{?dist}
Summary:        Memoizer specifically tailored for storing lazy-initialized intl formatters
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/intl-memoizer
Source0:        https://static.crates.io/crates/intl-memoizer/intl-memoizer-%{version}.crate
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
Summary:        Memoizer specifically tailored for storing lazy-initialized intl formatters
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

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
%files -n rust-intl-memoizer-devel -f %{oreon_filedir}/rust-intl-memoizer-devel.list

%changelog

%autochangelog
