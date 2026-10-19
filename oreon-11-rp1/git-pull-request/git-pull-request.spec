%global source0_hash e0c8fd5122a6783e9a92660cd43b94a933d6aadebfd1bb07d276fc60c1013973
%global pypi_name git-pull-request
%global pkg_name git_pull_request
Name:           %{pypi_name}
Version:        6.0.2
Release:        17%{?dist}
Summary:        Command line tool to send GitHub pull-request
License:        Apache-2.0
URL:            https://github.com/Mergifyio/git-pull-request
Source0:        https://files.pythonhosted.org/packages/source/g/%{name}/%{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       python3-PyGithub
Requires:       python3-daiquiri
Requires:       python3-setuptools
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 45
BuildRequires:  python3dist(setuptools-scm) >= 6.2
Requires:       python3-git-pull-request = %{version}-%{release}
# /oreon:deps
%description
%{name} is a command line tool to send GitHub pull-request from
your terminal.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main

%files

%changelog

%autochangelog
