%global source0_hash 1884c2b539f65708bdc50455bb415941a4479e609b7259891730242c7aa53ea3
Name:       rpm-git-tag-sort
Version:    1.0.git.5.0b8afd62
Release:        1%{?dist}
Summary:        Sorts merged git annotated tags according to topology and rpm version sorting.
License:    GPL-2.0-or-later
URL:        https://pagure.io/rpm-git-tag-sort
Source0:        rpm-git-tag-sort-0b8afd62.tar.gz
Source1:    rpm-git-tag-sort-c-vector-0b8afd62.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libgit2-devel
BuildRequires:  make
BuildRequires:  rpm-devel
# /oreon:deps
%description
Sorts git annotated tags of Name-Version-Release form
according to topology (primary criterion) and rpm
version sorting (secondary criterion). Outputs only
merged tags (i.e. those that reachable from the
current HEAD).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -T -b 0 -b 1 -q -n rpm-git-tag-sort
# move c-vector sources to the correct place
mv ../rpm-git-tag-sort-c-vector/* c-vector/

%build

%set_build_flags
%make_build
./test
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
