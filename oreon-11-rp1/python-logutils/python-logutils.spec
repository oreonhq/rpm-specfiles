%global source0_hash bc058a25d5c209461f134e1f03cab637d66a7a5ccc12e593db56fbb279899a82

%global modname logutils

Name:               python-%{modname}
Version:            0.3.5
Release:            36%{?dist}
Summary:            Logging utilities

# Automatically converted from old format: BSD - review is highly recommended.
License:            LicenseRef-Callaway-BSD
URL:                https://pypi.io/project/logutils
Source0:            https://pypi.io/packages/source/l/%{modname}/%{modname}-%{version}.tar.gz

Patch0:             0001-remove-test_hashandlers.patch

BuildArch:          noarch

BuildRequires:      python3-devel
BuildRequires:      python3-setuptools
BuildRequires:      python3-pytest
BuildRequires:      python3-redis
#BuildRequires:      /usr/bin/redis-server

%global _description\
The logutils package provides a set of handlers for the Python standard\
library's logging package.\
\
Some of these handlers are out-of-scope for the standard library, and so\
they are packaged here. Others are updated versions which have appeared in\
recent Python releases, but are usable with older versions of Python and so\
are packaged here.

%description %_description

%package -n python3-logutils
Summary:            Logging utilities
%{?python_provide:%python_provide python3-logutils}

%description -n python3-logutils
The logutils package provides a set of handlers for the Python standard
library's logging package.

Some of these handlers are out-of-scope for the standard library, and so
they are packaged here. Others are updated versions which have appeared in
recent Python releases, but are usable with older versions of Python and so
are packaged here.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{modname}-%{version} -p 1

%generate_buildrequires
%pyproject_buildrequires

# Remove bundled egg-info in case it exists
rm -rf %{modname}.egg-info

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files %{modname}

%check
%pyproject_check_import %{modname}

#%%pytest

%files -n python3-%{modname}
%license LICENSE.txt
%doc README.rst NEWS.txt doc/
%{python3_sitelib}/%{modname}/
%{python3_sitelib}/%{modname}-%{version}.dist-info/

%changelog
%autochangelog
