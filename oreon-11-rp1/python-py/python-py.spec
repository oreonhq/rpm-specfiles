%global source0_hash 51c75c4126074b472f746a24399ad32f6053d1b34b68d2fa41e558e6f4a98719

%global srcname py

Name:           python-%{srcname}
Version:        1.11.0
Release:        20%{?dist}
Summary:        Library with cross-python path, ini-parsing, io, code, log facilities
# Automatically converted from old format: MIT and Public Domain - review is highly recommended.
License:        LicenseRef-Callaway-MIT AND LicenseRef-Callaway-Public-Domain
#               main package: MIT, except: doc/style.css: Public Domain
URL:            http://py.readthedocs.io/
Source:        https://files.pythonhosted.org/packages/source/p/python-py/python-py-1.11.0.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel

%description
The py lib is a Python development support library featuring the
following tools and modules:

  * py.path: uniform local and svn path objects
  * py.apipkg: explicit API control and lazy-importing
  * py.iniconfig: easy parsing of .ini files
  * py.code: dynamic code generation and introspection
  * py.path: uniform local and svn path objects


%package -n python3-%{srcname}
Summary:        Library with cross-python path, ini-parsing, io, code, log facilities
Requires:       python3-setuptools
Provides:       bundled(python3-apipkg) = 2.0
Provides:       bundled(python3-iniconfig) = 1.1.1
Obsoletes:      platform-python-%{srcname} < %{version}-%{release}

%description -n python3-%{srcname}
The py lib is a Python development support library featuring the
following tools and modules:

  * py.path: uniform local and svn path objects
  * py.apipkg: explicit API control and lazy-importing
  * py.iniconfig: easy parsing of .ini files
  * py.code: dynamic code generation and introspection
  * py.path: uniform local and svn path objects


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -n %{srcname}-%{version}

# remove shebangs and fix permissions
find . \
   -type f -a \( -name '*.py' -o -name 'py.*' \) \
   -exec sed -i '1{/^#!/d}' {} \; \
   -exec chmod u=rw,go=r {} \;


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l %{srcname}

# Remove bundled dist/egg-info directories, they shouldn't be shipped for
# bundled modules and in some cases they could confuse automatic generators
# that read the dist/egg-info data.
rm -rf %{buildroot}%{python3_sitelib}/py/_vendored_packages/*.{dist,egg}-info
sed -i -r -e '/\/py\/_vendored_packages\/.*(dist|egg)-info/d' %{pyproject_files}


%check
%pyproject_check_import

%py3_check_import %{srcname}

%files -n python3-%{srcname} -f %{pyproject_files}
%doc CHANGELOG.rst
%doc README.rst


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.11.0-20
- Prepare for Oreon 11 (RP1)
