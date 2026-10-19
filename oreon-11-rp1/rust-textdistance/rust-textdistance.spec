%global source0_hash aa672c55ab69f787dbc9126cc387dbe57fdd595f585e4524cf89018fa44ab819
%bcond check 1
%global debug_package %{nil}
%global cargo_install_bin 0
%global crate textdistance
Name:           rust-textdistance
Version:        1.1.1
Release:        1%{?dist}
Summary:        Lots of algorithms to compare how similar two sequences are
License:        MIT
URL:            https://crates.io/crates/textdistance
Source0:        https://static.crates.io/crates/textdistance/textdistance-%{version}.crate
Patch:          textdistance-fix-metadata.diff
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
Summary:        Lots of algorithms to compare how similar two sequences are
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Lots of algorithms to compare how similar two sequences are
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

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
%files -n rust-textdistance-devel -f %{oreon_filedir}/rust-textdistance-devel.list

%changelog

%autochangelog
