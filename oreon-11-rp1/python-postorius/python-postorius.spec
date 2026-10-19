%global source0_hash 602def5c4852900d49e8ad95196a2334e13c31e49d9c0859324879e7c5131a22
Name:           python-postorius
Version:        1.3.13
Release:        1%{?dist}
Summary:        A web user interface for GNU Mailman
License:        ...
URL:            https://gitlab.com/mailman/postorius
Source0:        https://files.pythonhosted.org/packages/source/p/postorius/postorius-%{version}.tar.gz
BuildArch:      noarch
Patch:          postorius-dont-ship-examples.diff
Patch:          postorius-django52.diff
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-postorius = %{version}-%{release}
# /oreon:deps
%package -n       python3-postorius+test
Summary:        Metapackage for python3-postorius test extras
Requires:       python3-postorius = %{version}-%{release}
Provides:       python3dist(postorius[test]) = %{version}-%{release}

%description -n python3-postorius+test
Metapackage for python3-postorius test extras.

%description

%package -n     python3-postorius
Summary:        A web user interface for GNU Mailman
# oreon:reqs
Requires:       python3dist(django) < 5.1
Requires:       python3dist(django) >= 4.2
Requires:       python3dist(django-mailman3) >= 1.3.13
Requires:       python3dist(mailmanclient) >= 3.3.3
# /oreon:reqs
%description -n python3-postorius

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir postorius-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-postorius usr/lib/python3*/site-packages/postorius* usr/lib64/python3*/site-packages/postorius* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/postorius* usr/lib64/python3*/site-packages/postorius* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-postorius -f %{oreon_filedir}/python3-postorius.list

%changelog

%autochangelog
