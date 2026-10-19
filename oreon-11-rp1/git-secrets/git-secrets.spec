%global source0_hash f1d50c6c5c7564f460ff8d279081879914abe920415c2923934c1f1d1fac3606
Name:           git-secrets
Version:        1.3.0
Release:        17%{?dist}
Summary:        Prevents committing secrets and credentials into git repos
License:        Apache-2.0
URL:            https://github.com/awslabs/%{name}/
Source0:        https://github.com/awslabs/%{name}//archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       git-core
# oreon:deps
BuildRequires:  bash
BuildRequires:  git-core
BuildRequires:  make
# /oreon:deps
%description
git-secrets scans commits, commit messages, and --no-ff merges to prevent
adding secrets into your git repositories. If a commit, commit message, or any
commit in a --no-ff merge history matches one of your configured prohibited
regular expression patterns, then the commit is rejected.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%make_build PREFIX=%{_prefix}
%install
%make_install PREFIX=%{_prefix}
%oreon_autofiles main

%check

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
