%global source0_hash 0369ee1ad671834580515889b80f2ea915f23b8be8d0daa4bbaf2ac5c7590835
%bcond check 1
%global debug_package %{nil}
%global crate ctr
Name:           rust-ctr0.9
Version:        0.9.2
Release:        1%{?dist}
Summary:        CTR block modes of operation
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/ctr
Source0:        https://static.crates.io/crates/ctr/ctr-%{version}.crate
Patch:          ctr-fix-metadata.diff
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
Summary:        CTR block modes of operation
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        CTR block modes of operation
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+block-padding-devel
Summary:        CTR block modes of operation
BuildArch:      noarch
%description -n %{name}+block-padding-devel

This package contains library source intended for building other packages which
use the "block-padding" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        CTR block modes of operation
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+zeroize-devel
Summary:        CTR block modes of operation
BuildArch:      noarch
%description -n %{name}+zeroize-devel

This package contains library source intended for building other packages which
use the "zeroize" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
sed --regexp-extended --in-place 's@^mod gost;$@// &@' tests/mod.rs
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
%files -n rust-ctr0.9-devel -f %{oreon_filedir}/rust-ctr0.9-devel.list

%changelog

%autochangelog
