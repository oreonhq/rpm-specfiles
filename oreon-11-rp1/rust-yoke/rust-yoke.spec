%global source0_hash 709fe23a0424b6a435d82152b1bd3fdfb0833487d5fa90d05d42762a9891fef5
%bcond check 0
%global debug_package %{nil}
%global crate yoke
Name:           rust-yoke
Version:        0.8.3
Release:        1%{?dist}
Summary:        Abstraction allowing borrowed data to be carried along with the backi...
License:        Unicode-3.0
URL:            https://crates.io/crates/yoke
Source0:        https://static.crates.io/crates/yoke/yoke-%{version}.crate
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
Summary:        Abstraction allowing borrowed data to be carried along with the backi...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Abstraction allowing borrowed data to be carried along with the backi...
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+derive-devel
Summary:        Abstraction allowing borrowed data to be carried along with the backi...
BuildArch:      noarch
%description -n %{name}+derive-devel

This package contains library source intended for building other packages which
use the "derive" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Abstraction allowing borrowed data to be carried along with the backi...
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+zerofrom-devel
Summary:        Abstraction allowing borrowed data to be carried along with the backi...
BuildArch:      noarch
%description -n %{name}+zerofrom-devel

This package contains library source intended for building other packages which
use the "zerofrom" feature of the "%{crate}" crate.

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
%files -n rust-yoke-devel -f %{oreon_filedir}/rust-yoke-devel.list

%changelog

%autochangelog
