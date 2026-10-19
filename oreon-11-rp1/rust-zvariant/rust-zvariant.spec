%global source0_hash bee2a0bcd2a907786a456fff45aaaaf54c9ba5f50b71ae9ec1a4edd200c94911
%bcond check 0
%global debug_package %{nil}
%global crate zvariant
Name:           rust-zvariant
Version:        5.13.1
Release:        1%{?dist}
Summary:        D-Bus & GVariant encoding & decoding
License:        MIT
URL:            https://crates.io/crates/zvariant
Source0:        https://static.crates.io/crates/zvariant/zvariant-%{version}.crate
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
Summary:        D-Bus & GVariant encoding & decoding
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+arrayvec-devel
Summary:        D-Bus & GVariant encoding & decoding
BuildArch:      noarch
%description -n %{name}+arrayvec-devel

This package contains library source intended for building other packages which
use the "arrayvec" feature of the "%{crate}" crate.

%package     -n %{name}+camino-devel
Summary:        D-Bus & GVariant encoding & decoding
BuildArch:      noarch
%description -n %{name}+camino-devel

This package contains library source intended for building other packages which
use the "camino" feature of the "%{crate}" crate.

%package     -n %{name}+chrono-devel
Summary:        D-Bus & GVariant encoding & decoding
BuildArch:      noarch
%description -n %{name}+chrono-devel

This package contains library source intended for building other packages which
use the "chrono" feature of the "%{crate}" crate.

%package     -n %{name}+enumflags2-devel
Summary:        D-Bus & GVariant encoding & decoding
BuildArch:      noarch
%description -n %{name}+enumflags2-devel

This package contains library source intended for building other packages which
use the "enumflags2" feature of the "%{crate}" crate.

%package     -n %{name}+gvariant-devel
Summary:        D-Bus & GVariant encoding & decoding
BuildArch:      noarch
%description -n %{name}+gvariant-devel

This package contains library source intended for building other packages which
use the "gvariant" feature of the "%{crate}" crate.

%package     -n %{name}+heapless-devel
Summary:        D-Bus & GVariant encoding & decoding
BuildArch:      noarch
%description -n %{name}+heapless-devel

This package contains library source intended for building other packages which
use the "heapless" feature of the "%{crate}" crate.

%package     -n %{name}+option-as-array-devel
Summary:        D-Bus & GVariant encoding & decoding
BuildArch:      noarch
%description -n %{name}+option-as-array-devel

This package contains library source intended for building other packages which
use the "option-as-array" feature of the "%{crate}" crate.

%package     -n %{name}+ostree-tests-devel
Summary:        D-Bus & GVariant encoding & decoding
BuildArch:      noarch
%description -n %{name}+ostree-tests-devel

This package contains library source intended for building other packages which
use the "ostree-tests" feature of the "%{crate}" crate.

%package     -n %{name}+serde_bytes-devel
Summary:        D-Bus & GVariant encoding & decoding
BuildArch:      noarch
%description -n %{name}+serde_bytes-devel

This package contains library source intended for building other packages which
use the "serde_bytes" feature of the "%{crate}" crate.

%package     -n %{name}+time-devel
Summary:        D-Bus & GVariant encoding & decoding
BuildArch:      noarch
%description -n %{name}+time-devel

This package contains library source intended for building other packages which
use the "time" feature of the "%{crate}" crate.

%package     -n %{name}+url-devel
Summary:        D-Bus & GVariant encoding & decoding
BuildArch:      noarch
%description -n %{name}+url-devel

This package contains library source intended for building other packages which
use the "url" feature of the "%{crate}" crate.

%package     -n %{name}+uuid-devel
Summary:        D-Bus & GVariant encoding & decoding
BuildArch:      noarch
%description -n %{name}+uuid-devel

This package contains library source intended for building other packages which
use the "uuid" feature of the "%{crate}" crate.

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
%files -n rust-zvariant-devel -f %{oreon_filedir}/rust-zvariant-devel.list

%changelog

%autochangelog
