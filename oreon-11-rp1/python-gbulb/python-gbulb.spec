%global source0_hash b66bb1637e956a605636ac2820747583983715a87742beaddeb2e41da37b5154
Name:           python-gbulb
Version:        0.6.6
Release:        1%{?dist}
Summary:        GLib event loop for Python asyncio
License:        ...
URL:            https://github.com/beeware/gbulb
Source0:        https://files.pythonhosted.org/packages/source/g/gbulb/gbulb-%{version}.tar.gz
BuildArch:      noarch
Patch:          requirements-versions.patch
Patch:          0001-Fix-compatibility-with-Python-3.13.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) == 74.1.2
BuildRequires:  python3dist(setuptools-scm) == 8.1.0
Requires:       python3-gbulb = %{version}-%{release}
# /oreon:deps
%package -n       python3-gbulb+dev
Summary:        Metapackage for python3-gbulb dev extras
Requires:       python3-gbulb = %{version}-%{release}
Requires:       python3dist(coverage[toml]) == 7.6.1
Requires:       python3dist(pre-commit) == 3.5.0
Requires:       python3dist(pre-commit) == 3.8.0
Requires:       python3dist(pytest) == 8.3.2
Requires:       python3dist(setuptools-scm) == 8.1.0
Requires:       python3dist(tox) == 4.18.1
Provides:       python3dist(gbulb[dev]) = %{version}-%{release}

%description -n python3-gbulb+dev
Metapackage for python3-gbulb dev extras.

%description

%package -n     python3-gbulb
Summary:        GLib event loop for Python asyncio
# oreon:reqs
Requires:       python3dist(pygobject) < 3.50.0
Requires:       python3dist(pygobject) >= 3.14.0
# /oreon:reqs
%description -n python3-gbulb

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir gbulb-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-gbulb usr/lib/python3*/site-packages/gbulb* usr/lib64/python3*/site-packages/gbulb* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/gbulb* usr/lib64/python3*/site-packages/gbulb* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-gbulb -f %{oreon_filedir}/python3-gbulb.list

%changelog

%autochangelog
