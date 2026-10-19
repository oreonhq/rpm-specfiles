%global source0_hash 0b8275fb1afee25b4111d2dc8b5c505dbbc4afd0b990cb96deb2d88bff8be18d
%bcond check 0
%global debug_package %{nil}
%global crate uzers
Name:           rust-uzers
Version:        0.12.2
Release:        1%{?dist}
Summary:        Continuation of users, a library for accessing Unix users and groups
License:        MIT
URL:            https://crates.io/crates/uzers
Source0:        https://static.crates.io/crates/uzers/uzers-%{version}.crate
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
Summary:        Continuation of users, a library for accessing Unix users and groups
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+cache-devel
Summary:        Continuation of users, a library for accessing Unix users and groups
BuildArch:      noarch
%description -n %{name}+cache-devel

This package contains library source intended for building other packages which
use the "cache" feature of the "%{crate}" crate.

%package     -n %{name}+log-devel
Summary:        Continuation of users, a library for accessing Unix users and groups
BuildArch:      noarch
%description -n %{name}+log-devel

This package contains library source intended for building other packages which
use the "log" feature of the "%{crate}" crate.

%package     -n %{name}+logging-devel
Summary:        Continuation of users, a library for accessing Unix users and groups
BuildArch:      noarch
%description -n %{name}+logging-devel

This package contains library source intended for building other packages which
use the "logging" feature of the "%{crate}" crate.

%package     -n %{name}+mock-devel
Summary:        Continuation of users, a library for accessing Unix users and groups
BuildArch:      noarch
%description -n %{name}+mock-devel

This package contains library source intended for building other packages which
use the "mock" feature of the "%{crate}" crate.

%package     -n %{name}+test-integration-devel
Summary:        Continuation of users, a library for accessing Unix users and groups
BuildArch:      noarch
%description -n %{name}+test-integration-devel

This package contains library source intended for building other packages which
use the "test-integration" feature of the "%{crate}" crate.

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
%files -n rust-uzers-devel -f %{oreon_filedir}/rust-uzers-devel.list

%changelog

%autochangelog
