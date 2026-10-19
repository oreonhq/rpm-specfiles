%global source0_hash 963af71311c356bce99c4e056754f3a2bd1a4f33836f13d9197c399c7732176f
Name:           python-dandischema
Version:        0.14.0
Release:        1%{?dist}
Summary:        Schemata for DANDI archive project
License:        Apache-2.0
URL:            http://dandiarchive.org
Source0:        https://files.pythonhosted.org/packages/source/d/dandischema/dandischema-%{version}.tar.gz
BuildArch:      noarch
Patch:          %{forgeurl}/pull/249.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.0.0
Requires:       python3-dandischema = %{version}-%{release}
# /oreon:deps
%package -n       python3-dandischema+style
Summary:        Metapackage for python3-dandischema style extras
Requires:       python3-dandischema = %{version}-%{release}
Provides:       python3dist(dandischema[style]) = %{version}-%{release}

%description -n python3-dandischema+style
Metapackage for python3-dandischema style extras.

%package -n       python3-dandischema+test
Summary:        Metapackage for python3-dandischema test extras
Requires:       python3-dandischema = %{version}-%{release}
Provides:       python3dist(dandischema[test]) = %{version}-%{release}

%description -n python3-dandischema+test
Metapackage for python3-dandischema test extras.

%package -n       python3-dandischema+all
Summary:        Metapackage for python3-dandischema all extras
Requires:       python3-dandischema = %{version}-%{release}
Provides:       python3dist(dandischema[all]) = %{version}-%{release}

%description -n python3-dandischema+all
Metapackage for python3-dandischema all extras.

%description

%package -n     python3-dandischema
Summary:        Schemata for DANDI archive project
# oreon:reqs
Requires:       python3dist(packaging) >= 14.0
Requires:       python3dist(pydantic[email]) >= 2.4
# /oreon:reqs
%description -n python3-dandischema

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir dandischema-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-dandischema usr/lib/python3*/site-packages/dandischema* usr/lib64/python3*/site-packages/dandischema* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/dandischema* usr/lib64/python3*/site-packages/dandischema* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-dandischema -f %{oreon_filedir}/python3-dandischema.list

%changelog

%autochangelog
