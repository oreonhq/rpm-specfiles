%global source0_hash 7df058c713841ad818f1dc5d3fd88063241cc61f49f5fbea4b951e8cf5a8d71d
%bcond check 0
%global debug_package %{nil}
%global crate unicode-properties
Name:           rust-unicode-properties
Version:        0.1.4
Release:        1%{?dist}
Summary:        Query character Unicode properties according to
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/unicode-properties
Source0:        https://static.crates.io/crates/unicode-properties/unicode-properties-%{version}.crate
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
Summary:        Query character Unicode properties according to
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+emoji-devel
Summary:        Query character Unicode properties according to
BuildArch:      noarch
%description -n %{name}+emoji-devel

This package contains library source intended for building other packages which
use the "emoji" feature of the "%{crate}" crate.

%package     -n %{name}+general-category-devel
Summary:        Query character Unicode properties according to
BuildArch:      noarch
%description -n %{name}+general-category-devel

This package contains library source intended for building other packages which
use the "general-category" feature of the "%{crate}" crate.

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
%files -n rust-unicode-properties-devel -f %{oreon_filedir}/rust-unicode-properties-devel.list

%changelog

%autochangelog
