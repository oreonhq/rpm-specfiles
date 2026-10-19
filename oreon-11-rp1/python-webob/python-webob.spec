%global source0_hash aa8c27231070b135c025e567a9cd7eda03f4df71352ffaac740cb6a75f0f81a5
%bcond tests 1
%global desc WebOb provides wrappers around the WSGI request environment, and an object to \
help create WSGI responses. The objects map much of the specified behavior of \
HTTP, including header parsing and accessors for other standard parts of the \
environment.
Name:           python-webob
Summary:        WSGI request and response object
Version:        1.8.11
Release:        7%{?dist}
License:        MIT
URL:            https://webob.org
Source0:        https://files.pythonhosted.org/packages/source/w/webob/webob-%{version}.tar.gz
BuildArch:      noarch
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-webob = %{version}-%{release}
# /oreon:deps
%description
%{desc}

%package -n python3-webob
Summary:        WSGI request and response object
%description -n python3-webob
%{desc}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n webob-%{version}
# Disable performance_test, which requires repoze.profile, which isn't
# in Fedora.
rm -f tests/performance_test.py

# Remove an empty unneeded file that is there for scm purposes.
rm docs/_static/.empty

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-webob usr/lib/python3*/site-packages/webob* usr/lib64/python3*/site-packages/webob* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/webob* usr/lib64/python3*/site-packages/webob* usr/bin/*

%check

%if %{with tests}
%pytest -k "not test_interrupted_request"
%else
%pyproject_check_import
%endif
%files
%files -n python3-webob -f %{oreon_filedir}/python3-webob.list

%changelog

%autochangelog
