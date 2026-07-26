%global source0_hash 0212ef2727ac9caa5ca4b2c75ae89454312f440a756fcfc8ef1993e718f50f8a

%global srcname imageio

Name: python-%{srcname}
Version: 2.37.2
Release: %autorelease
Summary: Python IO of image, video, scientific, and volumetric data formats.
License: BSD-2-Clause
URL: https://imageio.github.io
Source0: %{pypi_source}

BuildArch: noarch
BuildRequires: python3-devel

%global _description %{expand:
Imageio is a Python library that provides an easy interface to read and write a wide range of image data, including animated images, volumetric data, and scientific formats.}

%description %_description

%package -n python3-%{srcname}
Summary: %{summary}
BuildRequires: python3-setuptools

%description -n python3-%{srcname}
%_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files imageio

%check
# Testing requires image sample, either local or from the internet
%pyproject_check_import -t

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md 
# Exclude files that download binary freeimage library
%exclude %{_bindir}/imageio*

%changelog
%autochangelog
