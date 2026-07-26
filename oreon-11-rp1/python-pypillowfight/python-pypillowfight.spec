%global source0_hash none

%global srcname pypillowfight

Name:           python-%{srcname}
Version:        0.3.1
Release:        %autorelease
Summary:        Various image processing algorithms

License:        GPL-2.0-or-later
URL:            https://gitlab.gnome.org/World/OpenPaperwork/libpillowfight
# PyPI tarball does not include tests.
Source:         https://gitlab.gnome.org/World/OpenPaperwork/libpillowfight/-/archive/%{version}/libpillowfight-%{version}.tar.gz
# Because Fedora 32-bit does not necessarily support SSE2.
Patch0001:      0001-Do-not-override-compile-args.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

%global _description \
Library containing various image processing algorithms: Automatic Color \
Equalization, Unpaper's algorithms, Stroke Width Transformation, etc.

%description %{_description}

%package -n     python3-%{srcname}
Summary:        %{summary}

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%description -n python3-%{srcname} %{_description}

%prep
%autosetup -n libpillowfight-%{version} -p1

echo "#define INTERNAL_PILLOWFIGHT_VERSION \"%{version}\"" > src/pillowfight/_version.h

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l pillowfight

%check
# https://gitlab.gnome.org/World/OpenPaperwork/libpillowfight/issues/11
%{pytest} -ra --ignore 'tests/test_swt.py' --ignore 'tests/test_canny.py'

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
