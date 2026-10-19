%global source0_hash 752ae1831a7c60fefa1bf6f4ea96609f53f842d0d8f416d62ce631b1361a2592
%bcond check 1
%global cargo_install_lib 0
Name:           mirrorlist-server
Version:        3.0.8
Release:        1%{?dist}
Summary:        Mirrorlist Server
SourceLicense:  MIT
License:        %{shrink:
    MIT AND
    ISC AND
    Unicode-3.0 AND
    Unicode-DFS-2016 AND
    (Apache-2.0 OR MIT) AND
    (BSD-2-Clause OR Apache-2.0 OR MIT) AND
    (Unlicense OR MIT)
}
URL:            https://github.com/adrianreber/mirrorlist-server
Source0:        https://github.com/adrianreber/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch:          0001-set-license-in-crate-metadata.patch
Patch:          0002-Bump-console-dependency-from-0.15-to-0.16-to-match-i.patch
Patch:          0003-Relax-ipnetwork-dependency-to-allow-both-v0.20-and-v.patch
Patch:          0004-Relax-dns-lookup-dependency.patch
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n mirrorlist-server-%{version} -p1
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

%cargo_test -- --bin mirrorlist-server
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
