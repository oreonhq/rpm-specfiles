%global source0_hash 3219755622f812c6cfae046e0464b6c2cd18a88650db1bfaaa4c68591ddbcb44

Name:           teampulls
Version:        0.2.7
Release:        3%{?dist}
Summary:        CLI tool that lists pull requests from GitHub

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            https://github.com/brejoc/teampulls
Source0:        https://files.pythonhosted.org/packages/source/t/%{name}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(poetry-core)
BuildRequires:  python3dist(pip)
BuildRequires:  pyproject-rpm-macros

# Runtime dependencies
#BuildRequires:  python3dist(requests)
#BuildRequires:  python3dist(toml)
#BuildRequires:  python3dist(docopt)

%description
teampulls lists all of the pull requests for a list of users and repositories.
On top of that every pull requests that is older than 14 days is
printed in red.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version}

%build
%pyproject_wheel

%install
%{pyproject_install}
install -Dpm 0644 teampulls.toml %{buildroot}%{_sysconfdir}/teampulls.toml

%files
%doc README.md
%license LICENSE
%{_bindir}/teampulls
%config(noreplace) %{_sysconfdir}/teampulls.toml
%{python3_sitelib}/teampulls
%{python3_sitelib}/teampulls-0.2.6.dist-info/

%changelog
%autochangelog
