%global source0_hash 2990d9ea5967266ea0ccf413a4aa5c42a93dbcfda9cb49a97de6931726b12566
%bcond check 0
%global debug_package %{nil}
%global crate vergen
Name:           rust-vergen
Version:        8.3.2
Release:        1%{?dist}
Summary:        Generate cargo:rustc-env instructions for use with env!
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/vergen
Source0:        https://static.crates.io/crates/vergen/vergen-%{version}.crate
Patch:          vergen-fix-metadata.diff
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
Summary:        Generate cargo:rustc-env instructions for use with env!
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+build-devel
Summary:        Generate cargo:rustc-env instructions for use with env!
BuildArch:      noarch
%description -n %{name}+build-devel

This package contains library source intended for building other packages which
use the "build" feature of the "%{crate}" crate.

%package     -n %{name}+cargo-devel
Summary:        Generate cargo:rustc-env instructions for use with env!
BuildArch:      noarch
%description -n %{name}+cargo-devel

This package contains library source intended for building other packages which
use the "cargo" feature of the "%{crate}" crate.

%package     -n %{name}+cargo_metadata-devel
Summary:        Generate cargo:rustc-env instructions for use with env!
BuildArch:      noarch
%description -n %{name}+cargo_metadata-devel

This package contains library source intended for building other packages which
use the "cargo_metadata" feature of the "%{crate}" crate.

%package     -n %{name}+cfg-if-devel
Summary:        Generate cargo:rustc-env instructions for use with env!
BuildArch:      noarch
%description -n %{name}+cfg-if-devel

This package contains library source intended for building other packages which
use the "cfg-if" feature of the "%{crate}" crate.

%package     -n %{name}+git-devel
Summary:        Generate cargo:rustc-env instructions for use with env!
BuildArch:      noarch
%description -n %{name}+git-devel

This package contains library source intended for building other packages which
use the "git" feature of the "%{crate}" crate.

%package     -n %{name}+git2-devel
Summary:        Generate cargo:rustc-env instructions for use with env!
BuildArch:      noarch
%description -n %{name}+git2-devel

This package contains library source intended for building other packages which
use the "git2" feature of the "%{crate}" crate.

%package     -n %{name}+git2-rs-devel
Summary:        Generate cargo:rustc-env instructions for use with env!
BuildArch:      noarch
%description -n %{name}+git2-rs-devel

This package contains library source intended for building other packages which
use the "git2-rs" feature of the "%{crate}" crate.

%package     -n %{name}+gitcl-devel
Summary:        Generate cargo:rustc-env instructions for use with env!
BuildArch:      noarch
%description -n %{name}+gitcl-devel

This package contains library source intended for building other packages which
use the "gitcl" feature of the "%{crate}" crate.

%package     -n %{name}+gitoxide-devel
Summary:        Generate cargo:rustc-env instructions for use with env!
BuildArch:      noarch
%description -n %{name}+gitoxide-devel

This package contains library source intended for building other packages which
use the "gitoxide" feature of the "%{crate}" crate.

%package     -n %{name}+gix-devel
Summary:        Generate cargo:rustc-env instructions for use with env!
BuildArch:      noarch
%description -n %{name}+gix-devel

This package contains library source intended for building other packages which
use the "gix" feature of the "%{crate}" crate.

%package     -n %{name}+regex-devel
Summary:        Generate cargo:rustc-env instructions for use with env!
BuildArch:      noarch
%description -n %{name}+regex-devel

This package contains library source intended for building other packages which
use the "regex" feature of the "%{crate}" crate.

%package     -n %{name}+rustc-devel
Summary:        Generate cargo:rustc-env instructions for use with env!
BuildArch:      noarch
%description -n %{name}+rustc-devel

This package contains library source intended for building other packages which
use the "rustc" feature of the "%{crate}" crate.

%package     -n %{name}+rustc_version-devel
Summary:        Generate cargo:rustc-env instructions for use with env!
BuildArch:      noarch
%description -n %{name}+rustc_version-devel

This package contains library source intended for building other packages which
use the "rustc_version" feature of the "%{crate}" crate.

%package     -n %{name}+si-devel
Summary:        Generate cargo:rustc-env instructions for use with env!
BuildArch:      noarch
%description -n %{name}+si-devel

This package contains library source intended for building other packages which
use the "si" feature of the "%{crate}" crate.

%package     -n %{name}+sysinfo-devel
Summary:        Generate cargo:rustc-env instructions for use with env!
BuildArch:      noarch
%description -n %{name}+sysinfo-devel

This package contains library source intended for building other packages which
use the "sysinfo" feature of the "%{crate}" crate.

%package     -n %{name}+time-devel
Summary:        Generate cargo:rustc-env instructions for use with env!
BuildArch:      noarch
%description -n %{name}+time-devel

This package contains library source intended for building other packages which
use the "time" feature of the "%{crate}" crate.

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
%files -n rust-vergen-devel -f %{oreon_filedir}/rust-vergen-devel.list

%changelog

%autochangelog
