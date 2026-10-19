%global source0_hash 310b08c538c04bae779a1c4786430e974801e8880a4c5256dc0877bc82b61af0
%bcond check 1
%global cargo_install_lib 0
Name:           spacer
Version:        0.5.0
Release:        1%{?dist}
Summary:        CLI utility for adding spacers when command output stops
SourceLicense:  MIT
License:        %{shrink:
                MIT AND
                Apache-2.0 AND
                ISC AND
                Unicode-DFS-2016 AND
                (0BSD OR MIT OR Apache-2.0) AND
                (Apache-2.0 OR MIT) AND
                (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
                (MIT OR Zlib OR Apache-2.0) AND
                (Unlicense OR MIT)
                }
URL:            https://github.com/samwho/spacer
Source0:        https://github.com/samwho/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description
A CLI utility for adding spacers when command output stops.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup
%oreon_vendor_cargo
%build

%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%install
%cargo_install
%oreon_autofiles main
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
