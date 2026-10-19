%global source0_hash 6c49c37c09c17a53d937dfbb742eb3a961d65a994e6bcdcf37e7399d0cc8ab5e
%bcond check 1
%global debug_package %{nil}
%global crate hmac
Name:           rust-hmac0.12
Version:        0.12.1
Release:        1%{?dist}
Summary:        Generic implementation of Hash-based Message Authentication Code (HMAC)
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/hmac
Source0:        https://static.crates.io/crates/hmac/hmac-%{version}.crate
Patch:          hmac-fix-metadata.diff
Patch10:        hmac-0.12.1-no-streebog.patch
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
Summary:        Generic implementation of Hash-based Message Authentication Code (HMAC)
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+reset-devel
Summary:        Generic implementation of Hash-based Message Authentication Code (HMAC)
BuildArch:      noarch
%description -n %{name}+reset-devel

This package contains library source intended for building other packages which
use the "reset" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Generic implementation of Hash-based Message Authentication Code (HMAC)
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

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
%files -n rust-hmac0.12-devel -f %{oreon_filedir}/rust-hmac0.12-devel.list

%changelog

%autochangelog
