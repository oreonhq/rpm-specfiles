%global source0_hash 55ca7c70a75689be937aa27f8ff4b018f06ff4838fc73045560bf0f5a1291060
Name:           python-werkzeug
Version:        3.1.9
Release:        1%{?dist}
Summary:        The comprehensive WSGI web application library.
License:        BSD-3-Clause
URL:            https://github.com/pallets/werkzeug/
Source0:        https://files.pythonhosted.org/packages/source/w/werkzeug/werkzeug-%{version}.tar.gz
BuildArch:      noarch
Patch:          preserve-any-existing-PYTHONPATH-in-tests.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 5
BuildRequires:  python3dist(flit-core) >= 3.11
Requires:       python3-werkzeug = %{version}-%{release}
# /oreon:deps
%package -n       python3-werkzeug+watchdog
Summary:        Metapackage for python3-werkzeug watchdog extras
Requires:       python3-werkzeug = %{version}-%{release}
Requires:       python3dist(watchdog) >= 2.3
Provides:       python3dist(werkzeug[watchdog]) = %{version}-%{release}

%description -n python3-werkzeug+watchdog
Metapackage for python3-werkzeug watchdog extras.

%description

%package -n     python3-werkzeug
Summary:        The comprehensive WSGI web application library.
# oreon:reqs
Requires:       python3dist(markupsafe) >= 2.1.1
# /oreon:reqs
%description -n python3-werkzeug

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir werkzeug-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-werkzeug usr/lib/python3*/site-packages/werkzeug* usr/lib64/python3*/site-packages/werkzeug* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/werkzeug* usr/lib64/python3*/site-packages/werkzeug* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-werkzeug -f %{oreon_filedir}/python3-werkzeug.list

%changelog

%autochangelog
