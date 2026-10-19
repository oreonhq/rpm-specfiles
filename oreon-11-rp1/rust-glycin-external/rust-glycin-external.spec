%global source0_hash a7d335778b14437e1339d703afd1ce69e61df8ab5420882b4b7821b9a2ca9d4a
%bcond check 0
%global debug_package %{nil}
%global crate glycin-external
Name:           rust-glycin-external
Version:        4.0.0
Release:        1%{?dist}
Summary:        Sandboxed image decoding
License:        MPL-2.0 OR LGPL-2.1-or-later
URL:            https://crates.io/crates/glycin-external
Source0:        https://static.crates.io/crates/glycin-external/glycin-external-%{version}.crate
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
Summary:        Sandboxed image decoding
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+async-io-devel
Summary:        Sandboxed image decoding
BuildArch:      noarch
%description -n %{name}+async-io-devel

This package contains library source intended for building other packages which
use the "async-io" feature of the "%{crate}" crate.

%package     -n %{name}+gdk4-devel
Summary:        Sandboxed image decoding
BuildArch:      noarch
%description -n %{name}+gdk4-devel

This package contains library source intended for building other packages which
use the "gdk4" feature of the "%{crate}" crate.

%package     -n %{name}+gobject-devel
Summary:        Sandboxed image decoding
BuildArch:      noarch
%description -n %{name}+gobject-devel

This package contains library source intended for building other packages which
use the "gobject" feature of the "%{crate}" crate.

%package     -n %{name}+tests-devel
Summary:        Sandboxed image decoding
BuildArch:      noarch
%description -n %{name}+tests-devel

This package contains library source intended for building other packages which
use the "tests" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-devel
Summary:        Sandboxed image decoding
BuildArch:      noarch
%description -n %{name}+tokio-devel

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

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
%files -n rust-glycin-external-devel -f %{oreon_filedir}/rust-glycin-external-devel.list

%changelog

%autochangelog
