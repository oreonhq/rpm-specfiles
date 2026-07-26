%global source0_hash 5dd2740c29ad485f62f2e871e732f8405f078b1d283dc2ea90a5a5e74f5bf7ba

%global sum     Python client library for openQA API
%global desc    The openqa_client Python library provides convenient access to the \
openQA web API, using the requests HTTP request library.

%global srcname         openqa_client

%global github_owner    os-autoinst
%global github_name     openQA-python-client
%global github_version  4.3.1
# if set, will be a post-release snapshot build, otherwise a 'normal' build
#global github_commit   080d03858b7b12f144770af8ceb938fe6c7dbb11
#global github_date     20170130
%global shortcommit     %(c=%{github_commit}; echo ${c:0:7})

Name:           python-openqa_client
Version:        %{github_version}
Release:        3%{?github_date:.%{github_date}git%{shortcommit}}%{?dist}
Summary:        %{sum}

License:        GPL-2.0-or-later
URL:            https://github.com/%{github_owner}/%{github_name}/
Source0:        https://files.pythonhosted.org/packages/source/o/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

%description
%{desc}

%package -n python3-openqa_client
Summary:        %{sum}
BuildRequires:  pyproject-rpm-macros

%{?python_provide:%python_provide python3-openqa_client}
Obsoletes:      python2-openqa_client < %{version}-%{release}

%description -n python3-openqa_client
%{desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}
# setuptools-git is needed to build the source distribution, but not
# for packaging, which *starts* from the source distribution
sed -i -e 's., "setuptools-scm"..g' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install

%check
%tox

%files -n python3-openqa_client
%doc README.md CHANGELOG.md
%license COPYING
%{python3_sitelib}/openqa_client*

%changelog
%autochangelog
