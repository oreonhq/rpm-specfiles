%global source0_hash 8c5bc62c1784b0c4483caadda3564e47180648572dc15d16cfbe2622512bd97b

%global pypi_name pyroaring

Name:           python-%{pypi_name}
Version:        1.0.3
Release:        %{autorelease}
Summary:        Fast and lightweight set for unsigned 32 bits integers

%global forgeurl https://github.com/Ezibenroc/PyRoaringBitMap
%global tag %{version}
%forgemeta

# pyroaring/roaring.c and pyroaring/roaring.h are dual licensed
License:        MIT or Apache-2.0
URL:            %{forgeurl}
Source:         %{forgesource}

BuildRequires:  gcc, gcc-c++
BuildRequires:  python3-devel
BuildRequires:  python3-Cython

# Leaf package. Stop building for i686.
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

%global _description %{expand:
An efficient and light-weight ordered set of 32 bits integers. This is
a Python wrapper for the C library CRoaring.}

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%generate_buildrequires
%pyproject_buildrequires -e cython3

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%tox -e %{toxenv}
%pyproject_check_import

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.*

%changelog
%autochangelog
