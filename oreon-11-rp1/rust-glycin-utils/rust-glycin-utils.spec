%global source0_hash 43a93c6dfde7ab29b8e3c9844cb9e59a5bcd58ffdd9b24aab500d3a78a4b4cb0
%bcond check 1
%global debug_package %{nil}
%global crate glycin-utils
Name:           rust-glycin-utils
Version:        5.0.1
Release:        1%{?dist}
Summary:        Sandboxed image decoding
License:        MPL-2.0 OR LGPL-2.1-or-later
URL:            https://crates.io/crates/glycin-utils
Source0:        https://static.crates.io/crates/glycin-utils/glycin-utils-%{version}.crate
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

%package     -n %{name}+glib-devel
Summary:        Sandboxed image decoding
BuildArch:      noarch
%description -n %{name}+glib-devel

This package contains library source intended for building other packages which
use the "glib" feature of the "%{crate}" crate.

%package     -n %{name}+gobject-devel
Summary:        Sandboxed image decoding
BuildArch:      noarch
%description -n %{name}+gobject-devel

This package contains library source intended for building other packages which
use the "gobject" feature of the "%{crate}" crate.

%package     -n %{name}+image-rs-devel
Summary:        Sandboxed image decoding
BuildArch:      noarch
%description -n %{name}+image-rs-devel

This package contains library source intended for building other packages which
use the "image-rs" feature of the "%{crate}" crate.

%package     -n %{name}+loader-utils-devel
Summary:        Sandboxed image decoding
BuildArch:      noarch
%description -n %{name}+loader-utils-devel

This package contains library source intended for building other packages which
use the "loader-utils" feature of the "%{crate}" crate.

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
%files -n rust-glycin-utils-devel -f %{oreon_filedir}/rust-glycin-utils-devel.list

%changelog

%autochangelog
