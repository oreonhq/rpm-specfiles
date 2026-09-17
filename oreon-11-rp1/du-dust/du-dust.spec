%global source0_hash 2f6768534bd01727234e67f1dd3754c9547aa18c715f6ee52094e881ebac50e3

%bcond check 1

Name:           du-dust
Version:        1.2.4
Release:        %autorelease
Summary:        More intuitive version of du

SourceLicense:  Apache-2.0
# (MIT OR Apache-2.0) AND Unicode-DFS-2016
# Apache-2.0
# Apache-2.0 OR BSL-1.0
# Apache-2.0 OR MIT
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# BSD-2-Clause
# MIT
# MIT OR Apache-2.0
# MPL-2.0
# Unlicense OR MIT
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
# LICENSE.dependencies contains a full license breakdown

URL:            https://github.com/bootandy/dust
Source:         %{url}/archive/v%{version}.tar.gz
# Manually created patch for downstream crate metadata changes
# * Remove windows-only dependencies
Patch:          du-dust-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 26

%global _description %{expand:
A more intuitive version of du.}

%description %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n dust-%{version} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

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

%if %{with check}
%check
%cargo_test
%endif

%files
%license LICENSE
%license LICENSE.dependencies
%doc README.md
%{_bindir}/dust
%{bash_completions_dir}/dust.bash
%{fish_completions_dir}/dust.fish
%{zsh_completions_dir}/_dust
%{_mandir}/man1/dust.1*

%changelog
%autochangelog
