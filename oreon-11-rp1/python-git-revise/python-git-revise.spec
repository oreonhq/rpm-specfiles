%global source0_hash 47dbed47738dfd6f7f33339a6503c886ce95d36f4690ed20077250e2538443aa
%global shortname git-revise
%global descrip \
git revise is a git subcommand to efficiently update, split, and rearrange\
commits. It is heavily inspired by git rebase, however it tries to be more\
efficient and ergonomic for patch-stack oriented workflows.\
\
By default, git revise will apply staged changes to a target commit, then\
update HEAD to point at the revised history. It also supports splitting commits\
and rewording commit messages.\
\
Unlike git rebase, git revise avoids modifying the working directory or the\
index state, performing all merges in-memory and only writing them when\
necessary. This allows it to be significantly faster on large codebases and\
avoids unnecessarily invalidating builds.
Name:           python-%{shortname}
Version:        0.8.0
Release:        1%{?dist}
Summary:        Efficiently update, split, and rearrange git commits
License:        MIT
URL:            https://github.com/mystor/git-revise
Source0:        https://github.com/mystor/%{shortname}/archive/%{version}/%{shortname}-%{version}.tar.gz
BuildArch:      noarch
Patch0: git-ref-log.patch
# oreon:deps
BuildRequires:  git
BuildRequires:  gnupg2
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)
# /oreon:deps
%description    %{descrip}

%package -n %{shortname}
Summary:        Efficiently update, split, and rearrange git commits
Requires: git
Requires: python3-%{shortname} = %{version}-%{release}
%description -n %{shortname}
%{descrip}

%package -n python3-%{shortname}
Summary:    Python modules for git-revise
Requires:   git
Recommends: %{shortname} = %{version}-%{release}
%{?python_provide:%python_provide python3-%{shortname}}
%description -n python3-%{shortname}
This package contains the python modules for the git-revise program.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -n %{shortname}-%{version}

%patch -P 0 -p1

%build

%py3_build
%install
%py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} -m pytest
%files -f %{oreon_filedir}/main.list
%files -n git-revise -f %{oreon_filedir}/git-revise.list
%files -n python3-git-revise -f %{oreon_filedir}/python3-git-revise.list

%changelog

%autochangelog
