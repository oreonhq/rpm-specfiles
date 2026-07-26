%global source0_hash 9e693af54af527cce539f5555b7e007d90ba587e3d44f5da2fd2e00679f04865

Summary: Git commit message linting tool
Name: gitlint
Version: 0.15.0
Release: 20%{?dist}
License: MIT
Source: %pypi_source
Patch0: strict-dependencies.patch
URL: https://jorisroovers.github.io/gitlint
BuildArch: noarch
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: %{py3_dist Click} >= 7.1.2
BuildRequires: %{py3_dist arrow} >= 0.15.6
BuildRequires: %{py3_dist sh} >= 1.13.1
BuildRequires: %{py3_dist coverage}
BuildRequires: git-core
Requires: git-core

%description
gitlint checks git commit messages for style, using validations based on
well-known community standards or on checks which have proved useful:
maximum title length, trailing white-space checks, punctuation, tabs,
minimum body length, valid email addresses...

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%py3_build

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} -m coverage run --omit='/usr/*,$(pwd)/gitlint/tests/*,$(pwd)/gitlint/qa/*' -m unittest discover -v -s $(pwd)/gitlint/tests

%install
%py3_install
rm -rf %{buildroot}%{python3_sitelib}/qa

%files
%license LICENSE
%doc README.md
%{python3_sitelib}/%{name}-*.egg-info/
%{python3_sitelib}/%{name}/
%{_bindir}/gitlint

%changelog
%autochangelog
