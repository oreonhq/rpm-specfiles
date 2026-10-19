%global source0_hash 57206b407293d2bcd3af849ce869d52068623f19e1b5ff8e8778e3309439682b
%bcond check 0
%global debug_package %{nil}
%global crate pulldown-cmark
Name:           rust-pulldown-cmark
Version:        0.9.6
Release:        1%{?dist}
Summary:        A pull parser for CommonMark
License:        MIT
URL:            https://crates.io/crates/pulldown-cmark
Source0:        https://static.crates.io/crates/pulldown-cmark/pulldown-cmark-%{version}.crate
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
Summary:        A pull parser for CommonMark
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+gen-tests-devel
Summary:        A pull parser for CommonMark
BuildArch:      noarch
%description -n %{name}+gen-tests-devel

This package contains library source intended for building other packages which
use the "gen-tests" feature of the "%{crate}" crate.

%package     -n %{name}+simd-devel
Summary:        A pull parser for CommonMark
BuildArch:      noarch
%description -n %{name}+simd-devel

This package contains library source intended for building other packages which
use the "simd" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build
%install
%cargo_install
rm -f %{buildroot}%{_bindir}/pulldown-cmark
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-pulldown-cmark-devel -f %{oreon_filedir}/rust-pulldown-cmark-devel.list

%changelog

%autochangelog
