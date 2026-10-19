%global source0_hash 1c458f81926b37301cadc8ec1b6316d9a5db53fba061fc4826610395fe5d5c81
Name:           python-daphne
Version:        4.2.3
Release:        1%{?dist}
Summary:        Django ASGI _HTTP/WebSocket_ server
License:        ...
URL:            https://github.com/django/daphne
Source0:        https://files.pythonhosted.org/packages/source/d/daphne/daphne-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-daphne = %{version}-%{release}
# /oreon:deps
%package -n       python3-daphne+tests
Summary:        Metapackage for python3-daphne tests extras
Requires:       python3-daphne = %{version}-%{release}
Provides:       python3dist(daphne[tests]) = %{version}-%{release}

%description -n python3-daphne+tests
Metapackage for python3-daphne tests extras.

%description

%package -n     python3-daphne
Summary:        Django ASGI _HTTP/WebSocket_ server
# oreon:reqs
Requires:       python3dist(asgiref) < 4
Requires:       python3dist(asgiref) >= 3.5.2
Requires:       python3dist(autobahn) >= 22.4.2
Requires:       python3dist(twisted[tls]) >= 22.4
# /oreon:reqs
%description -n python3-daphne

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir daphne-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-daphne usr/lib/python3*/site-packages/daphne* usr/lib64/python3*/site-packages/daphne* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/daphne* usr/lib64/python3*/site-packages/daphne* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-daphne -f %{oreon_filedir}/python3-daphne.list

%changelog

%autochangelog
