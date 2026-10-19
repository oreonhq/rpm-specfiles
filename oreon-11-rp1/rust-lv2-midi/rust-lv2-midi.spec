%global source0_hash ad23e6bcd0036b1859992b92bbf1855f99ed648886ed9ad9a32fc4ecf2a20f74
%bcond check 0
%global debug_package %{nil}
%global crate lv2-midi
Name:           rust-lv2-midi
Version:        1.2.0
Release:        1%{?dist}
Summary:        Rust-lv2's MIDI processing library
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/lv2-midi
Source0:        https://static.crates.io/crates/lv2-midi/lv2-midi-%{version}.crate
Patch:          lv2-midi-fix-metadata.diff
ExcludeArch:    ppc64le s390x
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
Summary:        Rust-lv2's MIDI processing library
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+wmidi-devel
Summary:        Rust-lv2's MIDI processing library
BuildArch:      noarch
%description -n %{name}+wmidi-devel

This package contains library source intended for building other packages which
use the "wmidi" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build -a
%install
%cargo_install -a
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test -a
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-lv2-midi-devel -f %{oreon_filedir}/rust-lv2-midi-devel.list

%changelog

%autochangelog
