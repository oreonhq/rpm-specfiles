%global source0_hash 86f96a8195b0fd874bd67847f52435ac3c6bdbbfb8cb9a10a626711e6c9f616a
Name:           python-openslide
Version:        1.4.3
Release:        1%{?dist}
Summary:        Python bindings for the OpenSlide library
License:        LGPL-2.1-only
URL:            https://openslide.org/
Source0:        https://github.com/openslide/openslide-python/releases/download/v%{version}/openslide_python-%{version}.tar.xz
Patch0:         disable-intersphinx.patch
Patch1:         setuptools-version.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77.0.0
Requires:       python3-openslide = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-openslide
Summary:        Python bindings for the OpenSlide library
Requires:       openslide
%description -n python3-openslide

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n openslide_python-%{version} -p1

# Examples include bundled jQuery and OpenSeadragon
rm -rf examples

%build

%pyproject_wheel
sphinx-build doc build/html
rm -r build/html/.buildinfo build/html/.doctrees
%install
%pyproject_install
%oreon_autofiles python3-openslide usr/lib/python3*/site-packages/openslide* usr/lib64/python3*/site-packages/openslide* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/openslide* usr/lib64/python3*/site-packages/openslide* usr/bin/*

%check

%pytest
%files
%files -n python3-openslide -f %{oreon_filedir}/python3-openslide.list

%changelog

%autochangelog
