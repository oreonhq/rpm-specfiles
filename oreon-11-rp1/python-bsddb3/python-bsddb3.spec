%global source0_hash 70d05ec8dc568f42e70fc919a442e0daadc2a905a1cfb7ca77f549d49d6e7801

# Allow building with multiple Python versions in EPEL
%{?el7:%bcond_without python3_other}

# Metadata for Python-related macros (i.e. %%pypi_source)
## Upstream package/project name
%global srcname bsddb3

## Description common to all version-specific subpackages
%global common_description %{expand:
This package contains Python wrappers for Berkeley DB, the Open Source embedded
database system. The Python wrappers allow you to store Python string objects of
any length.}

Name:           python-%{srcname}
Version:        6.2.9
Release:        24%{?dist}
Summary:        Python 3 bindings for Berkeley DB

License:        BSD-3-Clause
URL:            https://pypi.org/project/bsddb3
Source0:        %{pypi_source}

# This change satisfies the rpath check during the build
# Currently, both Python's and setuptools' bundled distutils are patched to work
# around this issue, so the package doesn't fail even without this patch.
# As both patches may be removed in the future and it's possible to fix the
# package directly, it's better to do it here.
Patch0:          dont-include-standard-paths-in-runtime-libdir.patch
Patch1:          TextTestResult.patch
Patch2:          threads.patch
BuildRequires:  gcc libdb-devel

%description    %{common_description}

# Mainline Python 3 subpackage
%global python3_name        %{expand:python%{python3_pkgversion}-%{srcname}}
%package -n     %{python3_name}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-pip

%description -n %{python3_name} %{common_description}

# Alternative Python 3 subpackage
%if %{with python3_other}
%global python3_other_name  %{expand:python%{python3_other_pkgversion}-%{srcname}}
%package -n     %{python3_other_name}
Summary:        %{summary}
BuildRequires:  python%{python3_other_pkgversion}-devel
BuildRequires:  python%{python3_other_pkgversion}-setuptools

%description -n %{python3_other_name} %{common_description}
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

#%%generate_buildrequires
#%%pyproject_buildrequires

%build
%pyproject_wheel -C--global-option=--berkeley-db-incdir=%{_includedir} -C--global-option=--berkeley-db-libdir=%{_libdir}
%{?with_python3_other:%py3_other_build}

%install
# Helper installation functions
fix_scripts_shebangs_and_permissions() {
    local -r py_binary="$1"
    local -r py_install_dir="$2"

    local -r WRONG_SHEBANG='#!/usr/bin/python|#!/usr/bin/env python[[:digit:]]*'
    local -r CORRECT_SHEBANG="#!${py_binary}"

    # Fix shebangs
    grep --recursive --files-with-matches --null --extended-regexp \
        --regexp="${WRONG_SHEBANG}" "${py_install_dir}" \
    | xargs --null -- sed --regexp-extended --in-place \
        --expression="s@${WRONG_SHEBANG}@${CORRECT_SHEBANG}@"

    # Set correct permissions on scripts
    grep --recursive --files-with-matches --null --extended-regexp \
        --regexp="${CORRECT_SHEBANG}" "${py_install_dir}" \
    | xargs --null -- chmod 0755

    # Recompile bytecode for changed files
    %{py_byte_compile "${py_binary}" "${py_install_dir}"}
}

# Latter builds override former ones
%if %{with python3_other}
%py3_other_install
fix_scripts_shebangs_and_permissions %{__python3_other} \
    %{buildroot}%{python3_other_sitearch}/%{srcname}
%endif

%pyproject_install 
fix_scripts_shebangs_and_permissions %{__python3} \
    %{buildroot}%{python3_sitearch}/%{srcname}

# Get rid of unneeded header
rm -f %{buildroot}%{_includedir}/python3.*/%{srcname}/bsddb.h

%check
%{__python3} test.py
%{?with_python3_other:%{__python3_other} test.py}

%files -n %{python3_name}
%doc ChangeLog PKG-INFO README.txt
%license LICENSE.txt
%{python3_sitearch}/bsddb3/
%{python3_sitearch}/bsddb3-%{version}.dist-info

%if %{with python3_other}
%files -n %{python3_other_name}
%doc ChangeLog PKG-INFO README.txt
%license LICENSE.txt
%{python3_other_sitearch}/bsddb3/
%{python3_other_sitearch}/bsddb3-%{version}-py%{python3_other_version}.egg-info
%endif

%changelog
%autochangelog
