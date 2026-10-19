%global source0_hash af0e5dac788d42e3c571cbbc4780bd8ab974fc44a1567514d64564e4f825559c
Name:           python-webscrapbook
Version:        2.10.2
Release:        1%{?dist}
Summary:        A backend toolkit for management of WebScrapBook collection.
License:        MIT
URL:            https://github.com/danny0838/PyWebScrapBook
Source0:        https://files.pythonhosted.org/packages/source/w/webscrapbook/webscrapbook-%{version}.tar.gz
BuildArch:      noarch
Patch100:       python-webscrapbook-2.7.1-test-requirements.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.0
Requires:       python3-webscrapbook = %{version}-%{release}
# /oreon:deps
%package -n       python3-webscrapbook+adhoc_ssl
Summary:        Metapackage for python3-webscrapbook adhoc_ssl extras
Requires:       python3-webscrapbook = %{version}-%{release}
Provides:       python3dist(webscrapbook[adhoc_ssl]) = %{version}-%{release}

%description -n python3-webscrapbook+adhoc_ssl
Metapackage for python3-webscrapbook adhoc_ssl extras.

%description

%package -n     python3-webscrapbook
Summary:        A backend toolkit for management of WebScrapBook collection.
# oreon:reqs
Requires:       python3dist(commonmark) >= 0.8
Requires:       python3dist(flask) >= 2.0.0
Requires:       python3dist(jinja2) >= 2.10.1
Requires:       python3dist(lxml) >= 4.0
Requires:       python3dist(werkzeug) >= 2.0.1
Requires:       python3dist(zipremove) >= 0.9
# /oreon:reqs
%description -n python3-webscrapbook

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir webscrapbook-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-webscrapbook usr/lib/python3*/site-packages/webscrapbook* usr/lib64/python3*/site-packages/webscrapbook* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/webscrapbook* usr/lib64/python3*/site-packages/webscrapbook* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-webscrapbook -f %{oreon_filedir}/python3-webscrapbook.list

%changelog

%autochangelog
