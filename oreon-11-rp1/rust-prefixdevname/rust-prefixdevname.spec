%global source0_hash 5d97dd3d11401362ff4c1056cdeaf7d8961362d6f0e570f62b7c4bda220c4cb9
%global source1_hash none
%bcond_without check
%global crate prefixdevname
Name:           rust-prefixdevname
Version:        0.2.0
Release:        1%{?dist}
Summary:        Udev helper utility that provides network interface naming using user defined prefix
License:        MIT
URL:            https://crates.io/crates/prefixdevname
Source0:        https://crates.io/api/v1/crates/prefixdevname/0.2.0/download
Patch0001:      0001-Drop-unnecessary-cast.patch
%if 0%{?rhel} || (0%{?oreon} >= 11)
%else
%endif
%if %{with check}
%endif
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  pkgconfig(libudev)
BuildRequires:  rustc
BuildRequires:  umockdev-devel
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Udev helper utility that provides network interface naming using user defined prefix
License:        MIT AND (MIT OR Apache-2.0) AND (Unlicense OR MIT) AND Unicode-DFS-2016
%description -n %{crate}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version_no_tilde} -p1
%if 0%{?rhel} || (0%{?oreon} >= 11)
cargo vendor --versioned-dirs
rm -f Cargo.lock
%else
%oreon_vendor_cargo
%build

%cargo_build
%cargo_license_summary
%{cargo_license} > LICENSE.dependencies
%if 0%{?rhel} || (0%{?oreon} >= 11)
%cargo_vendor_manifest
%endif
%install
%make_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n prefixdevname -f %{oreon_filedir}/prefixdevname.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.2.0-1
- Import
%endif
