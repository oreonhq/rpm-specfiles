%global source0_hash 2ed2eaec452d98ccc1c615dd843fd039d9445f2fb4da114ee7e6af5fcb68be98
%bcond check 0
%global debug_package %{nil}
%global crate octseq
%global forgeurl0 https://github.com/NLnetLabs/octseq
Name:           rust-octseq
Version:        0.5.1
Release:        1%{?dist}
Summary:        Abstractions for types representing octet sequences
License:        BSD-3-Clause
URL:            https://crates.io/crates/octseq
VCS:            git:%{forgeurl0}
Source0:        https://static.crates.io/crates/octseq/octseq-%{version}.crate
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
Summary:        Abstractions for types representing octet sequences
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+bytes-devel
Summary:        Abstractions for types representing octet sequences
BuildArch:      noarch
%description -n %{name}+bytes-devel

This package contains library source intended for building other packages which
use the "bytes" feature of the "%{crate}" crate.

%package     -n %{name}+heapless-devel
Summary:        Abstractions for types representing octet sequences
BuildArch:      noarch
%description -n %{name}+heapless-devel

This package contains library source intended for building other packages which
use the "heapless" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Abstractions for types representing octet sequences
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+smallvec-devel
Summary:        Abstractions for types representing octet sequences
BuildArch:      noarch
%description -n %{name}+smallvec-devel

This package contains library source intended for building other packages which
use the "smallvec" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Abstractions for types representing octet sequences
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

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
%files -n rust-octseq-devel -f %{oreon_filedir}/rust-octseq-devel.list

%changelog

%autochangelog
