%global source0_hash 20de0e5dd5a18292d36d928cc3d6e52f8b2ac73daec40d41eb62dee154933b68
%global github_owner    gabrielfalcao
%global github_name     HTTPretty
%global srcname         httpretty
%global run_tests 0
Name:           python-httpretty
Version:        1.1.4
Release:        1%{?dist}
Summary:        HTTP request mock tool for Python
License:        MIT
URL:            https://github.com/%{github_owner}/%{github_name}
Source0:        https://files.pythonhosted.org/packages/source/h/httpretty/httpretty-1.1.4.tar.gz
Patch1:         python-httpretty-fakesock_getpeercert_noconnect.patch
Patch2:         skip-test_passthrough.patch
Patch3:         test_response-no-within.patch
Patch4:         test_handle_slashes.patch
Patch5:         chunked_requests_handled_by_urllib3.patch  
Patch6:         485.patch
Patch7:         remove_deprecations_in_python_3_13.patch
Patch8:         python-httpretty-rm-python-mock-usage.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-httpretty = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-httpretty
Summary:        HTTP request mock tool for Python 3
Requires:       python3-six
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip
BuildRequires:  python3-wheel
%description -n python3-httpretty
Once upon a time a python developer wanted to use a RESTful API, everything was
fine but until the day he needed to test the code that hits the RESTful API:
what if the API server is down? What if its content has changed?
Don't worry, HTTPretty is here for you.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n httpretty-%{version} -p1

%pyproject_buildrequires

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-httpretty usr/lib/python3*/site-packages/httpretty* usr/lib64/python3*/site-packages/httpretty* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/httpretty* usr/lib64/python3*/site-packages/httpretty* usr/bin/*

%check

%files
%files -n python3-httpretty -f %{oreon_filedir}/python3-httpretty.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1.4-1
- Prepare for Oreon 11 (RP1)
