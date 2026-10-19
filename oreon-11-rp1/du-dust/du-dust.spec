%global source0_hash 9dd1ec7576d43574e6f48342cb96a5087338b4c308460a848f5895f72ddc3bc9
%bcond check 1
Name:           du-dust
Version:        1.2.6
Release:        1%{?dist}
Summary:        More intuitive version of du
SourceLicense:  Apache-2.0
License:        %{shrink:
    Apache-2.0 AND
    BSD-2-Clause AND
    MIT AND
    MPL-2.0 AND
    Unicode-DFS-2016 AND
    (Apache-2.0 OR BSL-1.0) AND
    (Apache-2.0 OR MIT) AND
    (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
    (Unlicense OR MIT)
    }
URL:            https://github.com/bootandy/dust
Source0:        https://github.com/bootandy/dust/archive/v%{version}.tar.gz
Patch:          du-dust-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n dust-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%install
install -Dpm 0755 target/rpm/dust -t %{buildroot}%{_bindir}
install -Dpm 0644 completions/dust.bash -t %{buildroot}%{bash_completions_dir}
install -Dpm 0644 completions/dust.fish -t %{buildroot}%{fish_completions_dir}
install -Dpm 0644 completions/_dust -t %{buildroot}%{zsh_completions_dir}
install -Dpm 0644 man-page/dust.1 -t %{buildroot}%{_mandir}/man1/
%oreon_autofiles main
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
