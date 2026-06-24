%global source0_hash none

%{?python_enable_dependency_generator}

%if 0%{?rhel} == 8
%global py3 python3
%global py3dev python36
%endif
%if 0%{?rhel} >= 9
%global py3 python3
%global py3dev python3
%endif
%if 0%{?fedora} || 0%{?rhel} >= 9
%global py3 python3
%global py3dev python3
%endif

%global library kubernetes

Name:       python-%{library}
Epoch:      1
Version:    36.0.2
Release:    2%{?dist}
Summary:    Python client for the kubernetes API.
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:    Apache-2.0
URL:        https://pypi.python.org/pypi/kubernetes

Source0:    https://github.com/kubernetes-client/python/archive/v%{version}.tar.gz
BuildArch:  noarch

%package -n %{py3}-%{library}
Summary:    Kubernetes Python Client
BuildRequires:  git-core
BuildRequires:  %{py3dev}-devel

%generate_buildrequires
%pyproject_buildrequires

%if %{undefined __pythondist_requires}
%if 0%{?fedora}
Requires:  %{py3}-adal
%endif
Requires:  %{py3}-certifi
Requires:  %{py3}-six
Requires:  %{py3}-dateutil
Requires:  %{py3}-setuptools
Requires:  %{py3}-urllib3
Requires:  %{py3}-PyYAML
Requires:  %{py3}-google-auth
Requires:  %{py3}-websocket-client
Requires:  %{py3}-oauthlib
Requires:  %{py3}-durationpy
%endif

%description -n %{py3}-%{library}
Python client for the kubernetes API.

%package -n %{py3}-%{library}-tests
Summary:    Tests python-kubernetes library

Requires:  %{py3}-%{library} = 1:%{version}-%{release}

%description -n %{py3}-%{library}-tests
Tests python-kubernetes library

#recommonmark not available for docs in EPEL
%if 0%{?fedora}
%package doc
Summary: Documentation for %{name}.
Provides: %{name}-doc = 1:%{version}-%{release}
BuildRequires: %{py3}-sphinx
BuildRequires: %{py3}-recommonmark
%description doc
%{summary}
%endif

%description
Python client for the kubernetes API.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n python-%{version} -S git

#This is needed until CentOS 8.1. The dep was
#updated because of a CVE in urllib3 and the
#corresponding package update is in EL 8.1
%if 0%{?rhel} == 8
sed -i 's/1.24.2/1.23/g' requirements.txt
%endif

sed -i 's/^mock.*//g' test-requirements.txt
sed -i 's/^nose.*//g' test-requirements.txt
sed -i 's/^py>.*//g' test-requirements.txt

#BZ1758141 - python autorequires do not handles asterisks properly.
#Fedora is using 0.56.0+ since at least Fedora 31 so this works aorund
#the issue by setting the minimum version above the problem versions.
%if 0%{?fedora} > 30
sed -i 's/websocket-client.*/websocket-client>=0.43.0/g' requirements.txt
%endif

%build
%pyproject_wheel

#11.0 adds spinx-markdown-tables as a requirement
#It is not packaged in Fedora
#%if 0%{?fedora}
#sphinx-build doc/source/ html
#%{__rm} -rf html/.buildinfo
#%endif

# Currently recommonmark requires an old version of commonmark,
# commonmark (<=0.5.4) wich doesn't exist in fedora rawhide so
# we disable docs generation until recommonmark is fixed to be
# compatible with recent version.
# generate html docs
# {__python2} setup.py build_sphinx
# remove the sphinx-build leftovers
#rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
cp -pr kubernetes/test %{buildroot}%{python3_sitelib}/%{library}/
cp -pr kubernetes/e2e_test %{buildroot}%{python3_sitelib}/%{library}/

%check

%if 0%{?fedora}
%files doc
%license LICENSE
#%doc html
%endif

%files -n %{py3}-%{library}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{library}
%{python3_sitelib}/%{library}-*.dist-info
%exclude %{python3_sitelib}/%{library}/test
%exclude %{python3_sitelib}/%{library}/e2e_test

%files -n %{py3}-%{library}-tests
%license LICENSE
%{python3_sitelib}/%{library}/test
%{python3_sitelib}/%{library}/e2e_test

%changelog
%autochangelog

