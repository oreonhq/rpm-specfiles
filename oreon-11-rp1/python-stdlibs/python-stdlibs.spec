%global source0_hash 10f911bdd8d3e45b452cc187b3527e6f9d288c8a943c5f973da94c71b2757d5b

Name:           python-stdlibs
Version:        2026.2.26
Release:        %autorelease
Summary:        List of packages in the stdlib

License:        MIT
URL:            https://stdlibs.omnilib.dev
Source:         %{pypi_source stdlibs}
# use tomllib instead of the deprecated toml
Patch:          stdlibs-use-tomllib.diff

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(moreorless)

%global _description %{expand:
This package provides a static listing of all known modules in the Python
standard library, with separate lists available for each major release dating
back to Python 2.3. It also includes combined lists of all module names that
were ever available in any 3.x release, any 2.x release, or both.

Note: On Python versions 3.10 or newer, a list of module names for the active
runtime is available sys.stdlib_module_names. This package exists to provide an
historical record for use with static analysis and other tooling.

This package only includes listings for CPython releases. If other runtimes
would be useful, open an issue and start a discussion on how best that can be
accomodated.}

%description %_description

%package -n     python3-stdlibs
Summary:        %{summary}

%description -n python3-stdlibs %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n stdlibs-%{version}
# not intended for use by consumers of the library
# see https://github.com/omnilib/stdlibs/pull/105
rm stdlibs/fetch.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -L stdlibs

%check
%pyproject_check_import
%py3_test_envvars %python3 -m unittest -v

%files -n python3-stdlibs -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
