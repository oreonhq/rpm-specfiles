%global source0_hash 76d283dc7e8c901e79e32d077866eaf599156cbf427fffa8289aecc52c5c3f63
%bcond check 1
%global debug_package %{nil}
%global crate uzers
Name:           rust-uzers0.11
Version:        0.11.3
Release:        1%{?dist}
Summary:        Library for accessing Unix users and groups
License:        MIT
URL:            https://crates.io/crates/uzers
Source0:        https://static.crates.io/crates/uzers/uzers-%{version}.crate
Patch:          uzers-fix-metadata.diff
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
Summary:        Library for accessing Unix users and groups
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+cache-devel
Summary:        Library for accessing Unix users and groups
BuildArch:      noarch
%description -n %{name}+cache-devel

This package contains library source intended for building other packages which
use the "cache" feature of the "%{crate}" crate.

%package     -n %{name}+log-devel
Summary:        Library for accessing Unix users and groups
BuildArch:      noarch
%description -n %{name}+log-devel

This package contains library source intended for building other packages which
use the "log" feature of the "%{crate}" crate.

%package     -n %{name}+logging-devel
Summary:        Library for accessing Unix users and groups
BuildArch:      noarch
%description -n %{name}+logging-devel

This package contains library source intended for building other packages which
use the "logging" feature of the "%{crate}" crate.

%package     -n %{name}+mock-devel
Summary:        Library for accessing Unix users and groups
BuildArch:      noarch
%description -n %{name}+mock-devel

This package contains library source intended for building other packages which
use the "mock" feature of the "%{crate}" crate.

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
%files -n rust-uzers0.11-devel -f %{oreon_filedir}/rust-uzers0.11-devel.list

%changelog

%autochangelog
