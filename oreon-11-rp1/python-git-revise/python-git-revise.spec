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
Version:        0.7.0
Release:        17%{?dist}
Summary:        Efficiently update, split, and rearrange git commits

License:        MIT
URL:            https://github.com/mystor/git-revise
Source0:        https://github.com/mystor/git-revise/archive/%{version}/%{shortname}-%{version}.tar.gz
BuildArch:      noarch

# Patch from upstream commit https://github.com/mystor/git-revise/commit/a7d02b009f79021b5c5add0a1767ffcace3e7904
# This should be fixed in the next release
Patch0: git-ref-log.patch

BuildRequires:  python3-devel >= 3.8
BuildRequires:  python3dist(setuptools)

# For testing purposes
BuildRequires:  python3dist(pytest)
BuildRequires:  git

# Needs gpg in the tests
BuildRequires:  gnupg2

%description    %{descrip}

%package -n %{shortname}
Summary:  %{summary}
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

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} -m pytest

%files -n %{shortname}
%license LICENSE
%doc README.md
%{_bindir}/git-revise
%{_mandir}/man1/git-revise.1*

%files -n python3-%{shortname}
%license LICENSE
%doc README.md
%{python3_sitelib}/gitrevise
%{python3_sitelib}/git_revise-%{version}-py%{python3_version}.egg-info

%changelog
%autochangelog
