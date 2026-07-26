%global source0_hash 06b6abf7de2fc0a63846f6cb9aff15fb43f195a50aae32a058f61c91bcd400d4

%global github_owner    kevin1024
%global github_name     pytest-httpbin
%global modname         pytest_httpbin

%global desc Pytest-httpbin creates a pytest fixture that is dependency-injected into your \
tests. It automatically starts up a HTTP server in a separate thread running \
a local instance of httpbin (a web service for testing HTTP libraries) and \
provides your test with the URL in the fixture.

%global sum Fixture providing local instance of httpbin test service

Name:           python-%{github_name}
Version:        2.1.0
Release:        7%{?dist}
Summary:        %{sum}

# License is included in-line in README.md
License:        MIT
URL:            https://github.com/%{github_owner}/%{github_name}
# NOTE: the source includes a CA trust bundle (certs/cacert.pem). We
# don't replace it with the system-wide trust bundle because it's only
# used for httpbin itself and contains only the self-signed cert,
# valid only for 127.0.0.1, that the test server uses. We can't
# replace it because we can't actually securely have the test server
# use a cert that would be trusted by the system-wide trust bundle.
%global ghversion %(v=%{version}; echo $v | sed -r "s,[\\^~],,g")
Source0:        https://github.com/%{github_owner}/%{github_name}/archive/v%{ghversion}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%description
%{desc}

#################################################################################
%package -n python3-%{github_name}
Summary:        %{sum}

%description -n python3-%{github_name}
%{desc}

This package provides the Python 3 implementation.

#################################################################################
%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{github_name}-%{ghversion} -p1

%generate_buildrequires
%pyproject_buildrequires -x test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{modname}

#################################################################################
%check
# we don't use tox because upstream's tox config is a bit odd and has
# an unsatisfiable dependency that's only relevant to Github Actions
%pytest

#################################################################################
%files -n python3-%{github_name} -f %{pyproject_files}
%doc DESCRIPTION.rst README.md

#################################################################################
%changelog
%autochangelog
