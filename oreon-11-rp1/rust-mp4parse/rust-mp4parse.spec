%global source0_hash 63a35203d3c6ce92d5251c77520acb2e57108c88728695aa883f70023624c570
%bcond check 0
%global debug_package %{nil}
%global crate mp4parse
Name:           rust-mp4parse
Version:        0.17.0
Release:        1%{?dist}
Summary:        Parser for ISO base media file format (mp4)
License:        MPL-2.0
URL:            https://crates.io/crates/mp4parse
Source0:        https://static.crates.io/crates/mp4parse/mp4parse-%{version}.crate
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

%package     -n %{name}+3gpp-devel
Summary:        Parser for ISO base media file format (mp4)
BuildArch:      noarch
%description -n %{name}+3gpp-devel

This package contains library source intended for building other packages which
use the "3gpp" feature of the "%{crate}" crate.

%package     -n %{name}+meta-xml-devel
Summary:        Parser for ISO base media file format (mp4)
BuildArch:      noarch
%description -n %{name}+meta-xml-devel

This package contains library source intended for building other packages which
use the "meta-xml" feature of the "%{crate}" crate.

%package     -n %{name}+missing-pixi-permitted-devel
Summary:        Parser for ISO base media file format (mp4)
BuildArch:      noarch
%description -n %{name}+missing-pixi-permitted-devel

This package contains library source intended for building other packages which
use the "missing-pixi-permitted" feature of the "%{crate}" crate.

%package     -n %{name}+mp4v-devel
Summary:        Parser for ISO base media file format (mp4)
BuildArch:      noarch
%description -n %{name}+mp4v-devel

This package contains library source intended for building other packages which
use the "mp4v" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-api-devel
Summary:        Parser for ISO base media file format (mp4)
BuildArch:      noarch
%description -n %{name}+unstable-api-devel

This package contains library source intended for building other packages which
use the "unstable-api" feature of the "%{crate}" crate.

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
%files -n rust-mp4parse-devel -f %{oreon_filedir}/rust-mp4parse-devel.list

%changelog

%autochangelog
