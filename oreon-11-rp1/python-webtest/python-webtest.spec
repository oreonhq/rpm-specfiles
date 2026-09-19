%global source0_hash 7aeab50f970d46c068e7a36dd162cb242591edf72a1d04efd21374772b931741

%bcond tests 1

Name:           python-webtest
Version:        3.0.7
Release:        2%{?dist}
Summary:        Helper to test WSGI applications

License:        MIT
URL:            https://github.com/Pylons/webtest
Source:         %{pypi_source webtest}

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
WebTest wraps any WSGI application and makes it easy to send test requests to
that application, without starting up an HTTP server.

This provides convenient full-stack testing of applications written with any
WSGI-compatible framework.}

%description %_description

%package -n python3-webtest
Summary:        %{summary}

%description -n python3-webtest %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n webtest-%{version}

# remove coverage dependencies
sed -e '/coverage/d' \
    -e '/pytest-cov/d' \
    -i setup.py

%generate_buildrequires
%pyproject_buildrequires %{?with_tests:-x tests}

%build
%pyproject_wheel
# remove files not needed in documentation
rm -f docs/Makefile docs/conf.py docs/changelog.rst

%install
%pyproject_install
%pyproject_save_files webtest

%check
%if %{with tests}
%pytest
%else
%pyproject_check_import
%endif

%files -n python3-webtest -f %{pyproject_files}
%doc docs/* CHANGELOG.rst

%changelog
%autochangelog
