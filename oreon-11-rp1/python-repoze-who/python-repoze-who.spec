%global source0_hash c528a6ac5a9e069ed5a3750aef377622ece53edd0087cfc0b685f2a24c064274

%global modname repoze.who

Name:           python-repoze-who
Version:        3.1.0
Release:        7%{?dist}
Summary:        An identification and authentication framework for WSGI

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://pypi.python.org/pypi/%{modname}
Source0:        %pypi_source repoze_who
BuildArch:      noarch

BuildRequires:      python3-devel
BuildRequires:      python3-pytest
BuildRequires:      python3-coverage
BuildRequires:      python3-zope-interface
BuildRequires:      python3-webob
BuildRequires:      python3dist(legacy-cgi)

%global _description\
repoze.who is an identification and authentication framework for arbitrary WSGI\
applications.  It acts as WSGI middleware.\
\
repoze.who is inspired by Zope 2's Pluggable Authentication Service (PAS) (but\
repoze.who is not dependent on Zope in any way; it is useful for any WSGI\
application).  It provides no facility for authorization (ensuring whether a\
user can or cannot perform the operation implied by the request).  This is\
considered to be the domain of the WSGI application.\

%description %_description

%package -n python3-repoze-who
Summary:        An identification and authentication framework for WSGI

%description -n python3-repoze-who
repoze.who is an identification and authentication framework for arbitrary WSGI
applications.  It acts as WSGI middleware.

repoze.who is inspired by Zope 2's Pluggable Authentication Service (PAS) (but
repoze.who is not dependent on Zope in any way; it is useful for any WSGI
application).  It provides no facility for authorization (ensuring whether a
user can or cannot perform the operation implied by the request).  This is
considered to be the domain of the WSGI application.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n repoze_who-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l repoze

%check
%pyproject_check_import

#PYTHONPATH=$(pwd) %%{__python3} setup.py test
%pytest -k "not test_crypt_check"

%files -n python3-repoze-who -f %{pyproject_files}
%doc README.rst CHANGES.rst CONTRIBUTORS.txt
%license COPYRIGHT.txt
%{python3_sitelib}/repoze.who-%{version}-py%{python3_version}-nspkg.pth

%changelog
%autochangelog
