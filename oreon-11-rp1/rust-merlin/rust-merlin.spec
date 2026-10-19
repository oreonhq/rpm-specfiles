%global source0_hash 58c38e2799fc0978b65dfff8023ec7843e2330bb462f19198840b34b6582397d
%bcond check 0
%global debug_package %{nil}
%global crate merlin
Name:           rust-merlin
Version:        3.0.0
Release:        1%{?dist}
Summary:        Composable proof transcripts for public-coin arguments of knowledge
License:        MIT
URL:            https://crates.io/crates/merlin
Source0:        https://static.crates.io/crates/merlin/merlin-%{version}.crate
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
Summary:        Composable proof transcripts for public-coin arguments of knowledge
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+debug-transcript-devel
Summary:        Composable proof transcripts for public-coin arguments of knowledge
BuildArch:      noarch
%description -n %{name}+debug-transcript-devel

This package contains library source intended for building other packages which
use the "debug-transcript" feature of the "%{crate}" crate.

%package     -n %{name}+hex-devel
Summary:        Composable proof transcripts for public-coin arguments of knowledge
BuildArch:      noarch
%description -n %{name}+hex-devel

This package contains library source intended for building other packages which
use the "hex" feature of the "%{crate}" crate.

%package     -n %{name}+nightly-devel
Summary:        Composable proof transcripts for public-coin arguments of knowledge
BuildArch:      noarch
%description -n %{name}+nightly-devel

This package contains library source intended for building other packages which
use the "nightly" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Composable proof transcripts for public-coin arguments of knowledge
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
%files -n rust-merlin-devel -f %{oreon_filedir}/rust-merlin-devel.list

%changelog

%autochangelog
