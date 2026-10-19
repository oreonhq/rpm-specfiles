%global source0_hash fcc23201e319d79fe25e064847efc254bd39ac30af28cc761409e1f9142dd033
Name:           python-vhacdx
Version:        0.0.10
Release:        1%{?dist}
Summary:        Python bindings for V-HACD
License:        MIT AND BSD-3-Clause
URL:            https://github.com/trimesh/vhacdx
Source0:        https://files.pythonhosted.org/packages/source/v/vhacdx/vhacdx-%{version}.tar.gz
%global common_description %{expand:
A very simple and raw Python binding for V-HACD that is forked from
https://github.com/thomwolf/pyVHACD which generates an approximate convex
decomposition of a triangle mesh.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(pybind11) >= 2.13.1
BuildRequires:  python3dist(setuptools) >= 42
Requires:       python3-vhacdx = %{version}-%{release}
# /oreon:deps
%package -n       python3-vhacdx+test
Summary:        Metapackage for python3-vhacdx test extras
Requires:       python3-vhacdx = %{version}-%{release}
Provides:       python3dist(vhacdx[test]) = %{version}-%{release}

%description -n python3-vhacdx+test
Metapackage for python3-vhacdx test extras.

%description %{common_description}

%package -n python3-vhacdx
Summary:        Python bindings for V-HACD
%description -n python3-vhacdx %{common_description}

%prep

%autosetup -p1
# Remove the bundled copy of the V-HACD library (use the system one instead).
rm -v src/vhacdx/VHACD.h

%install
%pyproject_install
find '%{buildroot}%{python3_sitearch}' -type f -name '*.cpp' -print -delete
sed -r -i '/\.cpp$/d' '%{pyproject_files}'
%oreon_autofiles python3-vhacdx usr/lib/python3*/site-packages/vhacdx* usr/lib64/python3*/site-packages/vhacdx* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/vhacdx* usr/lib64/python3*/site-packages/vhacdx* usr/bin/*

%build

%pyproject_wheel
%check

%pytest
%files
%files -n python3-vhacdx -f %{oreon_filedir}/python3-vhacdx.list

%changelog

%autochangelog
