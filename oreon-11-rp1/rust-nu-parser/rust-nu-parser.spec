%global source0_hash 9672e0c0192a07bcde2fb2ebc5316afedeee1d1a717407b2c4dcae238aae0b98
%bcond check 1
%global debug_package %{nil}
%global crate nu-parser
Name:           rust-nu-parser
Version:        0.115.1
Release:        1%{?dist}
Summary:        Nushell's parser
License:        MIT
URL:            https://crates.io/crates/nu-parser
Source0:        https://static.crates.io/crates/nu-parser/nu-parser-%{version}.crate
Patch:          nu-parser-fix-metadata.diff
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
Summary:        Nushell's parser
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+nu-plugin-engine-devel
Summary:        Nushell's parser
BuildArch:      noarch
%description -n %{name}+nu-plugin-engine-devel

This package contains library source intended for building other packages which
use the "nu-plugin-engine" feature of the "%{crate}" crate.

%package     -n %{name}+plugin-devel
Summary:        Nushell's parser
BuildArch:      noarch
%description -n %{name}+plugin-devel

This package contains library source intended for building other packages which
use the "plugin" feature of the "%{crate}" crate.

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
%files -n rust-nu-parser-devel -f %{oreon_filedir}/rust-nu-parser-devel.list

%changelog

%autochangelog
