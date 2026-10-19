%global source0_hash b4ac048d71ede7ee76d585517add45da530660ef4390e49b098733c6e897f254
%bcond check 1
%global debug_package %{nil}
%global crate unicode-width
Name:           rust-unicode-width
Version:        0.2.2
Release:        1%{?dist}
Summary:        Determine displayed width of 'char' and 'str' types
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/unicode-width
Source0:        https://static.crates.io/crates/unicode-width/unicode-width-%{version}.crate
Patch:          unicode-width-fix-metadata.diff
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
Summary:        Determine displayed width of 'char' and 'str' types
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+cjk-devel
Summary:        Determine displayed width of 'char' and 'str' types
BuildArch:      noarch
%description -n %{name}+cjk-devel

This package contains library source intended for building other packages which
use the "cjk" feature of the "%{crate}" crate.

%package     -n %{name}+no_std-devel
Summary:        Determine displayed width of 'char' and 'str' types
BuildArch:      noarch
%description -n %{name}+no_std-devel

This package contains library source intended for building other packages which
use the "no_std" feature of the "%{crate}" crate.

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
%files -n rust-unicode-width-devel -f %{oreon_filedir}/rust-unicode-width-devel.list

%changelog

%autochangelog
