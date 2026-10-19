%global source0_hash 5c4282c1c7fc9b5a23febe16ae038b6392d7ce068d186ad4870ba22e74db0711
Name:           python-sphinxcontrib-programoutput
Version:        0.20
Release:        1%{?dist}
Summary:        Sphinx extension to include program output
License:        BSD-2-Clause
URL:            https://sphinxcontrib-programoutput.readthedocs.io/en/latest/
Source0:        https://files.pythonhosted.org/packages/source/s/sphinxcontrib_programoutput/sphinxcontrib_programoutput-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61
Requires:       python3-sphinxcontrib-programoutput = %{version}-%{release}
# /oreon:deps
%package -n       python3-sphinxcontrib-programoutput+test
Summary:        Metapackage for python3-sphinxcontrib-programoutput test extras
Requires:       python3-sphinxcontrib-programoutput = %{version}-%{release}
Requires:       python3dist(erbsland-sphinx-ansi) >= 1.2.4
Provides:       python3dist(sphinxcontrib-programoutput[test]) = %{version}-%{release}

%description -n python3-sphinxcontrib-programoutput+test
Metapackage for python3-sphinxcontrib-programoutput test extras.

%package -n       python3-sphinxcontrib-programoutput+docs
Summary:        Metapackage for python3-sphinxcontrib-programoutput docs extras
Requires:       python3-sphinxcontrib-programoutput = %{version}-%{release}
Provides:       python3dist(sphinxcontrib-programoutput[docs]) = %{version}-%{release}

%description -n python3-sphinxcontrib-programoutput+docs
Metapackage for python3-sphinxcontrib-programoutput docs extras.

%package -n       python3-sphinxcontrib-programoutput+ansi
Summary:        Metapackage for python3-sphinxcontrib-programoutput ansi extras
Requires:       python3-sphinxcontrib-programoutput = %{version}-%{release}
Requires:       python3dist(erbsland-sphinx-ansi) >= 1.2.4
Provides:       python3dist(sphinxcontrib-programoutput[ansi]) = %{version}-%{release}

%description -n python3-sphinxcontrib-programoutput+ansi
Metapackage for python3-sphinxcontrib-programoutput ansi extras.

%description

%package -n     python3-sphinxcontrib-programoutput
Summary:        Sphinx extension to include program output
# oreon:reqs
Requires:       python3dist(sphinx) >= 5.0.0
# /oreon:reqs
%description -n python3-sphinxcontrib-programoutput

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir sphinxcontrib_programoutput-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-sphinxcontrib-programoutput usr/lib/python3*/site-packages/sphinxcontrib_programoutput* usr/lib64/python3*/site-packages/sphinxcontrib_programoutput* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/sphinxcontrib_programoutput* usr/lib64/python3*/site-packages/sphinxcontrib_programoutput* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-sphinxcontrib-programoutput -f %{oreon_filedir}/python3-sphinxcontrib-programoutput.list

%changelog

%autochangelog
