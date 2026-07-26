%global source0_hash a24d818d6a836c131976d22f8c27b8d3ca32d0af64c1d8d29deb7bafa4da1eea

%global srcname affine

Name:           python-%{srcname}
Version:        2.4.0
Release:        %autorelease
Summary:        Matrices describing affine transformation of the plane

License:        BSD-3-Clause
URL:            https://github.com/sgillies/affine
Source0:        %pypi_source

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description \
Matrices describing affine transformation of the plane. The Affine package is \
derived from Casey Duncan's Planar package.

%description %{_description}

%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires -x test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%{pytest} -v --pyargs affine

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
