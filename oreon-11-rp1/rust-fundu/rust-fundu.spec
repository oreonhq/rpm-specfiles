%global source0_hash e47ed3102262b937cdbc46cc412c58f2243b8d13989657d0c9f027eb03168aca
%bcond check 1
%global debug_package %{nil}
%global crate fundu
Name:           rust-fundu
Version:        2.1.1
Release:        1%{?dist}
Summary:        Configurable, precise and fast rust string parser to a Duration
License:        MIT
URL:            https://crates.io/crates/fundu
Source0:        https://static.crates.io/crates/fundu/fundu-%{version}.crate
Patch:          fundu-fix-metadata.diff
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
Summary:        Configurable, precise and fast rust string parser to a Duration
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+base-devel
Summary:        Configurable, precise and fast rust string parser to a Duration
BuildArch:      noarch
%description -n %{name}+base-devel

This package contains library source intended for building other packages which
use the "base" feature of the "%{crate}" crate.

%package     -n %{name}+chrono-devel
Summary:        Configurable, precise and fast rust string parser to a Duration
BuildArch:      noarch
%description -n %{name}+chrono-devel

This package contains library source intended for building other packages which
use the "chrono" feature of the "%{crate}" crate.

%package     -n %{name}+custom-devel
Summary:        Configurable, precise and fast rust string parser to a Duration
BuildArch:      noarch
%description -n %{name}+custom-devel

This package contains library source intended for building other packages which
use the "custom" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Configurable, precise and fast rust string parser to a Duration
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+standard-devel
Summary:        Configurable, precise and fast rust string parser to a Duration
BuildArch:      noarch
%description -n %{name}+standard-devel

This package contains library source intended for building other packages which
use the "standard" feature of the "%{crate}" crate.

%package     -n %{name}+time-devel
Summary:        Configurable, precise and fast rust string parser to a Duration
BuildArch:      noarch
%description -n %{name}+time-devel

This package contains library source intended for building other packages which
use the "time" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build -f custom
%install
%cargo_install -f custom
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test -f custom -- -- --skip src/custom/builder.rs
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-fundu-devel -f %{oreon_filedir}/rust-fundu-devel.list

%changelog

%autochangelog
