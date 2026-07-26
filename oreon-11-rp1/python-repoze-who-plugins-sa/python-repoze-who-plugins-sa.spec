%global source0_hash 9eeda8d01e926ec01de2b6b095eda3fec842ff5b81c636098b461dc307a18fc3

Name:           python-repoze-who-plugins-sa
Version:        1.0.1
Release:        52.20160106gite1a36c5%{?dist}
Summary:        repoze.who SQLAlchemy plugin

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://code.gustavonarea.net/repoze.who.plugins.sa
# Git snapshot to get python3 support.  Generate this way:
# git clone https://github.com/repoze/repoze.who-sqlalchemy.git
# cd repoze.who-sqlalchemy
# patch -p1 < ../repoze-who-plugins-sa-sdist.patch
# python3 setup.py sdist
# tarball will be in the dist/ subdirectory
Source0: repoze.who.plugins.sa-%{version}.tar.gz
#Source0:        https://pypi.python.org/packages/source/r/repoze.who.plugins.sa/repoze.who.plugins.sa-%%{version}.tar.gz
# This patch is to be applied when generating the tarball.  It includes the
# test directoriy so we can run the test suite
# https://github.com/repoze/repoze.who-sqlalchemy/pull/6
#Patch100: repoze-who-plugins-sa-sdist.patch
Patch101: repoze-who-plugins-sa-requires.patch
BuildArch:      noarch

BuildRequires: python3-devel
BuildRequires: python3-repoze-who
BuildRequires: python3-sqlalchemy
BuildRequires: python3-coverage
BuildRequires: python3-pytest

%global _description\
This plugin provides one repoze.who authenticator which works with SQLAlchemy\
or Elixir-based models.\

%description %_description

%package -n python3-repoze-who-plugins-sa
Summary: repoze.who SQLAlchemy plugin

%description -n python3-repoze-who-plugins-sa
This plugin provides one repoze.who authenticator which works with SQLAlchemy
based models on python3

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n repoze.who.plugins.sa-%{version}
%patch -P 101 -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files repoze

%check
%pyproject_check_import
# Tests not ported to Python3.
%if 0
%pytest
%endif

%files -n python3-repoze-who-plugins-sa -f %{pyproject_files}
%doc README.txt
%{python3_sitelib}/repoze.who.plugins.sa-%{version}-py%{python3_version}-nspkg.pth
%exclude %{python3_sitelib}/tests

%changelog
%autochangelog
