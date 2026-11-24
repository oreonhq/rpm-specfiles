# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash b84079b9fa404f37171b961bdd1d8da21370e6c818defb8481c5b3fe3d6436da
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global srcname glad2

Name:           python-%{srcname}
Version:        2.0.8
Release:        %{autorelease}
Summary:        Multi-Language GL/GLES/EGL/GLX/WGL Loader-Generator

License:        MIT and Apache-2.0
URL:            https://github.com/Dav1dde/glad
Source0:        %pypi_source %{srcname}
BuildArch:      noarch

BuildRequires: oreon-rpm-macros
BuildRequires:  python3-devel

%description
Glad uses the official Khronos-XML specs to generate a GL/GLES/EGL/GLX/WGL
Loader made for your needs.

%package -n     %{srcname}
Summary:        %{summary}

Requires:       python3-glad2 = %{version}-%{release}

%description -n %{srcname}
Glad uses the official Khronos-XML specs to generate a GL/GLES/EGL/GLX/WGL
Loader made for your needs.

%package -n     python3-%{srcname}
Summary:        %{summary}

Conflicts:      python3-glad

%description -n python3-%{srcname}
Glad uses the official Khronos-XML specs to generate a GL/GLES/EGL/GLX/WGL
Loader made for your needs.

%prep
%oreon_sha256
%autosetup -n %{srcname}-%{version}
sed -i -e '1{\@^#!@d}' glad/__main__.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l glad

%files -n %{srcname}
%doc README.md
%license LICENSE
%{_bindir}/glad

%files -n python3-%{srcname} -f %{pyproject_files}

%changelog
%autochangelog
