%global source0_hash 6c297679cb867470fa8c9f67dbba74a78d78e3e98d7cf2b08d6d71540f797332
%bcond check 0
%global debug_package %{nil}
%global crate raw-cpuid
Name:           rust-raw-cpuid
Version:        10.7.0
Release:        1%{?dist}
Summary:        A library to parse the x86 CPUID instruction, written in rust with no...
License:        MIT
URL:            https://crates.io/crates/raw-cpuid
Source0:        https://static.crates.io/crates/raw-cpuid/raw-cpuid-%{version}.crate
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

%package     -n %{name}+clap-devel
Summary:        A library to parse the x86 CPUID instruction, written in rust with no...
BuildArch:      noarch
%description -n %{name}+clap-devel

This package contains library source intended for building other packages which
use the "clap" feature of the "%{crate}" crate.

%package     -n %{name}+cli-devel
Summary:        A library to parse the x86 CPUID instruction, written in rust with no...
BuildArch:      noarch
%description -n %{name}+cli-devel

This package contains library source intended for building other packages which
use the "cli" feature of the "%{crate}" crate.

%package     -n %{name}+display-devel
Summary:        A library to parse the x86 CPUID instruction, written in rust with no...
BuildArch:      noarch
%description -n %{name}+display-devel

This package contains library source intended for building other packages which
use the "display" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        A library to parse the x86 CPUID instruction, written in rust with no...
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+serde_derive-devel
Summary:        A library to parse the x86 CPUID instruction, written in rust with no...
BuildArch:      noarch
%description -n %{name}+serde_derive-devel

This package contains library source intended for building other packages which
use the "serde_derive" feature of the "%{crate}" crate.

%package     -n %{name}+serde_json-devel
Summary:        A library to parse the x86 CPUID instruction, written in rust with no...
BuildArch:      noarch
%description -n %{name}+serde_json-devel

This package contains library source intended for building other packages which
use the "serde_json" feature of the "%{crate}" crate.

%package     -n %{name}+serialize-devel
Summary:        A library to parse the x86 CPUID instruction, written in rust with no...
BuildArch:      noarch
%description -n %{name}+serialize-devel

This package contains library source intended for building other packages which
use the "serialize" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        A library to parse the x86 CPUID instruction, written in rust with no...
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+termimad-devel
Summary:        A library to parse the x86 CPUID instruction, written in rust with no...
BuildArch:      noarch
%description -n %{name}+termimad-devel

This package contains library source intended for building other packages which
use the "termimad" feature of the "%{crate}" crate.

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
%files -n rust-raw-cpuid-devel -f %{oreon_filedir}/rust-raw-cpuid-devel.list

%changelog

%autochangelog
