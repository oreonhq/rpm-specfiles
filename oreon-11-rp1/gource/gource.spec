%global source0_hash 332d89b9a979b17417fbce0edd72b19914f1409fd126a13d11787d0e15dc0d79
Summary:        Software version control visualization
Name: gource
Version: 0.56
Release:        1%{?dist}
URL: http://gource.io/
Source0:        https://github.com/acaudwell/Gource/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz
ExcludeArch: ppc64le
License: GPL-3.0-or-later
Requires: gnu-free-sans-fonts
# oreon:deps
BuildRequires:  SDL2-devel
BuildRequires:  SDL2_image-devel
BuildRequires:  boost-devel
BuildRequires:  freetype-devel
BuildRequires:  gcc-c++
BuildRequires:  glew-devel
BuildRequires:  glm-devel
BuildRequires:  libGL-devel
BuildRequires:  libGLU-devel
BuildRequires:  libX11-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  make
BuildRequires:  pcre2-devel
BuildRequires:  tinyxml-devel
# /oreon:deps
%description

OpenGL-based 3D visualization tool for source control repositories.
The repository is displayed as a tree where the root of the repository is
the centre, directories are branches and files are leaves. Contributors
to the source code appear and disappear as they contribute to specific
files and directories.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
#%%patch1 -p0
sed -i.cp -e 's|cp |cp -p |' Makefile.in
rm -r src/tinyxml

%build

%configure --enable-ttf-font-dir=%{_datadir}/fonts/gnu-free/ --with-tinyxml
make %{?_smp_mflags}
%install
make install DESTDIR=%{buildroot}
rm -rf %{buildroot}/%{_datadir}/%{name}/fonts
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
