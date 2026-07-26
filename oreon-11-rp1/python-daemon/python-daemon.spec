%global source0_hash fdb621d7e5f46e74b4de1ad6b0fff6e69cd91b4f219de1476190ebdd0f4781df

Name:           python-daemon
Version:        3.1.0
Release:        %autorelease
Summary:        Library to implement a well-behaved Unix daemon process

# Some build scripts and test framework are licensed GPL-3.0-or-later but those aren't shipped
License:        Apache-2.0
URL:            https://pagure.io/python-daemon
Source:         %{pypi_source python_daemon}
# Downstream changes to some deps and metdata, for example:
# - changelog-chug is not packaged in Fedora
# - coverage and other static analysis tools are not needed here
# - version is dynamic but got via changelog-chug, use a placeholder
# - setuptools is not needed at runtime
Patch:          drop-dependencies-and-fix-dynamic-version.patch

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
This library implements the well-behaved daemon specification of PEP 3143,
"Standard daemon process library".}

%description %_description

%package -n python3-daemon
Summary:        %{summary}

%description -n python3-daemon %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n python_daemon-%{version}
# See the patch removing dependencies above
# - insert the actual version
sed -i "s/VERSION_PLACEHOLDER/%{version}/" pyproject.toml
# - setup.py is not needed, everything that remains is in pyproject.toml
# - test_setup.py tests importing of setup.py
# - test_util_* are not testing the libraty but packaging and other tools
rm setup.py test/test_setup.py test/test_util_metadata.py test/test_util_packaging.py

%generate_buildrequires
%pyproject_buildrequires -x test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files daemon

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} %python3 -m unittest discover

%files -n python3-daemon -f %{pyproject_files}
%doc README ChangeLog

%changelog
%autochangelog
