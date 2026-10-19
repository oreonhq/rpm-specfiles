%global source0_hash 062249c8886a0ab19e45d1c3afd5631ec806e7a95cf5153c96560f5e47756cbd
Name:           python-sybil
Version:        10.1.0
Release:        1%{?dist}
Summary:        Automated testing for the examples in your code and documentation.
License:        MIT
URL:            https://github.com/simplistix/sybil
Source0:        https://files.pythonhosted.org/packages/source/s/sybil/sybil-%{version}.tar.gz
BuildArch:      noarch
Patch:          drop-dependency-on-seedir.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-sybil = %{version}-%{release}
# /oreon:deps
%package -n       python3-sybil+pytest
Summary:        Metapackage for python3-sybil pytest extras
Requires:       python3-sybil = %{version}-%{release}
Requires:       python3dist(pytest) >= 8
Provides:       python3dist(sybil[pytest]) = %{version}-%{release}

%description -n python3-sybil+pytest
Metapackage for python3-sybil pytest extras.

%package -n       python3-sybil+myst
Summary:        Metapackage for python3-sybil myst extras
Requires:       python3-sybil = %{version}-%{release}
Requires:       python3dist(pyyaml) >= 6.0.3
Provides:       python3dist(sybil[myst]) = %{version}-%{release}

%description -n python3-sybil+myst
Metapackage for python3-sybil myst extras.

%description

%package -n     python3-sybil
Summary:        Automated testing for the examples in your code and documentation.
%description -n python3-sybil

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir sybil-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-sybil usr/lib/python3*/site-packages/sybil* usr/lib64/python3*/site-packages/sybil* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/sybil* usr/lib64/python3*/site-packages/sybil* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-sybil -f %{oreon_filedir}/python3-sybil.list

%changelog

%autochangelog
