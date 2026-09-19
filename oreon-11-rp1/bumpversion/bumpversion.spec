%global source0_hash b0864d58b0ef231f99fef85ee028633d9366557a748e29cd92df0aa94f83f5fc

%if 0%{?rhel}
# https://bugzilla.redhat.com/show_bug.cgi?id=2125297
%bcond_with tests
%else
%bcond_without tests
%endif

Name:           bumpversion
Version:        1.0.1
Release:        19%{?dist}
Summary:        Version-bump your software with a single command

License:        MIT
URL:            https://github.com/c4urself/bump2version
Source0:        %{url}/archive/v%{version}/bump2version-%{version}.tar.gz
# sre_constants was removed in Python 3.15 (rhbz#2414558), use more modern re exception
Patch0:         0001-Python_3.15_compat_sre_constants.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%if %{with tests}
BuildRequires:  python3-pytest
BuildRequires:  python3-testfixtures
%endif

%description
A small command line tool to simplify releasing software by updating all
version strings in your source code by the correct increment. Also creates
commits and tags:

 * version formats are highly configurable
 * works without any VCS, but happily reads tag information from and writes
    commits and tags to Git and Mercurial if available
 * just handles text files, so it's not specific to any programming language

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n bump2version-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%if %{with tests}
%check
%pytest -k "not test_usage_string and not test_defaults_in_usage_with_config"
%endif

%install
%pyproject_install

%files
%doc README.md
%license LICENSE.rst
%attr(0755,root,root) %{_bindir}/{bumpversion,bump2version}
%{python3_sitelib}/bumpversion/
%{python3_sitelib}/bump2version-%{version}.dist-info/

%changelog
%autochangelog
