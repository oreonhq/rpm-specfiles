%global source0_hash 65eb05f2959861d16e60d132b2175169e6e1aec840ab6e4bae556c6d08a199a7

Name:           git-tools
Version:        2025.08
Release:        2%{?dist}
Summary:        Assorted git-related scripts and tools

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/MestreLion/%{name}
Source0:        https://github.com/MestreLion/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       git

BuildRequires:  python3-devel

%description
Assorted git-related scripts and tools:

git-branches-rename:
Batch renames branches with a matching prefix to another prefix

git-clone-subset:
Clones a subset of a git repository

git-find-uncommitted-repos:
Recursively list repos with uncommitted changes

git-rebase-theirs:
Resolve rebase conflicts and failed cherry-picks by favoring 'theirs' version

git-restore-mtime:
Restore original modification time of files based on the date of the most
recent commit that modified them

git-strip-merge:
A git-merge wrapper that deletes files on a "foreign" branch before merging

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

# https://python-rpm-porting.readthedocs.io/en/latest/applications.html#fixing-shebangs
sed -i.bak '1s=^#!/usr/bin/\(python\|env python\)[0-9.]*=#!%{__python3}=' git-restore-mtime
touch -r git-restore-mtime.bak git-restore-mtime
rm -f git-restore-mtime.bak

%build

%install
mkdir -p %{buildroot}%{_bindir}
cp -p git-branches-rename %{buildroot}%{_bindir}/.
cp -p git-clone-subset %{buildroot}%{_bindir}/.
cp -p git-find-uncommitted-repos %{buildroot}%{_bindir}/.
cp -p git-rebase-theirs %{buildroot}%{_bindir}/.
cp -p git-restore-mtime %{buildroot}%{_bindir}/.
cp -p git-strip-merge %{buildroot}%{_bindir}/.
mkdir -p %{buildroot}%{_mandir}/man1
cp -p man1/git-* %{buildroot}%{_mandir}/man1/.

%files
%license LICENSE.txt
%doc README.md
%{_bindir}/*
%{_mandir}/man1/*

%changelog
%autochangelog
