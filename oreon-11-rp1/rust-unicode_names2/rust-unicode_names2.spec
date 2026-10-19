%global source0_hash d1673eca9782c84de5f81b82e4109dcfb3611c8ba0d52930ec4a9478f547b2dd
%bcond check 1
%global debug_package %{nil}
%global crate unicode_names2
Name:           rust-unicode_names2
Version:        1.3.0
Release:        1%{?dist}
Summary:        Map characters to and from their name given in the Unicode standard
License:        (MIT OR Apache-2.0) AND Unicode-DFS-2016
URL:            https://crates.io/crates/unicode_names2
Source0:        https://static.crates.io/crates/unicode_names2/unicode_names2-%{version}.crate
Patch:          unicode_names2-fix-metadata.diff
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
Summary:        Map characters to and from their name given in the Unicode standard
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+generator-timing-devel
Summary:        Map characters to and from their name given in the Unicode standard
BuildArch:      noarch
%description -n %{name}+generator-timing-devel

This package contains library source intended for building other packages which
use the "generator-timing" feature of the "%{crate}" crate.

%package     -n %{name}+no_std-devel
Summary:        Map characters to and from their name given in the Unicode standard
BuildArch:      noarch
%description -n %{name}+no_std-devel

This package contains library source intended for building other packages which
use the "no_std" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-devel
Summary:        Map characters to and from their name given in the Unicode standard
BuildArch:      noarch
%description -n %{name}+unstable-devel

This package contains library source intended for building other packages which
use the "unstable" feature of the "%{crate}" crate.

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
%files -n rust-unicode_names2-devel -f %{oreon_filedir}/rust-unicode_names2-devel.list

%changelog

%autochangelog
