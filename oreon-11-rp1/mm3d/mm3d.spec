%global source11_hash faddf838b192517e2e01ce92fe0e45eeab4f55b3278b15ffd1f169a95638d60c
%global source10_hash 56fdbbf05e2e1764f35f4dbdbcaa5f521c31263d6cbdaff8056394505f3577ee
%global source0_hash 695642a021b8fb529ac7442e26b342bd95a8b1f73e6221a2b114362f5a2a716e
%global         plugin_3ds_ver          0.8.1
%global         plugin_imtex_ver        1.4.0
%global         mm3d_plugins            ad3dsfilter imtex
%global         major_version           1.3
Name:           mm3d
Version:        1.3.15
Release:        1%{?dist}
Summary:        3D model editor
License:        GPL-2.0-or-later
URL:            https://clover.moe/mm3d
Source0:        https://github.com/zturtleman/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source10:       http://www.misfitcode.com/misfitmodel3d/download/plugins/ad3dsfilter-%{plugin_3ds_ver}.tar.gz
Source11:       http://www.misfitcode.com/misfitmodel3d/download/plugins/imtex-%{plugin_imtex_ver}.tar.gz
Patch0:         mm3d-1.3.11-sighandler.patch
Patch10:        mm3d-ad3dsfilter-make.patch
Patch11:        mm3d-imtex-make.patch
Patch12:        mm3d-imtex-gcc43.patch
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  dos2unix
BuildRequires:  imlib2-devel
BuildRequires:  lib3ds-devel
BuildRequires:  libGLU-devel
BuildRequires:  libXmu-devel
BuildRequires:  libtool
BuildRequires:  lua-devel
BuildRequires:  make
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtbase-devel
# /oreon:deps
%description
Maverick Model 3D is an OpenGL-based 3D model editor that works with
triangle-based models. It supports multi-level undo, skeletal animations,
simple texturing, scripting, command-line batch processing, and a plugin
system for adding new model and image filters. Complete online help
is included. It is designed to be easy to use and easy to extend
with plugins and scripts.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -a 10 -a 11

%patch -P 0 -p1 -b .sigh

%patch -P 10 -b .ad3ds
%patch -P 11 -b .imtex
%patch -P 12 -b .gcc43

autoreconf -vif

for i in AUTHORS COPYING ChangeLog INSTALL README TODO doc/html/TODO
do
    dos2unix -q --keepdate $i
done

# remove bundled lib3ds
rm -rf plugins/ad3ds/lib3ds

%build

export CPPFLAGS="-DSHARED_PLUGINS=\\\"%{_libdir}/%{name}\\\""
%configure --with-Qt-include-dir=%{_qt5_includedir} --with-Qt-bin-dir=%{_qt5_bindir} --with-lua-dir=%{_usr} --with-lualib-dir=%{_usr} --with-lualib-lib=lua
make %{?_smp_mflags} "CFLAGS=%build_cflags" "CXXFLAGS=%build_cxxflags" "LDFLAGS=%build_ldflags"
cd plugins
for d in %{mm3d_plugins}
do
    pushd $d
    make "CFLAGS=%build_cflags" "CXXFLAGS=%build_cxxflags" "LFLAGS=%build_ldflags"
    popd
done
%install
%make_install
mkdir -p %{buildroot}%{_libdir}/%{name}/%{major_version}
for d in %{mm3d_plugins}
do
    install -p -m 0755 plugins/$d/$d.so %{buildroot}%{_libdir}/%{name}/%{major_version}
done
rm -rf %{buildroot}%{_datadir}/%{name}/plugins
desktop-file-validate %{buildroot}%{_datadir}/applications/moe.clover.%{name}.desktop
cp -p AUTHORS COPYING ChangeLog README.md TODO %{buildroot}%{_datadir}/doc/%{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
