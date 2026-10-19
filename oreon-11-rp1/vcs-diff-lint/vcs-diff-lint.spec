%global source1_hash 6619407ba49ec6f867eb052d117aa38d567c860b6473595140b131296ee3b133
%global source0_hash 5a0e3b1f5b03b6b00e666883d1dcf5c5db32c5379a829bf7d56fdc4b2cba3028
Name:    vcs-diff-lint
Version: 6.4
Release:        4%{?dist}
Summary:        VCS Differential Code Analysis Tool
BuildArch: noarch
%bcond check 0
License: GPL-2.0-or-later
URL:     https://github.com/fedora-copr/vcs-diff-lint
Source0:        %{name}-%{version}.tar.gz
Source1: https://github.com/praiskup/vcs-diff-lint-testdata/releases/download/v1.0.0/vcs-diff-lint-testdata-1.0.0.bundle
Requires: csdiff
Requires: git
Recommends: pylint
Recommends: python3-mypy
Recommends: python3-types-requests
Recommends: ruff
%if %{with check}
%endif
# oreon:deps
BuildRequires:  csdiff
BuildRequires:  git
BuildRequires:  pylint
BuildRequires:  python3-pytest
BuildRequires:  rpmdevtools
# /oreon:deps
%description
Analyze code, and print only reports related to a particular change.

From within a VCS directory (only Git is supported for now) first analyze set of
changed files against given changeset (origin/main by default) so we know what
files need to be analyzed.  Then run code analyzers (e.g. PyLint) against the
old code (before changes), run analyzers against the actual code (not yet pushed
changes), perform a diff (using csdiff utility), and finally print a set of
added (or even fixed, as opt-in) analyzers' warnings.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
%if %{with check}
cp %{SOURCE1} ./
%endif

%build

%install
install -d %buildroot%_bindir
install -p vcs-diff-lint %buildroot%_bindir
install -p vcs-diff-lint-csdiff-pylint %buildroot%_bindir
install -p vcs-diff-lint-csdiff-mypy   %buildroot%_bindir
install -p vcs-diff-lint-csdiff-ruff   %buildroot%_bindir
%oreon_autofiles main
%if %{with check}
%check

./run-tests.sh --no-cov
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
