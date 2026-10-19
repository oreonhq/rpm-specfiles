%global source0_hash 7793f5f18f20e20d0242554d09d774ed7be2b6ae81b1f685897ec05127165474
%bcond check 0
%global crate rustcat
Name:           rust-rustcat
Version:        3.0.0
Release:        1%{?dist}
Summary:        Rustcat - The Modern Port Listener & Reverse Shell
License:        MIT
URL:            https://crates.io/crates/rustcat
Source0:        https://static.crates.io/crates/rustcat/rustcat-%{version}.crate
Patch:          rustcat-fix-metadata.diff
Patch:          0001-port-to-rustyline-v12.patch
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Rustcat - The Modern Port Listener & Reverse Shell
License:        MIT AND MPL-2.0 AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (Unlicense OR MIT)
%description -n %{crate}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
find . -type f -executable -print -exec chmod -x {} + ;
%oreon_vendor_cargo
%build

%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%install
%cargo_install
mv %{buildroot}%{_bindir}/rc %{buildroot}%{_bindir}/rcat
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rustcat -f %{oreon_filedir}/rustcat.list

%changelog

%autochangelog
