%global source0_hash 9466e4f18a53312faee414ea85813d6674d4cb5badad059365c4882984b40201
%bcond check 0
%global debug_package %{nil}
%global crate glycin-core
Name:           rust-glycin-core
Version:        4.0.0
Release:        1%{?dist}
Summary:        Sandboxed image decoding
License:        MPL-2.0 OR LGPL-2.1-or-later
URL:            https://crates.io/crates/glycin-core
Source0:        https://static.crates.io/crates/glycin-core/glycin-core-%{version}.crate
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

%package     -n %{name}+builtin-devel
Summary:        Sandboxed image decoding
BuildArch:      noarch
%description -n %{name}+builtin-devel

This package contains library source intended for building other packages which
use the "builtin" feature of the "%{crate}" crate.

%package     -n %{name}+builtin-image-rs-devel
Summary:        Sandboxed image decoding
BuildArch:      noarch
%description -n %{name}+builtin-image-rs-devel

This package contains library source intended for building other packages which
use the "builtin-image-rs" feature of the "%{crate}" crate.

%package     -n %{name}+builtin-test-devel
Summary:        Sandboxed image decoding
BuildArch:      noarch
%description -n %{name}+builtin-test-devel

This package contains library source intended for building other packages which
use the "builtin-test" feature of the "%{crate}" crate.

%package     -n %{name}+external-devel
Summary:        Sandboxed image decoding
BuildArch:      noarch
%description -n %{name}+external-devel

This package contains library source intended for building other packages which
use the "external" feature of the "%{crate}" crate.

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
%files -n rust-glycin-core-devel -f %{oreon_filedir}/rust-glycin-core-devel.list

%changelog

%autochangelog
