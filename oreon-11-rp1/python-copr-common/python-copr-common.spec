%global source0_hash 84c3794b026fd558b3fb42748e3060f26884a8fb828eb36df967b6de83e03e3e

%global srcname copr-common

Name:       python-copr-common
Version:    1.5
Release:    2%{?dist}
Summary:    Python code used by Copr

License:    GPL-2.0-or-later
URL:        https://github.com/fedora-copr/copr

# Source is created by:
# git clone %%url && cd copr
# tito build --tgz --tag %%name-%%version-%%release
Source0:    %name-%version.tar.gz

BuildArch: noarch

%if 0%{?rhel} > 10 || 0%{?fedora} > 42
BuildRequires: python3-devel
%else
BuildRequires: python3-devel
BuildRequires: python3-setuptools
%endif
BuildRequires: python3-pytest
BuildRequires: python3-requests
BuildRequires: python3-filelock
BuildRequires: python3-setproctitle

%global _description\
COPR is lightweight build system. It allows you to create new project in WebUI,\
and submit new builds and COPR will create yum repository from latest builds.\
\
This package contains python code used by other Copr packages. Mostly\
useful for developers only.\

%description %_description

%package -n python3-%{srcname}
Summary: %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
%description -n python3-%{srcname} %_description

%if 0%{?rhel} > 10 || 0%{?fedora} > 42
%generate_buildrequires
%pyproject_buildrequires
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%if 0%{?rhel} > 10 || 0%{?fedora} > 42
version="%version" %pyproject_wheel
%else
version="%version" %py3_build
%endif

%install
%if 0%{?rhel} > 10 || 0%{?fedora} > 42
version=%version %pyproject_install
%else
version=%version %py3_install
%endif

%check
%{_bindir}/python3 -m pytest -vv tests

%files -n python3-%{srcname}
%license LICENSE
%{python3_sitelib}/*

%changelog
%autochangelog
