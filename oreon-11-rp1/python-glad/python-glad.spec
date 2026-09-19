%global source0_hash 3fb00dbfec7ae6ddbeba04e21547f67f3ccfc795fc34562450cf3f2bb19fdbc7

%global srcname glad

Name:           python-%{srcname}
Version:        0.1.36
Release:        %autorelease
Summary:        Multi-Language GL/GLES/EGL/GLX/WGL Loader-Generator

# Mostly MIT, Apache-2.0 for Khronos and EGL specifications/headers.
License:        MIT and Apache-2.0
URL:            https://github.com/Dav1dde/glad
Source0:        %pypi_source glad
BuildArch:      noarch

BuildRequires:  python3-devel

%description
Glad uses the official Khronos-XML specs to generate a GL/GLES/EGL/GLX/WGL
Loader made for your needs.

%package -n     %{srcname}
Summary:        %{summary}

Requires:       python3dist(glad)

%description -n %{srcname}
Glad uses the official Khronos-XML specs to generate a GL/GLES/EGL/GLX/WGL
Loader made for your needs.

%package -n     python3-%{srcname}
Summary:        %{summary}

Requires:       python3dist(setuptools)

%description -n python3-%{srcname}
Glad uses the official Khronos-XML specs to generate a GL/GLES/EGL/GLX/WGL
Loader made for your needs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

# Fix shebang
sed -i -e '/^#!\//, 1d' %{srcname}/__main__.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%pyproject_check_import

%files -n %{srcname}
%{_bindir}/glad

%files -n python3-%{srcname} -f %{pyproject_files}

%changelog
%autochangelog
