%global source2_hash 0b1ba68a1ba1548f44209ce1228d17d6d5768d72ffa991909771df8e9d42d70d
%global source0_hash 618a38baf452fbe29499f4236bc0f3120c613171fb926429cd4c1fe4fed40cf9
%bcond check 1
%global crate git-interactive-rebase-tool
Name:           rust-git-interactive-rebase-tool
Version:        2.4.1
Release:        1%{?dist}
Summary:        Full-featured terminal-based sequence editor for Git interactive rebase
License:        GPL-3.0-or-later
URL:            https://crates.io/crates/git-interactive-rebase-tool
Source0:        https://static.crates.io/crates/git-interactive-rebase-tool/git-interactive-rebase-tool-%{version}.crate
Source2:        https://github.com/MitMaro/%{crate}/archive/refs/tags/%{version}.tar.gz
Source3:        COPYING
Patch:          git-interactive-rebase-tool-fix-metadata-auto.diff
Patch:          git-interactive-rebase-tool-fix-metadata.diff
Patch2:         git-interactive-rebase-tool-fix-test.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Full-featured terminal-based sequence editor for Git interactive rebase
License:        %{shrink:
    Apache-2.0 AND
    (Apache-2.0 OR MIT) AND
    (Apache-2.0 OR BSD-2-Clause OR MIT) AND
    BSD-3-Clause AND
    (GPL-2.0-only WITH GCC-exception-2.0) AND
    GPL-3.0-or-later AND
    ISC AND
    MIT AND
    Unicode-3.0
}
%description -n %{crate}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%setup -D -q -n %{crate}-%{version} -T -a 2
mv %{crate}-%{version}/test .
mv %{crate}-%{version}/src/interactive-rebase-tool.1 src/
rm -r %{crate}-%{version}
cp -a %{SOURCE3} .
%oreon_vendor_cargo
%build

%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%install
%cargo_install
install -p src/interactive-rebase-tool.1 -t %{buildroot}%{_mandir}/man1 -D -m 644
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n git-interactive-rebase-tool -f %{oreon_filedir}/git-interactive-rebase-tool.list

%changelog

%autochangelog
