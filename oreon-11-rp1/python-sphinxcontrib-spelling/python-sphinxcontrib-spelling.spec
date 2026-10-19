%global source0_hash afbc7b8e93721ab88f12bdd39d848b92017b3763b9ed6226b4b0e54b06664fea
Name:           python-sphinxcontrib-spelling
Version:        8.0.2
Release:        1%{?dist}
Summary:        Sphinx spelling extension
License:        ...
URL:            https://sphinxcontrib-spelling.readthedocs.io/en/latest/
Source0:        https://files.pythonhosted.org/packages/source/s/sphinxcontrib_spelling/sphinxcontrib_spelling-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-sphinxcontrib-spelling = %{version}-%{release}
# /oreon:deps
%package -n       python3-sphinxcontrib-spelling+test
Summary:        Metapackage for python3-sphinxcontrib-spelling test extras
Requires:       python3-sphinxcontrib-spelling = %{version}-%{release}
Requires:       python3dist(coverage) >= 4.0
Provides:       python3dist(sphinxcontrib-spelling[test]) = %{version}-%{release}

%description -n python3-sphinxcontrib-spelling+test
Metapackage for python3-sphinxcontrib-spelling test extras.

%description

%package -n     python3-sphinxcontrib-spelling
Summary:        Sphinx spelling extension
# oreon:reqs
Requires:       python3dist(pyenchant) >= 3.1.1
Requires:       python3dist(requests) >= 2.32.3
Requires:       python3dist(sphinx) >= 3.0.0
# /oreon:reqs
%description -n python3-sphinxcontrib-spelling

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir sphinxcontrib_spelling-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-sphinxcontrib-spelling usr/lib/python3*/site-packages/sphinxcontrib_spelling* usr/lib64/python3*/site-packages/sphinxcontrib_spelling* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/sphinxcontrib_spelling* usr/lib64/python3*/site-packages/sphinxcontrib_spelling* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-sphinxcontrib-spelling -f %{oreon_filedir}/python3-sphinxcontrib-spelling.list

%changelog

%autochangelog
