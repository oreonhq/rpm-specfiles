%global source0_hash d6ae462f0b868614980d59df41e217a77648de7ad7cf8b2a407155659896d889
%bcond check 0
%global debug_package %{nil}
%global crate crosstermion
Name:           rust-crosstermion
Version:        0.16.0
Release:        1%{?dist}
Summary:        utilities for `crossterm`, without ties to `termion`
License:        MIT
URL:            https://crates.io/crates/crosstermion
Source0:        https://static.crates.io/crates/crosstermion/crosstermion-%{version}.crate
Patch:          crosstermion-fix-metadata-auto.diff
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
Summary:        utilities for `crossterm`, without ties to `termion`
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+ansiterm-devel
Summary:        utilities for `crossterm`, without ties to `termion`
BuildArch:      noarch
%description -n %{name}+ansiterm-devel

This package contains library source intended for building other packages which
use the "ansiterm" feature of the "%{crate}" crate.

%package     -n %{name}+async-channel-devel
Summary:        utilities for `crossterm`, without ties to `termion`
BuildArch:      noarch
%description -n %{name}+async-channel-devel

This package contains library source intended for building other packages which
use the "async-channel" feature of the "%{crate}" crate.

%package     -n %{name}+color-devel
Summary:        utilities for `crossterm`, without ties to `termion`
BuildArch:      noarch
%description -n %{name}+color-devel

This package contains library source intended for building other packages which
use the "color" feature of the "%{crate}" crate.

%package     -n %{name}+crossterm-devel
Summary:        utilities for `crossterm`, without ties to `termion`
BuildArch:      noarch
%description -n %{name}+crossterm-devel

This package contains library source intended for building other packages which
use the "crossterm" feature of the "%{crate}" crate.

%package     -n %{name}+futures-channel-devel
Summary:        utilities for `crossterm`, without ties to `termion`
BuildArch:      noarch
%description -n %{name}+futures-channel-devel

This package contains library source intended for building other packages which
use the "futures-channel" feature of the "%{crate}" crate.

%package     -n %{name}+futures-core-devel
Summary:        utilities for `crossterm`, without ties to `termion`
BuildArch:      noarch
%description -n %{name}+futures-core-devel

This package contains library source intended for building other packages which
use the "futures-core" feature of the "%{crate}" crate.

%package     -n %{name}+futures-lite-devel
Summary:        utilities for `crossterm`, without ties to `termion`
BuildArch:      noarch
%description -n %{name}+futures-lite-devel

This package contains library source intended for building other packages which
use the "futures-lite" feature of the "%{crate}" crate.

%package     -n %{name}+input-async-devel
Summary:        utilities for `crossterm`, without ties to `termion`
BuildArch:      noarch
%description -n %{name}+input-async-devel

This package contains library source intended for building other packages which
use the "input-async" feature of the "%{crate}" crate.

%package     -n %{name}+input-async-crossterm-devel
Summary:        utilities for `crossterm`, without ties to `termion`
BuildArch:      noarch
%description -n %{name}+input-async-crossterm-devel

This package contains library source intended for building other packages which
use the "input-async-crossterm" feature of the "%{crate}" crate.

%package     -n %{name}+tui-devel
Summary:        utilities for `crossterm`, without ties to `termion`
BuildArch:      noarch
%description -n %{name}+tui-devel

This package contains library source intended for building other packages which
use the "tui" feature of the "%{crate}" crate.

%package     -n %{name}+tui-crossterm-devel
Summary:        utilities for `crossterm`, without ties to `termion`
BuildArch:      noarch
%description -n %{name}+tui-crossterm-devel

This package contains library source intended for building other packages which
use the "tui-crossterm" feature of the "%{crate}" crate.

%package     -n %{name}+tui-crossterm-backend-devel
Summary:        utilities for `crossterm`, without ties to `termion`
BuildArch:      noarch
%description -n %{name}+tui-crossterm-backend-devel

This package contains library source intended for building other packages which
use the "tui-crossterm-backend" feature of the "%{crate}" crate.

%package     -n %{name}+tui-react-devel
Summary:        utilities for `crossterm`, without ties to `termion`
BuildArch:      noarch
%description -n %{name}+tui-react-devel

This package contains library source intended for building other packages which
use the "tui-react" feature of the "%{crate}" crate.

%package     -n %{name}+tui-react-crossterm-devel
Summary:        utilities for `crossterm`, without ties to `termion`
BuildArch:      noarch
%description -n %{name}+tui-react-crossterm-devel

This package contains library source intended for building other packages which
use the "tui-react-crossterm" feature of the "%{crate}" crate.

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
%files -n rust-crosstermion-devel -f %{oreon_filedir}/rust-crosstermion-devel.list

%changelog

%autochangelog
