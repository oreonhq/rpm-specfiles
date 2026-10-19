%global source0_hash 44f06f9195427c7017f5028d0894f57eb216b0a8f7c4eda7ce883732aeb2d0fc
Name:           glad2
Version:        2.0.8
Release:        1%{?dist}
Summary:        Multi-Language GL/GLES/EGL/GLX/WGL Loader-Generator
License:        MIT AND Apache-2.0
URL:            https://github.com/Dav1dde/glad
Source0:        https://github.com/Dav1dde/glad/archive/refs/tags/v%{version}.tar.gz#/glad-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.0
Requires:       python3-glad2 = %{version}-%{release}
# /oreon:deps
%package -n       python3-glad2+fortran
Summary:        Metapackage for python3-glad2 fortran extras
Requires:       python3-glad2 = %{version}-%{release}
Provides:       python3dist(glad2[fortran]) = %{version}-%{release}

%description -n python3-glad2+fortran
Metapackage for python3-glad2 fortran extras.

%description
Glad uses the official Khronos-XML specs to generate a GL/GLES/EGL/GLX/WGL
Loader made for your needs.

%package -n python3-glad2
Summary:        Python modules for %{name}
Requires:       python3dist(setuptools)
# oreon:reqs
Requires:       python3dist(jinja2) < 4.0
Requires:       python3dist(jinja2) >= 2.7
# /oreon:reqs
%description -n python3-glad2
Python modules for the glad2 loader generator.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n glad-%{version}
sed -i -e '/^#!\//, 1d' glad/__main__.py

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-glad2 usr/lib/python3*/site-packages/glad2* usr/lib64/python3*/site-packages/glad2* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/glad2* usr/lib64/python3*/site-packages/glad2* usr/bin/*

%check

%pyproject_check_import
%files
%files -n python3-glad2 -f %{oreon_filedir}/python3-glad2.list

%changelog

%autochangelog
