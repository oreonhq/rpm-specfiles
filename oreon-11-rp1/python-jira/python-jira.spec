%global source0_hash ca255690116b6161f131dcd230ad75ed18739db43e59aaf65d302eb9a131fafb
Name:               python-jira
Version:            3.10.5
Release:        1%{?dist}
Summary:        Python library for interacting with JIRA via REST APIs
License:            BSD-2-Clause
URL:                https://pypi.io/project/jira
Source0:        https://github.com/pycontribs/jira/archive/%{version}/jira-%{version}.tar.gz
Patch0:             https://github.com/pycontribs/jira/pull/2388.patch
BuildArch:          noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 60.0.0
BuildRequires:  python3dist(setuptools-scm[toml]) >= 7.0.0
Requires:       python3-jira = %{version}-%{release}
# /oreon:deps
%package -n       python3-jira+async
Summary:        Metapackage for python3-jira async extras
Requires:       python3-jira = %{version}-%{release}
Requires:       python3dist(requests-futures) >= 0.9.7
Provides:       python3dist(jira[async]) = %{version}-%{release}

%description -n python3-jira+async
Metapackage for python3-jira async extras.

%package -n       python3-jira+cli
Summary:        Metapackage for python3-jira cli extras
Requires:       python3-jira = %{version}-%{release}
Requires:       python3dist(ipython) >= 4.0.0
Provides:       python3dist(jira[cli]) = %{version}-%{release}

%description -n python3-jira+cli
Metapackage for python3-jira cli extras.

%package -n       python3-jira+docs
Summary:        Metapackage for python3-jira docs extras
Requires:       python3-jira = %{version}-%{release}
Requires:       python3dist(sphinx) >= 5.0.0
Provides:       python3dist(jira[docs]) = %{version}-%{release}

%description -n python3-jira+docs
Metapackage for python3-jira docs extras.

%package -n       python3-jira+opt
Summary:        Metapackage for python3-jira opt extras
Requires:       python3-jira = %{version}-%{release}
Requires:       python3dist(filemagic) >= 1.6
Provides:       python3dist(jira[opt]) = %{version}-%{release}

%description -n python3-jira+opt
Metapackage for python3-jira opt extras.

%package -n       python3-jira+test
Summary:        Metapackage for python3-jira test extras
Requires:       python3-jira = %{version}-%{release}
Requires:       python3dist(markupsafe) >= 0.23
Requires:       python3dist(pyyaml) >= 5.1
Requires:       python3dist(docutils) >= 0.21.2
Requires:       python3dist(parameterized) >= 0.8.1
Requires:       python3dist(pytest-timeout) >= 1.3.1
Requires:       python3dist(pytest-xdist) >= 2.2
Requires:       python3dist(pytest) >= 6.0.0
Requires:       python3dist(wheel) >= 0.24.0
Requires:       python3dist(yanc) >= 0.3.3
Provides:       python3dist(jira[test]) = %{version}-%{release}

%description -n python3-jira+test
Metapackage for python3-jira test extras.

%description

%package -n python3-jira
Summary:        Python library for interacting with JIRA via REST APIs
# oreon:reqs
Requires:       python3dist(requests) >= 2.10.0
Requires:       python3dist(requests-oauthlib) >= 1.1.0
Requires:       python3dist(typing-extensions) >= 3.7.4.2
# /oreon:reqs
%description -n python3-jira

%package -n jirashell
Requires: python3-ipython
Requires: python3-keyring
Requires: python3-jira == %{version}
Summary: Interactive Jira shell
%description -n jirashell
Interactive Jira shell using jira Python library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n jira-%{version}

sed -i "s/--cov-report=xml --cov jira//" pyproject.toml

%build

export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel
%install
%pyproject_install
rm -r %{buildroot}/%{python3_sitelib}/tests
grep -v -w 'jirashell' "%{pyproject_files}" >python3-jira.files
grep    -w 'jirashell' "%{pyproject_files}" >jirashell.files
%oreon_autofiles python3-jira usr/lib/python3*/site-packages/jira* usr/lib64/python3*/site-packages/jira* usr/bin/*
%oreon_autofiles jirashell usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/lib/python3*/site-packages/jira* usr/lib64/python3*/site-packages/jira* usr/bin/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pytest tests/resources/test_customer.py tests/resources/test_generic_resource.py \
        tests/resources/test_issue_link_type.py tests/resources/test_request_type.py \
        tests/resources/test_role.py tests/test_client.py tests/test_exceptions.py \
        tests/test_resilientsession.py tests/test_qsh.py tests/test_shell.py \
        -k "not test_delete_project and \
            not test_delete_inexistent_project and \
            not test_templates and \
            not test_token_auth and \
            not test_cookie_auth and \
            not test_cookie_auth_retry and \
            not test_createmeta_issuetypes_pagination and \
            not test_createmeta_fieldtypes_pagination"
%files
%files -n python3-jira -f %{oreon_filedir}/python3-jira.list
%files -n jirashell -f %{oreon_filedir}/jirashell.list

%changelog

%autochangelog
