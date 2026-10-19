%global source0_hash 1fb5288fac706d3ea3e4e2ba9ec38b78743b8c02f422e18cb342299cfd6ab7e8
%bcond check 0
%global debug_package %{nil}
%global crate gix-revision
Name:           rust-gix-revision0.45
Version:        0.45.0
Release:        1%{?dist}
Summary:        A crate of the gitoxide project dealing with finding names for revisi...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/gix-revision
Source0:        https://static.crates.io/crates/gix-revision/gix-revision-%{version}.crate
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
Summary:        A crate of the gitoxide project dealing with finding names for revisi...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+bitflags-devel
Summary:        A crate of the gitoxide project dealing with finding names for revisi...
BuildArch:      noarch
%description -n %{name}+bitflags-devel

This package contains library source intended for building other packages which
use the "bitflags" feature of the "%{crate}" crate.

%package     -n %{name}+describe-devel
Summary:        A crate of the gitoxide project dealing with finding names for revisi...
BuildArch:      noarch
%description -n %{name}+describe-devel

This package contains library source intended for building other packages which
use the "describe" feature of the "%{crate}" crate.

%package     -n %{name}+document-features-devel
Summary:        A crate of the gitoxide project dealing with finding names for revisi...
BuildArch:      noarch
%description -n %{name}+document-features-devel

This package contains library source intended for building other packages which
use the "document-features" feature of the "%{crate}" crate.

%package     -n %{name}+gix-hashtable-devel
Summary:        A crate of the gitoxide project dealing with finding names for revisi...
BuildArch:      noarch
%description -n %{name}+gix-hashtable-devel

This package contains library source intended for building other packages which
use the "gix-hashtable" feature of the "%{crate}" crate.

%package     -n %{name}+gix-trace-devel
Summary:        A crate of the gitoxide project dealing with finding names for revisi...
BuildArch:      noarch
%description -n %{name}+gix-trace-devel

This package contains library source intended for building other packages which
use the "gix-trace" feature of the "%{crate}" crate.

%package     -n %{name}+merge_base-devel
Summary:        A crate of the gitoxide project dealing with finding names for revisi...
BuildArch:      noarch
%description -n %{name}+merge_base-devel

This package contains library source intended for building other packages which
use the "merge_base" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        A crate of the gitoxide project dealing with finding names for revisi...
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+sha1-devel
Summary:        A crate of the gitoxide project dealing with finding names for revisi...
BuildArch:      noarch
%description -n %{name}+sha1-devel

This package contains library source intended for building other packages which
use the "sha1" feature of the "%{crate}" crate.

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
%files -n rust-gix-revision0.45-devel -f %{oreon_filedir}/rust-gix-revision0.45-devel.list

%changelog

%autochangelog
