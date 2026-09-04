%global source0_hash 908d25e6c8d120624c31a842eb93336fe4527ac364fc46e172f33fe2204ce31c

%global pkgname repoze.sphinx.autointerface
%global srcname %(tr . - <<< %{pkgname})

Name:           python-%{srcname}
Version:        1.1.0
Release:        1%{?dist}
Summary:        Auto-generate Sphinx API docs from Zope interfaces

License:        BSD-3-Clause-Modification
URL:            https://github.com/repoze/%{pkgname}
Source0:        https://github.com/repoze/%{pkgname}/archive/%{version}/%{pkgname}-%{version}.tar.gz
# Adapt to Sphinx 7.2+ and 8.2+
Patch0:         https://github.com/repoze/repoze.sphinx.autointerface/pull/22.patch

BuildArch:      noarch

BuildRequires:  python3-devel

# There is a test dependency loop, so we need a way to build this without tests
# repoze.sphinx.autointerface -> zope.testrunner -> zope.exceptions -> repoze.sphinx.autointerface
%bcond tests 1

%global common_desc %{expand:
This package defines an extension for the Sphinx documentation system.
The extension allows generation of API documentation by introspection of
zope.interface instances in code.}

%description %{common_desc}

%package -n python3-%{srcname}
Summary:        Auto-generate Sphinx API docs from Zope interfaces

%description -n python3-%{srcname} %{common_desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pkgname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires %{?with_tests:-x test}

%build
%pyproject_wheel
rst2html --no-datestamp CHANGES.rst CHANGES.html
rst2html --no-datestamp README.rst README.html

%install
%pyproject_install
%pyproject_save_files -L repoze

%check
%pyproject_check_import
%if %{with tests}
export PYTHONPATH=$PWD/build/lib
zope-testrunner --test-path=$PWD/build/lib
%endif

%files -n python3-%{srcname}
%doc CHANGES.html CONTRIBUTORS.txt README.html
%license COPYRIGHT.txt LICENSE.txt
%{python3_sitelib}/repoze*

%changelog
%autochangelog
