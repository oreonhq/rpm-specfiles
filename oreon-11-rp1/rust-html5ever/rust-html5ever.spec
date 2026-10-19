%global source0_hash 456a1a377e608e555d22ddab27ac0114bc7a7b4199078108e34c2aeae6c9b130
%bcond check 1
%global debug_package %{nil}
%global crate html5ever
Name:           rust-html5ever
Version:        0.40.1
Release:        1%{?dist}
Summary:        High-performance browser-grade HTML5 parser
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/html5ever
Source0:        https://static.crates.io/crates/html5ever/html5ever-%{version}.crate
Patch:          html5ever-fix-metadata.diff
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
Summary:        High-performance browser-grade HTML5 parser
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+trace_tokenizer-devel
Summary:        High-performance browser-grade HTML5 parser
BuildArch:      noarch
%description -n %{name}+trace_tokenizer-devel

This package contains library source intended for building other packages which
use the "trace_tokenizer" feature of the "%{crate}" crate.

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
%files -n rust-html5ever-devel -f %{oreon_filedir}/rust-html5ever-devel.list

%changelog

%autochangelog
