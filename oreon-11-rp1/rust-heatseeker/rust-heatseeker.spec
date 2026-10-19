%global source0_hash 9cdc2d4aa52a227306af44cfeb149116373c4c6edc9847b0a872ff0632aaed87
%bcond check 1
%global crate heatseeker
Name:           rust-heatseeker
Version:        1.10.1
Release:        1%{?dist}
Summary:        Fast, robust, and portable fuzzy finder
License:        MIT
URL:            https://crates.io/crates/heatseeker
Source0:        https://static.crates.io/crates/heatseeker/heatseeker-%{version}.crate
Patch:          heatseeker-fix-metadata-auto.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Fast, robust, and portable fuzzy finder
License:        MIT AND (Apache-2.0 OR MIT)
%description -n %{crate}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%install
%cargo_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%cargo_test -- -- --exact --skip screen::unix::tests::winsize_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n heatseeker -f %{oreon_filedir}/heatseeker.list

%changelog

%autochangelog
