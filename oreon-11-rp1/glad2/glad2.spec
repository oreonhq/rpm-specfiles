%global source0_hash 44f06f9195427c7017f5028d0894f57eb216b0a8f7c4eda7ce883732aeb2d0fc

Name:           glad2
Version:        2.0.8
Release:        %autorelease
Summary:        Multi-Language GL/GLES/EGL/GLX/WGL Loader-Generator
License:        MIT AND Apache-2.0
URL:            https://github.com/Dav1dde/glad
Source0:        https://github.com/Dav1dde/glad/archive/refs/tags/v%{version}.tar.gz#/glad-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel

%description
Glad uses the official Khronos-XML specs to generate a GL/GLES/EGL/GLX/WGL
Loader made for your needs.

%package -n python3-glad2
Summary:        Python modules for %{name}
Requires:       python3dist(setuptools)

%description -n python3-glad2
Python modules for the glad2 loader generator.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n glad-%{version}
sed -i -e '/^#!\//, 1d' glad/__main__.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files glad

%check
%pyproject_check_import

%files
%{_bindir}/glad

%files -n python3-glad2 -f %{pyproject_files}

%changelog
%autochangelog
