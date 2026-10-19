%global source0_hash c59d4b42303d6fdd5f2e058d7a420103752ec6c4bf260c08abd86a14ea5223a3
%bcond check 1
%global debug_package %{nil}
%global crate formatx
Name:           rust-formatx
Version:        0.4.2
Release:        1%{?dist}
Summary:        Macro for formatting non literal strings at runtime
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/formatx
Source0:        https://static.crates.io/crates/formatx/formatx-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  dos2unix
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
Summary:        Macro for formatting non literal strings at runtime
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
find . -type f -exec dos2unix --keepdate '{}' +
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
%files -n rust-formatx-devel -f %{oreon_filedir}/rust-formatx-devel.list

%changelog

%autochangelog
