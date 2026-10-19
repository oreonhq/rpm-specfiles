%global source0_hash 5febe7a2ade5c7d98eb8b75f946c046b335324b06a14ea0998271504134c05bf
%bcond check 0
%global debug_package %{nil}
%global crate hyphenation_commons
Name:           rust-hyphenation_commons
Version:        0.8.4
Release:        1%{?dist}
Summary:        Proemial code for the `hyphenation` library
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/hyphenation_commons
Source0:        https://static.crates.io/crates/hyphenation_commons/hyphenation_commons-%{version}.crate
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
Summary:        Proemial code for the `hyphenation` library
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

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
%files -n rust-hyphenation_commons-devel -f %{oreon_filedir}/rust-hyphenation_commons-devel.list

%changelog

%autochangelog
