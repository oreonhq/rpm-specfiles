%global source0_hash b75a19a7a740b25bc7944bdee6172368f988763b744e3d4dfe753f6b4ece40cc
%bcond check 0
%global debug_package %{nil}
%global crate signal-hook-mio
Name:           rust-signal-hook-mio
Version:        0.2.5
Release:        1%{?dist}
Summary:        MIO support for signal-hook
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/signal-hook-mio
Source0:        https://static.crates.io/crates/signal-hook-mio/signal-hook-mio-%{version}.crate
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

%package     -n %{name}+mio-0_6-devel
Summary:        MIO support for signal-hook
BuildArch:      noarch
%description -n %{name}+mio-0_6-devel

This package contains library source intended for building other packages which
use the "mio-0_6" feature of the "%{crate}" crate.

%package     -n %{name}+mio-0_7-devel
Summary:        MIO support for signal-hook
BuildArch:      noarch
%description -n %{name}+mio-0_7-devel

This package contains library source intended for building other packages which
use the "mio-0_7" feature of the "%{crate}" crate.

%package     -n %{name}+mio-0_8-devel
Summary:        MIO support for signal-hook
BuildArch:      noarch
%description -n %{name}+mio-0_8-devel

This package contains library source intended for building other packages which
use the "mio-0_8" feature of the "%{crate}" crate.

%package     -n %{name}+mio-1_0-devel
Summary:        MIO support for signal-hook
BuildArch:      noarch
%description -n %{name}+mio-1_0-devel

This package contains library source intended for building other packages which
use the "mio-1_0" feature of the "%{crate}" crate.

%package     -n %{name}+mio-uds-devel
Summary:        MIO support for signal-hook
BuildArch:      noarch
%description -n %{name}+mio-uds-devel

This package contains library source intended for building other packages which
use the "mio-uds" feature of the "%{crate}" crate.

%package     -n %{name}+support-v0_6-devel
Summary:        MIO support for signal-hook
BuildArch:      noarch
%description -n %{name}+support-v0_6-devel

This package contains library source intended for building other packages which
use the "support-v0_6" feature of the "%{crate}" crate.

%package     -n %{name}+support-v0_7-devel
Summary:        MIO support for signal-hook
BuildArch:      noarch
%description -n %{name}+support-v0_7-devel

This package contains library source intended for building other packages which
use the "support-v0_7" feature of the "%{crate}" crate.

%package     -n %{name}+support-v0_8-devel
Summary:        MIO support for signal-hook
BuildArch:      noarch
%description -n %{name}+support-v0_8-devel

This package contains library source intended for building other packages which
use the "support-v0_8" feature of the "%{crate}" crate.

%package     -n %{name}+support-v1_0-devel
Summary:        MIO support for signal-hook
BuildArch:      noarch
%description -n %{name}+support-v1_0-devel

This package contains library source intended for building other packages which
use the "support-v1_0" feature of the "%{crate}" crate.

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
%files -n rust-signal-hook-mio-devel -f %{oreon_filedir}/rust-signal-hook-mio-devel.list

%changelog

%autochangelog
