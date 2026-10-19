%global source0_hash 260e0d88c9a903c65cfe34fbe818764f44a3f96e722e1a3645ce4d596add22b1
Name:           python-pytools
Version:        2026.1.1
Release:        1%{?dist}
Summary:        A collection of tools for Python
License:        MIT
URL:            https://github.com/inducer/pytools/
Source0:        https://files.pythonhosted.org/packages/source/p/pytools/pytools-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pytools = %{version}-%{release}
# /oreon:deps
%package -n       python3-pytools+numpy
Summary:        Metapackage for python3-pytools numpy extras
Requires:       python3-pytools = %{version}-%{release}
Requires:       python3dist(numpy) >= 1.6
Provides:       python3dist(pytools[numpy]) = %{version}-%{release}

%description -n python3-pytools+numpy
Metapackage for python3-pytools numpy extras.

%package -n       python3-pytools+test
Summary:        Metapackage for python3-pytools test extras
Requires:       python3-pytools = %{version}-%{release}
Provides:       python3dist(pytools[test]) = %{version}-%{release}

%description -n python3-pytools+test
Metapackage for python3-pytools test extras.

%description

%package -n     python3-pytools
Summary:        A collection of tools for Python
# oreon:reqs
Requires:       python3dist(platformdirs) >= 2.2
Requires:       python3dist(siphash24) >= 1.6
Requires:       python3dist(typing-extensions) >= 4.5
# /oreon:reqs
%description -n python3-pytools

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir pytools-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pytools usr/lib/python3*/site-packages/pytools* usr/lib64/python3*/site-packages/pytools* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pytools* usr/lib64/python3*/site-packages/pytools* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pytools -f %{oreon_filedir}/python3-pytools.list

%changelog

%autochangelog
