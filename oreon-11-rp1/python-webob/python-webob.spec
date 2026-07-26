%global source0_hash ad6078e2edb6766d1334ec3dee072ac6a7f95b1e32ce10def8ff7f0f02d56589

%bcond tests 1

%global desc WebOb provides wrappers around the WSGI request environment, and an object to \
help create WSGI responses. The objects map much of the specified behavior of \
HTTP, including header parsing and accessors for other standard parts of the \
environment.

Name:           python-webob
Summary:        WSGI request and response object
Version:        1.8.9
Release:        7%{?dist}
License:        MIT
URL:            https://webob.org
Source:         %{pypi_source webob}

BuildArch:      noarch

BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  python3-pytest
%endif

%description
%{desc}

%package -n python3-webob
Summary:        %{summary}

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

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -L webob

%check
%if %{with tests}
# test_interrupted_request: https://github.com/Pylons/webob/issues/479
%pytest -k "not test_interrupted_request"
%else
%pyproject_check_import
%endif

%files -n python3-webob -f %{pyproject_files}
%license docs/license.txt
%doc docs/*

%changelog
%autochangelog
