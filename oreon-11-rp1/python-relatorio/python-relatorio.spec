%global source0_hash 18a0e8c47209a3d6b565c1136730ff149207c1ae7548f5f954382c9498237f42
Name:           python-relatorio
Version:        1.0.0
Release:        1%{?dist}
Summary:        A templating library able to output odt files
License:        GPL-3.0-or-later
URL:            https://www.tryton.org/
Source0:        https://files.pythonhosted.org/packages/source/r/relatorio/relatorio-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatchling) >= 1
Requires:       python3-relatorio = %{version}-%{release}
# /oreon:deps
%package -n       python3-relatorio+fodt
Summary:        Metapackage for python3-relatorio fodt extras
Requires:       python3-relatorio = %{version}-%{release}
Provides:       python3dist(relatorio[fodt]) = %{version}-%{release}

%description -n python3-relatorio+fodt
Metapackage for python3-relatorio fodt extras.

%description

%package -n     python3-relatorio
Summary:        A templating library able to output odt files
# oreon:reqs
Requires:       python3dist(genshi) >= 0.5
Requires:       python3dist(lxml) >= 2.0
# /oreon:reqs
%description -n python3-relatorio

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir relatorio-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-relatorio usr/lib/python3*/site-packages/relatorio* usr/lib64/python3*/site-packages/relatorio* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/relatorio* usr/lib64/python3*/site-packages/relatorio* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-relatorio -f %{oreon_filedir}/python3-relatorio.list

%changelog

%autochangelog
