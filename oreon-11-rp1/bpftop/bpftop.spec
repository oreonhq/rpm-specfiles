%global source0_hash 871ea55ebe1ddc9555aaf9553ecb10cbec121fe55aac1bb26d19bec23d8b597b
%bcond check 1
%global cargo_install_lib 0
Name:           bpftop
Version:        0.7.1
Release:        1%{?dist}
Summary:        Dynamic real-time view of running eBPF programs
SourceLicense:  Apache-2.0
License:        %{shrink:
    Apache-2.0 AND
    BSD-2-Clause AND
    BSD-3-Clause AND
    MIT AND
    Zlib AND
    (0BSD OR MIT OR Apache-2.0) AND
    (Apache-2.0 OR BSL-1.0) AND
    (Apache-2.0 OR MIT) AND
    (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
    (LGPL-2.1-only OR BSD-2-Clause) AND
    (MIT OR Zlib OR Apache-2.0)
    }
URL:            https://github.com/Netflix/%{name}
Source0:        https://github.com/Netflix/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch:          bpftop-fix-metadata.diff
ExcludeArch: %{ix86}
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n bpftop-%{version} -p1
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
