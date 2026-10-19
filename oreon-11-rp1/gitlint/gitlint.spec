%global source0_hash b5b70fb894e80849b69abbb65ee7dbb3520fc3511f202a6e6b6ddf1a71ee8f61
Summary:        Git commit message linting tool
Name: gitlint
Version: 0.19.1
Release:        1%{?dist}
License: MIT
Source0:        https://files.pythonhosted.org/packages/source/g/%{name}/%{name}-%{version}.tar.gz
Patch0: strict-dependencies.patch
URL: https://jorisroovers.github.io/gitlint
BuildArch: noarch
Requires: git-core
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-gitlint = %{version}-%{release}
# /oreon:deps
%description
gitlint checks git commit messages for style, using validations based on
well-known community standards or on checks which have proved useful:
maximum title length, trailing white-space checks, punctuation, tabs,
minimum body length, valid email addresses...

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%py3_build
%check

PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} -m coverage run --omit='/usr/*,$(pwd)/gitlint/tests/*,$(pwd)/gitlint/qa/*' -m unittest discover -v -s $(pwd)/gitlint/tests
%install
%py3_install
rm -rf %{buildroot}%{python3_sitelib}/qa
%oreon_autofiles main

%files

%changelog

%autochangelog
