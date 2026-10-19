%global source0_hash 8a6f157065790a3ed2f88679250419b5cdd96e714a0d65f7797fd337186e96bb
%bcond check 0
%global debug_package %{nil}
%global crate hyper
Name:           rust-hyper0.13
Version:        0.13.10
Release:        1%{?dist}
Summary:        A fast and correct HTTP library.
License:        MIT
URL:            https://crates.io/crates/hyper
Source0:        https://static.crates.io/crates/hyper/hyper-%{version}.crate
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
Summary:        A fast and correct HTTP library.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+__internal_happy_eyeballs_tests-devel
Summary:        A fast and correct HTTP library.
BuildArch:      noarch
%description -n %{name}+__internal_happy_eyeballs_tests-devel

This package contains library source intended for building other packages which
use the "__internal_happy_eyeballs_tests" feature of the "%{crate}" crate.

%package     -n %{name}+nightly-devel
Summary:        A fast and correct HTTP library.
BuildArch:      noarch
%description -n %{name}+nightly-devel

This package contains library source intended for building other packages which
use the "nightly" feature of the "%{crate}" crate.

%package     -n %{name}+runtime-devel
Summary:        A fast and correct HTTP library.
BuildArch:      noarch
%description -n %{name}+runtime-devel

This package contains library source intended for building other packages which
use the "runtime" feature of the "%{crate}" crate.

%package     -n %{name}+socket2-devel
Summary:        A fast and correct HTTP library.
BuildArch:      noarch
%description -n %{name}+socket2-devel

This package contains library source intended for building other packages which
use the "socket2" feature of the "%{crate}" crate.

%package     -n %{name}+stream-devel
Summary:        A fast and correct HTTP library.
BuildArch:      noarch
%description -n %{name}+stream-devel

This package contains library source intended for building other packages which
use the "stream" feature of the "%{crate}" crate.

%package     -n %{name}+tcp-devel
Summary:        A fast and correct HTTP library.
BuildArch:      noarch
%description -n %{name}+tcp-devel

This package contains library source intended for building other packages which
use the "tcp" feature of the "%{crate}" crate.

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
%files -n rust-hyper0.13-devel -f %{oreon_filedir}/rust-hyper0.13-devel.list

%changelog

%autochangelog
