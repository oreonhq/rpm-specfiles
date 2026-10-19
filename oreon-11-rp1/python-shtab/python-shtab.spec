%global source0_hash 0637338723a8fc08ed1c2fd826d8432229924649c26e3247bb48c53d60ca3bf9
Name:           python-shtab
Version:        1.12.1
Release:        1%{?dist}
Summary:        Automagic shell tab completion for Python CLI applications
License:        MPL-2.0
URL:            https://github.com/tqdm/shtab
Source0:        https://files.pythonhosted.org/packages/source/s/shtab/shtab-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77
BuildRequires:  python3dist(setuptools-scm[toml]) >= 3.4
Requires:       python3-shtab = %{version}-%{release}
# /oreon:deps
%package -n       python3-shtab+dev
Summary:        Metapackage for python3-shtab dev extras
Requires:       python3-shtab = %{version}-%{release}
Requires:       python3dist(pytest) >= 6
Provides:       python3dist(shtab[dev]) = %{version}-%{release}

%description -n python3-shtab+dev
Metapackage for python3-shtab dev extras.

%description

%package -n     python3-shtab
Summary:        Automagic shell tab completion for Python CLI applications
%description -n python3-shtab

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir shtab-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-shtab usr/lib/python3*/site-packages/shtab* usr/lib64/python3*/site-packages/shtab* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/shtab* usr/lib64/python3*/site-packages/shtab* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-shtab -f %{oreon_filedir}/python3-shtab.list

%changelog

%autochangelog
