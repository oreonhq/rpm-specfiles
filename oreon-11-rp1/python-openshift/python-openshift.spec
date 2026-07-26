%global source0_hash c06139978cd576cad5a275990ea186feccbeb360ef8cebf25d0c652ef91c1088

%if 0%{?rhel} == 7
%bcond_with    python3
%bcond_without python2
%else
%bcond_with    python2
%bcond_without python3
%endif

%global library openshift

%if 0%{?rhel} == 7
%global py3 python%{python3_pkgversion}
%global py3dev python%{python3_pkgversion}
%endif
%if 0%{?rhel} == 8
%global py3 python3
%global py3dev python36
%endif
%if 0%{?rhel} >= 9
%global py3 python3
%global py3dev python3
%endif
%if 0%{?fedora}
%global py3 python3
%global py3dev python3
%endif

Name:       python-%{library}
Version:    0.13.2
Release:    12%{?dist}
Summary:    Python client for the OpenShift API
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:    Apache-2.0
URL:        https://github.com/openshift/openshift-restclient-python
Source0:    https://github.com/openshift/openshift-restclient-python/archive/v%{version}.tar.gz
BuildArch:  noarch
Epoch:      1

%if 0%{?with_python2}
%package -n python2-%{library}
Summary:    Python client for the OpenShift API
%{?python_provide:%python_provide python2-%{library}}

BuildRequires: python2-devel
%if 0%{?rhel} != 7
BuildRequires: python2-kubernetes
%endif
BuildRequires: python-pytest
BuildRequires: python-setuptools
BuildRequires: git

Requires: python2
Requires: python2-dictdiffer
Requires: python2-kubernetes >= 9.0.0
Requires: python2-string_utils
Requires: python-requests
Requires: python2-ruamel-yaml
Requires: python-six
Requires: python-jinja2

%description -n python2-%{library}
Python client for the kubernetes API.
%endif

%if 0%{?with_python3}
%package -n %{py3}-%{library}
Summary: Python client for the OpenShift API
BuildRequires: %{py3dev}-devel
BuildRequires: %{py3dev}-rpm-macros
%if 0%{?rhel} != 7
BuildRequires: %{py3}-kubernetes >= 8.0.0
%endif
BuildRequires: %{py3}-pytest
BuildRequires: %{py3}-setuptools
BuildRequires: git

Requires: %{py3}
Requires: %{py3}-dictdiffer
Requires: %{py3}-kubernetes
Requires: %{py3}-string_utils
Requires: %{py3}-requests
Requires: %{py3}-ruamel-yaml
Requires: %{py3}-six
Requires: %{py3}-jinja2

%description -n %{py3}-%{library}
Python client for the OpenShift API
%endif

#recommonmark not available for docs in EPEL
%if 0%{?fedora}
%package doc
Summary: Documentation for %{name}.
%if 0%{?with_python3}
BuildRequires: %{py3}-sphinx
BuildRequires: %{py3}-recommonmark
%else
BuildRequires: python2-sphinx
BuildRequires: python2-recommonmark
%endif
%description doc
%{summary}
%endif

%description
Python client for the OpenShift API

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n openshift-restclient-python-%{version} -S git
#there is no include in RHEL7 setuptools find_packages
#the requirements are also done in an non-backwards compatible way
%if 0%{?rhel}
sed -i -e "s/find_packages(include='openshift.*')/['openshift', 'openshift.dynamic', 'openshift.helper']/g" setup.py
sed -i -e "49d" setup.py
%endif

#work around https://bugzilla.redhat.com/show_bug.cgi?id=1759100 in Fedora 31
sed -i 's/~/>/g' requirements.txt

%build
%if 0%{?with_python2}
%py2_build
%endif
%if 0%{?with_python3}
%py3_build
%endif

%if 0%{?fedora} >= 30
sphinx-build-3 doc/source/ html
%{__rm} -rf html/.buildinfo
%{__rm} -rf html/.doctrees
%endif

%if 0%{?fedora} > 28 && 0%{?fedora} < 30
sphinx-build doc/source/ html
%{__rm} -rf html/.buildinfo
%{__rm} -rf html/.doctrees
%endif

%install
%if 0%{?with_python2}
%py2_install
%endif
%if 0%{?with_python3}
%py3_install
%endif

%check
%if 0%{?rhel} != 7
export PYTHONPATH="$(pwd)"
%if 0%{?with_python2}
py.test test/unit -c /dev/null -v -r s
%endif
%if 0%{?with_python3}
py.test test/unit -c /dev/null -v -r s
%endif
%endif

%if 0%{?with_python2}
%files -n python2-%{library}
%license LICENSE
%{python2_sitelib}/%{library}
%{python2_sitelib}/%{library}-*.egg-info
%exclude %{python2_sitelib}/scripts
%endif

%if 0%{?with_python3}
%files -n %{py3}-%{library}
%license LICENSE
%{python3_sitelib}/%{library}
%{python3_sitelib}/%{library}-*.egg-info
%exclude %{python3_sitelib}/scripts
%endif

%if 0%{?fedora}
%files doc
%license LICENSE
%doc html
%endif

%changelog
%autochangelog
