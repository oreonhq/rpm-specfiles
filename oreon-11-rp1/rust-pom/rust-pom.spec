%global source0_hash 6c972d8f86e943ad532d0b04e8965a749ad1d18bb981a9c7b3ae72fe7fd7744b
%bcond check 0
%global debug_package %{nil}
%global crate pom
Name:           rust-pom
Version:        3.4.0
Release:        1%{?dist}
Summary:        PEG parser combinators using operator overloading without macros
License:        MIT
URL:            https://crates.io/crates/pom
Source0:        https://static.crates.io/crates/pom/pom-%{version}.crate
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
Summary:        PEG parser combinators using operator overloading without macros
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+trace-devel
Summary:        PEG parser combinators using operator overloading without macros
BuildArch:      noarch
%description -n %{name}+trace-devel

This package contains library source intended for building other packages which
use the "trace" feature of the "%{crate}" crate.

%package     -n %{name}+utf8-devel
Summary:        PEG parser combinators using operator overloading without macros
BuildArch:      noarch
%description -n %{name}+utf8-devel

This package contains library source intended for building other packages which
use the "utf8" feature of the "%{crate}" crate.

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
%files -n rust-pom-devel -f %{oreon_filedir}/rust-pom-devel.list

%changelog

%autochangelog
