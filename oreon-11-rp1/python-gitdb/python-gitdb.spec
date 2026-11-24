# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash bf5421126136d6d0af55bc1e7c1af1c397a34f5b7bd79e776cd3e89785c2b04b
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global srcname gitdb

Name:           python-%{srcname}
Version:        4.0.11
Release:        1%{?dist}
Summary:        Git Object Database

License:        BSD-3-Clause
URL:            https://github.com/gitpython-developers/gitdb
Source0:        %{pypi_source %{srcname}}

BuildArch:      noarch

BuildRequires: oreon-rpm-macros
BuildRequires:  git-core

%global _description %{expand:
GitDB allows you to access bare git repositories for reading and writing.
It aims at allowing full access to loose objects as well as packs with
performance and scalability in mind. It operates exclusively on streams,
allowing to handle large objects with a small memory footprint.}

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist pytest}

%description -n python3-%{srcname} %{_description}

%prep
%oreon_sha256
%autosetup -n %{srcname}-%{version} -p 1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{srcname}

%check
mkdir testrepo
pushd testrepo
git init -q
git config user.email "packaging@oreonhq.com"
git config user.name "%{name} maintainer"
for i in {1..400}; do echo $i > $i; git add $i; git commit -q -m "$i"; done
git gc
popd

export GITDB_TEST_GIT_REPO_BASE=testrepo/.git
%pytest --verbose

%files -n python3-%{srcname} -f %{pyproject_files}
%doc AUTHORS

%changelog
%autochangelog
