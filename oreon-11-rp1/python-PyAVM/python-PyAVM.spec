%global source0_hash ce11c279ec75bdf823d0c386124a1528a5e7b36fa5dd4d26499227939f117f88

%global pypi_name PyAVM
%global srcname pyavm

Name: python-%{pypi_name}
Version: 0.9.8
Release: %autorelease
Summary: Python package to handle Astronomy Visualization Metadata
License: MIT AND BSD-3-Clause

URL: https://astrofrog.github.io/pyavm/
Source0: %{pypi_source}

BuildArch: noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

#BuildRequires: python3dist(astropy)
#BuildRequires: python3dist(pillow)

Recommends: python3dist(astropy)
Recommends: python3dist(pillow)

%global _description %{expand:
PyAVM is a Python module to represent, read, and write metadata 
following the *Astronomy Visualization Metadata* (AVM) standard.}     

%description %_description

%package -n python3-%{pypi_name}
Summary: %{summary}

%description -n python3-%{pypi_name}
%_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} 

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files pyavm

%check
%{tox}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst 

%changelog
%autochangelog
