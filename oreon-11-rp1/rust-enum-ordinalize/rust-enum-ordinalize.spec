%global source0_hash 89dd01549b09589510cf0647475075d12071456586d70f5c75c98ae2a5537677
%bcond check 1
%global debug_package %{nil}
%global crate enum-ordinalize
Name:           rust-enum-ordinalize
Version:        4.4.2
Release:        1%{?dist}
Summary:        Construct enum variant from its ordinal
License:        MIT
URL:            https://crates.io/crates/enum-ordinalize
Source0:        https://static.crates.io/crates/enum-ordinalize/enum-ordinalize-%{version}.crate
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
Summary:        Construct enum variant from its ordinal
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+derive-devel
Summary:        Construct enum variant from its ordinal
BuildArch:      noarch
%description -n %{name}+derive-devel

This package contains library source intended for building other packages which
use the "derive" feature of the "%{crate}" crate.

%package     -n %{name}+nightly-test-devel
Summary:        Construct enum variant from its ordinal
BuildArch:      noarch
%description -n %{name}+nightly-test-devel

This package contains library source intended for building other packages which
use the "nightly-test" feature of the "%{crate}" crate.

%package     -n %{name}+traits-devel
Summary:        Construct enum variant from its ordinal
BuildArch:      noarch
%description -n %{name}+traits-devel

This package contains library source intended for building other packages which
use the "traits" feature of the "%{crate}" crate.

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
%files -n rust-enum-ordinalize-devel -f %{oreon_filedir}/rust-enum-ordinalize-devel.list

%changelog

%autochangelog
