%global source0_hash 45e6db343bac075ae898d3e8616565804c917545d9be45273ddc8f0666133147
%bcond check 1
Name:       stgit
Version:    2.6.1
Release:        1%{?dist}
Summary:        Stack-based patch management for Git
SourceLicense:    GPL-2.0-only
License:        %{shrink:
    Apache-2.0 AND
    BSD-3-Clause AND
    GPL-2.0-only AND
    MIT AND
    Unicode-3.0 AND
    Zlib AND
    (0BSD OR Apache-2.0 OR MIT) AND
    (Apache-2.0 OR MIT) AND
    (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
    (Apache-2.0 OR MIT OR Zlib) AND
    (MIT OR Unlicense)
}
URL:        https://stacked-git.github.io/
Source0:        https://github.com/stacked-git/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Patch:      stgit-fix-metadata.diff
Patch:      update-gix-to-0.75.0.patch
%if %{with check}
%endif
Requires:   git-core
Requires:   git-email
Requires:   emacs-filesystem
Requires:   vim-filesystem
# oreon:deps
BuildRequires:  asciidoc
BuildRequires:  cargo-rpm-macros
BuildRequires:  git-core
BuildRequires:  git-email
BuildRequires:  make
BuildRequires:  perl
BuildRequires:  procps-ng
BuildRequires:  xmlto
# /oreon:deps
%description
Stacked Git, StGit for short, is an application for managing Git commits as a
stack of patches.

With a patch stack workflow, multiple patches can be developed concurrently and
efficiently, with each patch focused on a single concern, resulting in both a
clean Git commit history and improved productivity.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

rm build.rs
%{__cargo} generate-lockfile
make all CARGO="%{__cargo}" STG_PROFILE=rpm
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%install
make install install-man install-completion install-contrib CARGO="%{__cargo}" STG_PROFILE=rpm DESTDIR=$RPM_BUILD_ROOT prefix=%{_prefix}
install -m 644 -D contrib/stgbashprompt.sh $RPM_BUILD_ROOT%{_datadir}/%{name}/contrib/stgbashprompt.sh
%oreon_autofiles main
%if %{with check}
%check

%cargo_test
make test CARGO="%{__cargo}" STG_PROFILE=rpm
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
