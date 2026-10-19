%global source0_hash a9ce9099a85f468663d3225bf87e85d0548968441e1db12248b996b24f0f5b5a
%bcond check 1
%global debug_package %{nil}
%global crate interim
Name:           rust-interim
Version:        0.2.1
Release:        1%{?dist}
Summary:        Parses simple English dates, inspired by Linux date command
License:        MIT
URL:            https://crates.io/crates/interim
Source0:        https://static.crates.io/crates/interim/interim-%{version}.crate
Patch:          interim-fix-metadata.diff
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
Summary:        Parses simple English dates, inspired by Linux date command
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+chrono_0_4-devel
Summary:        Parses simple English dates, inspired by Linux date command
BuildArch:      noarch
%description -n %{name}+chrono_0_4-devel

This package contains library source intended for building other packages which
use the "chrono_0_4" feature of the "%{crate}" crate.

%package     -n %{name}+jiff_0_2-devel
Summary:        Parses simple English dates, inspired by Linux date command
BuildArch:      noarch
%description -n %{name}+jiff_0_2-devel

This package contains library source intended for building other packages which
use the "jiff_0_2" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Parses simple English dates, inspired by Linux date command
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+time_0_3-devel
Summary:        Parses simple English dates, inspired by Linux date command
BuildArch:      noarch
%description -n %{name}+time_0_3-devel

This package contains library source intended for building other packages which
use the "time_0_3" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build -a
%install
%cargo_install -a
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test -a
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-interim-devel -f %{oreon_filedir}/rust-interim-devel.list

%changelog

%autochangelog
