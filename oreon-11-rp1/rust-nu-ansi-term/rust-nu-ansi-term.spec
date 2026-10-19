%global source0_hash 7957b9740744892f114936ab4a57b3f487491bbeafaf8083688b16841a4240e5
%bcond check 0
%global debug_package %{nil}
%global crate nu-ansi-term
Name:           rust-nu-ansi-term
Version:        0.50.3
Release:        2%{?dist}
Summary:        Library for ANSI terminal colors and styles (bold, underline)
License:        MIT
URL:            https://crates.io/crates/nu-ansi-term
Source0:        https://static.crates.io/crates/nu-ansi-term/nu-ansi-term-%{version}.crate
Patch:          nu-ansi-term-fix-metadata-auto.diff
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
Summary:        Library for ANSI terminal colors and styles (bold, underline)
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+derive_serde_style-devel
Summary:        Library for ANSI terminal colors and styles (bold, underline)
BuildArch:      noarch
%description -n %{name}+derive_serde_style-devel

This package contains library source intended for building other packages which
use the "derive_serde_style" feature of the "%{crate}" crate.

%package     -n %{name}+gnu_legacy-devel
Summary:        Library for ANSI terminal colors and styles (bold, underline)
BuildArch:      noarch
%description -n %{name}+gnu_legacy-devel

This package contains library source intended for building other packages which
use the "gnu_legacy" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Library for ANSI terminal colors and styles (bold, underline)
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Library for ANSI terminal colors and styles (bold, underline)
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
%files -n rust-nu-ansi-term-devel -f %{oreon_filedir}/rust-nu-ansi-term-devel.list

%changelog

%autochangelog
