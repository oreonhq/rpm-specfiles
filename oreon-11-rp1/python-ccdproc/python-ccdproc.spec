%global source0_hash 051b42884cd3188e22dbd2d788c37e0d57bead7c906e479da9a2ecabb44ebdfa

%global srcname ccdproc
%global summary Astropy affiliated package for reducing optical/IR CCD data

Name:           python-%{srcname}
Version:        2.5.1
Release:        %autorelease
Summary:        %{summary}

License:        BSD-3-Clause
URL:            http://ccdproc.readthedocs.io/
Source0:        %{pypi_source}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
The ccdproc package is a collection of code that will be helpful in basic CCD
processing. These steps will allow reduction of basic CCD data as either a
stand-alone processing or as part of a pipeline.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-setuptools

%description -n python3-%{srcname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires 

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files ccdproc

%check
# Tests require memory-profiler, not in Fedora
%pyproject_check_import -t

%files -n python3-%{srcname} -f %{pyproject_files}
# https://github.com/astropy/ccdproc/issues/872
#license LICENSE.rst licenses/LICENSE_STSCI_TOOLS.txt
%license LICENSE.rst 
%doc AUTHORS.rst README.rst

%changelog
%autochangelog
