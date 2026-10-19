%global source0_hash 262d0b383a150b44ffb7509f216cb797124da06a5cfdb0b3c38ca58943ba2cf4
%bcond check 1
%define cargo_install_lib 0
Name:     tbtools
Summary:        Thunderbolt/USB4 debugging tools
Version:  0.8.0
Release:        1%{?dist}
SourceLicense:  MIT AND GPL-2.0-only
%define simplified_license %{shrink:
Apache-2.0 AND
MIT AND
Unicode-DFS-2016 AND
(Apache-2.0 OR BSL-1.0) AND
(Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
(BSD-2-Clause OR Apache-2.0 OR MIT) AND
(Unlicense OR MIT)
}
License:  %{simplified_license}
URL:      https://github.com/intel/tbtools
Source0:        https://github.com/intel/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  make
BuildRequires:  rustc
# /oreon:deps
%description
This is a collection of tools for Linux Thunderbolt/USB4 development, debugging
and validation but may be useful to others as well.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1
%oreon_vendor_cargo
%build

%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%install
%cargo_install
PREFIX=%{buildroot}%{_prefix} %make_install CARGO=/usr/bin/true
%oreon_autofiles main
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
