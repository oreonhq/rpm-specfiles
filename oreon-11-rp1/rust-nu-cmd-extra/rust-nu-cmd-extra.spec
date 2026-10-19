%global source0_hash 2a5307625da907d2e4e80c2c4288307438753bfa1341d2ea7e5af0d9dd775331
%bcond check 1
%global debug_package %{nil}
%global crate nu-cmd-extra
Name:           rust-nu-cmd-extra
Version:        0.115.1
Release:        1%{?dist}
Summary:        Nushell's extra commands that are not part of the 1.0 api standard
License:        MIT
URL:            https://crates.io/crates/nu-cmd-extra
Source0:        https://static.crates.io/crates/nu-cmd-extra/nu-cmd-extra-%{version}.crate
Patch:          nu-cmd-extra-fix-metadata.diff
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
Summary:        Nushell's extra commands that are not part of the 1.0 api standard
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

%{cargo_test -- -- %{shrink:
    --skip commands::bits::into::
    --skip commands::bytes::ends_with::
    --skip commands::bytes::starts_with::
}}
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-nu-cmd-extra-devel -f %{oreon_filedir}/rust-nu-cmd-extra-devel.list

%changelog

%autochangelog
