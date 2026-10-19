%global source0_hash deedaa9117c56c7d80030ac5566fdc5b52b3eb6a9faf2baa69408896d9090d28
Name:           python-micawber
Version:        0.8.0
Release:        1%{?dist}
Summary:        a small library for extracting rich content from urls
License:        ...
URL:            https://github.com/coleifer/micawber
Source0:        https://files.pythonhosted.org/packages/source/m/micawber/micawber-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-micawber = %{version}-%{release}
# /oreon:deps
%package -n       python3-micawber+cache
Summary:        Metapackage for python3-micawber cache extras
Requires:       python3-micawber = %{version}-%{release}
Requires:       python3dist(redis) >= 3.0.0
Provides:       python3dist(micawber[cache]) = %{version}-%{release}

%description -n python3-micawber+cache
Metapackage for python3-micawber cache extras.

%description

%package -n     python3-micawber
Summary:        a small library for extracting rich content from urls
# oreon:reqs
Requires:       python3dist(beautifulsoup4) >= 4.4
# /oreon:reqs
%description -n python3-micawber

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir micawber-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-micawber usr/lib/python3*/site-packages/micawber* usr/lib64/python3*/site-packages/micawber* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/micawber* usr/lib64/python3*/site-packages/micawber* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-micawber -f %{oreon_filedir}/python3-micawber.list

%changelog

%autochangelog
