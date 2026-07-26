%global source0_hash 332d89b9a979b17417fbce0edd72b19914f1409fd126a13d11787d0e15dc0d79

Summary: Software version control visualization
Name: gource
Version: 0.56
Release: 1%{?dist}
URL: http://gource.io/
Source: https://github.com/acaudwell/Gource/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz
ExcludeArch: ppc64le

License: GPL-3.0-or-later

BuildRequires: gcc-c++
BuildRequires: SDL2_image-devel
BuildRequires: SDL2-devel
BuildRequires: libpng-devel
BuildRequires: libjpeg-devel
BuildRequires: pcre2-devel
BuildRequires: libX11-devel
BuildRequires: libGL-devel
BuildRequires: libGLU-devel
BuildRequires: glew-devel
BuildRequires: freetype-devel
BuildRequires: glm-devel
BuildRequires: boost-devel
BuildRequires: tinyxml-devel
BuildRequires: make

Requires: gnu-free-sans-fonts

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

%files
%{_bindir}/gource
%{_mandir}/man1/gource.1.gz
%license COPYING
%doc README.md THANKS ChangeLog

%dir %{_datadir}/gource
%{_datadir}/gource/*

%changelog
%autochangelog
