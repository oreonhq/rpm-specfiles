%global source0_hash ed8112fc2b513076d94101cd1fa97a7ee2a03fc057f258d0e2a64cd449c7f0c3
Name:           python-dpath
Version:        2.2.0
Release:        1%{?dist}
Summary:        Filesystem-like pathing and searching for dictionaries
License:        MIT
URL:            https://github.com/akesterson/dpath-python
Source0:        https://github.com/akesterson/dpath-python/archive/v%{version}/dpath-python-%{version}.tar.gz
BuildArch:      noarch
%global common_description %{expand:
A python library for accessing and searching dictionaries via /slashed/paths
ala xpath.
Basically it lets you glob over a dictionary as if it were a filesystem. It
allows you to specify globs (ala the bash eglob syntax, through some advanced
fnmatch.fnmatch magic) to access dictionary elements, and provides some
facility for filtering those results.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-dpath = %{version}-%{release}
# /oreon:deps
%description %{common_description}

%package -n python3-dpath
Summary:        Filesystem-like pathing and searching for dictionaries
%description -n python3-dpath %{common_description}

%prep
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-dpath usr/lib/python3*/site-packages/dpath* usr/lib64/python3*/site-packages/dpath* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/dpath* usr/lib64/python3*/site-packages/dpath* usr/bin/*

%check

%tox -- -- -v
%files
%files -n python3-dpath -f %{oreon_filedir}/python3-dpath.list

%changelog

%autochangelog
