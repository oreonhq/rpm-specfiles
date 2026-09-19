%global source0_hash 66f4889fd8e39dddf46fe498615d36156d494f6a2bec53886baf1c2c54322861

%global srcname pyvo

%global sum Access to remote data and services of the Virtual observatory (VO) using Python
%global desc                                                             \
PyVO is a package providing access to remote data and services of the    \
Virtual Observatory (VO) using Python.                                   \
                                                                         \
The pyvo module currently provides these main capabilities:              \
* Find archives that provide particular data of a particular type and/or \
  relates to a particular topic                                          \
* Search an archive for datasets of a particular type                    \
* Do simple searches on catalogs or databases                            \
* Get information about an object via its name                   

Name:           python-%{srcname}
Version:        1.8
Release:        %autorelease
Summary:        %{sum}

License:        BSD-3-Clause
URL:            https://github.com/astropy/%{srcname}
Source:        %{pypi_source %{srcname}} 

BuildArch:      noarch

BuildRequires:  python3-devel

Provides:       python3-pyvo-doc = %{version}-%{release}
Obsoletes:      python3-pyvo-doc = %{version}-%{release}

%description
%{desc}

%package -n python3-%{srcname}
Summary:        %{sum}
Requires:       astropy-tools
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} 

%generate_buildrequires
%pyproject_buildrequires -e %{toxenv}-test

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files pyvo

%check
%tox

%files -n python3-%{srcname} -f %{pyproject_files}
%license licenses/LICENSE.rst
%doc CHANGES.rst README.rst

%changelog
%autochangelog
