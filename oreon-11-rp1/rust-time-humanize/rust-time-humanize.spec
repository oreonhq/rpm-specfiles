%global source0_hash 3e32d019b4f7c100bcd5494e40a27119d45b71fba2b07a4684153129279a4647
%bcond check 1
%global debug_package %{nil}
%global crate time-humanize
Name:           rust-time-humanize
Version:        0.1.3
Release:        1%{?dist}
Summary:        Display time in a human readable manner
License:        MIT
URL:            https://crates.io/crates/time-humanize
Source0:        https://static.crates.io/crates/time-humanize/time-humanize-%{version}.crate
Patch10:        https://github.com/HallerPatrick/time-humanize/pull/3.patch
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
Summary:        Display time in a human readable manner
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+time-devel
Summary:        Display time in a human readable manner
BuildArch:      noarch
%description -n %{name}+time-devel

This package contains library source intended for building other packages which
use the "time" feature of the "%{crate}" crate.

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

%cargo_test -- -- --skip test_duration_from_system_time_since_epoch
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-time-humanize-devel -f %{oreon_filedir}/rust-time-humanize-devel.list

%changelog

%autochangelog
