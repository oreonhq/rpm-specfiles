%global source0_hash 1bfc0d32b43692f28a6e294ad2b69903d43a214672ebcf3124a66d66b52b2418
Name:           python-environs
Version:        15.2.0
Release:        1%{?dist}
Summary:        simplified environment variable parsing
License:        MIT
URL:            https://github.com/sloria/environs
Source0:        https://files.pythonhosted.org/packages/source/e/environs/environs-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 4
Requires:       python3-environs = %{version}-%{release}
# /oreon:deps
%package -n       python3-environs+django
Summary:        Metapackage for python3-environs django extras
Requires:       python3-environs = %{version}-%{release}
Provides:       python3dist(environs[django]) = %{version}-%{release}

%description -n python3-environs+django
Metapackage for python3-environs django extras.

%description

%package -n     python3-environs
Summary:        simplified environment variable parsing
# oreon:reqs
Requires:       python3dist(marshmallow) >= 4.0.0
# /oreon:reqs
%description -n python3-environs

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir environs-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-environs usr/lib/python3*/site-packages/environs* usr/lib64/python3*/site-packages/environs* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/environs* usr/lib64/python3*/site-packages/environs* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-environs -f %{oreon_filedir}/python3-environs.list

%changelog

%autochangelog
