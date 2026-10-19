%global source0_hash fd453554fcbc450bc9d2ddf28aafa480f1a6ccb00ee361a5597e8d407b4833ec
%global commit 4636eecc323b39e4b98e6d1d12ff281f7dd2752e
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global dxfrw_includedir %(%___build_pre; pkg-config --cflags-only-I libdxfrw | sed 's|-I||g')
Name:			librecad
Version:		2.2.1.5
Release:        1%{?dist}
Summary:        Computer Assisted Design (CAD) Application
License:		GPL-2.0-only AND GPL-2.0-or-later
URL:			http://librecad.org/
Source0:        https://github.com/LibreCAD/LibreCAD/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Source1:		ttf2lff.1
Source2:		Architect8-LCAD.zip
Source3:		Electronic8-LCAD.zip
Patch0:			librecad-use-system-libdxfrw.patch
Patch2:			librecad-install.patch
Patch3:			librecad-plugindir.patch
Patch6:			librecad-gcc6.patch
Patch8:			librecad-unique-symbol-names.patch
Requires:		%{name}-fonts = %{version}-%{release}
Requires:		%{name}-langs = %{version}-%{release}
Requires:		%{name}-parts = %{version}-%{release}
Requires:		%{name}-patterns = %{version}-%{release}
Requires:		libdxfrw >= 1.1.0-0.11.rc1
%global __provides_exclude_from ^(%{_libdir}/%{name}/plugins/.*\\.so)$
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  desktop-file-utils
BuildRequires:  freetype-devel
BuildRequires:  gcc-c++
BuildRequires:  libdxfrw-devel
BuildRequires:  make
BuildRequires:  muParser-devel
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  shapelib-devel
BuildRequires:  wqy-microhei-fonts
# /oreon:deps
%description
A graphical and comprehensive 2D CAD application.

%package devel
Summary:	Development files for LibreCAD
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description devel
Development files for LibreCAD.

%package fonts
Summary:	Fonts in LibreCAD (lff) format
License:	GPL-2.0-or-later AND LicenseRef-Fedora-UltraPermissive AND OFL-1.1 AND LicenseRef-Fedora-Public-Domain AND (LicenseRef-Fedora-UltraPermissive AND GPL-2.0-or-later) AND (Apache-2.0 OR GPL-3.0-only WITH Font-exception-2.0)
BuildArch:	noarch
%description fonts
Fonts converted to LibreCAD (lff) format.

%package langs
Summary:	Language (qm) files for LibreCAD
BuildArch:	noarch
%description langs
Language (qm) files for	LibreCAD.

%package parts
Summary:	Parts collection for LibreCAD
BuildArch:	noarch
%description parts
Collection of parts for LibreCAD.

%package patterns
Summary:	Pattern files for LibreCAD
BuildArch:	noarch
%description patterns
Pattern files for LibreCAD.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn LibreCAD-%{commit} -a 2 -a 3
%patch -P0 -p1 -b .system
# %%patch2 -p1 -b .install
%patch -P3 -p1
# %%patch4 -p1 -b .system-shapelib
%patch -P6 -p1 -b .gcc6
# %%patch8 -p1 -b .unique
sed -i 's|##LIBDIR##|%{_libdir}|g' librecad/src/lib/engine/rs_system.cpp
sed -i 's|$${DXFRW_INCLUDEDIR}|%{dxfrw_includedir}|g' librecad/src/src.pro

## Fix plugin search path
#sed -i 's|"/../share/"|"/../%{_lib}/"|'  librecad/src/lib/engine/rs_system.cpp

# Nuke bundled libraries
# rm -rf libraries/libdxfrw
# rm -rf plugins/importshp/shapelib

# unset +x flags on some source files
for i in plugins/*/*.cpp plugins/*/*.h librecad/src/plugins/qc_plugininterface.h; do
  chmod -x $i
done

# copy font licenses here
%if 0%{?epel} == 7
cp /usr/share/doc/wqy-microhei-fonts*/LICENSE_* .
%else
cp /usr/share/licenses/wqy-microhei-fonts/LICENSE_* .
%endif

sed -i 's|LRELEASE="lrelease"|LRELEASE="lrelease-qt5"|g' scripts/postprocess-unix.sh

# Fix the version string
sed -i 's|LC_VERSION="2.2.0-undef"|LC_VERSION="%{version}"|g' librecad/src/src.pro

%build

%{qmake_qt5} librecad.pro 'CONFIG+=release' 'BOOST_DIR=%{_prefix}' 'BOOST_LIBDIR=%{_libdir}' 'MUPARSER_DIR=%{_prefix}' 'QMAKE_LFLAGS_RELEASE=' 'DISABLE_POSTSCRIPT=true'
make %{?_smp_mflags} MUPARSER_DIR=%{_prefix}
rm -rf unix/resources/fonts/wqy-unicode.lff
mkdir -p unix/resources/fonts
./unix/ttf2lff -L "Apache-2.0 OR GPL-3.0-only WITH Font-exception-2.0" /usr/share/fonts/wqy-microhei-fonts/wqy-microhei.ttc unix/resources/fonts/wqy-unicode.lff
%install
export BUILDDIR="%{buildroot}%{_datadir}/%{name}"
sh scripts/postprocess-unix.sh
mkdir -p %{buildroot}%{_libdir}/%{name}/plugins
mv unix/resources/plugins/* %{buildroot}%{_libdir}/%{name}/plugins/
%{__install} -Dpm 755 -s unix/%{name} %{buildroot}%{_bindir}/%{name}
%{__install} -Dpm 755 -s unix/ttf2lff %{buildroot}%{_bindir}/ttf2lff
%{__install} -Dpm 644 desktop/%{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
%{__install} -Dpm 644 librecad/res/main/%{name}.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
%{__install} -Dpm 644 desktop/%{name}.sharedmimeinfo %{buildroot}%{_datadir}/mime/packages/%{name}.xml
%{__install} -Dpm 644 desktop/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
%{__install} -Dpm 644 %{SOURCE1} %{buildroot}%{_mandir}/man1/ttf2lff.1
%{__install} -Dpm 644 librecad/src/plugins/document_interface.h %{buildroot}%{_includedir}/%{name}/document_interface.h
%{__install} -Dpm 644 librecad/src/plugins/qc_plugininterface.h %{buildroot}%{_includedir}/%{name}/qc_plugininterface.h
mkdir -p %{buildroot}%{_datadir}/%{name}/fonts
cp -a unix/resources/fonts/*.lff %{buildroot}%{_datadir}/%{name}/fonts/
mkdir -p %{buildroot}%{_datadir}/%{name}/qm
cp -a unix/resources/qm/* %{buildroot}%{_datadir}/%{name}/qm/
mkdir -p %{buildroot}%{_datadir}/%{name}/library
cp -a unix/resources/library/* %{buildroot}%{_datadir}/%{name}/library/
mkdir -p %{buildroot}%{_datadir}/%{name}/patterns
cp -a unix/resources/patterns/* %{buildroot}%{_datadir}/%{name}/patterns/
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Ryan Lerch <rlerch@redhat.com> -->
<!--
BugReportURL: https://sourceforge.net/p/librecad/feature-requests/158/
SentUpstream: 2014-09-18
-->
<application>
  <id type="desktop">librecad.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>2D Computer Aided Design (CAD)</summary>
  <description>
    <p>
      LibreCAD is an 2D Computer Aided Design (CAD) application for creating plans
      and designs on your computer.
      It can be used to make  accurate 2D representations of floorplans, part designs,
      and just about anything that can be represented as a flat 2D plan.
    </p>
  </description>
  <url type="homepage">http://librecad.org/</url>
  <screenshots>
    <screenshot type="default">http://wiki.librecad.org/images/f/f8/Lcnotclosed.png</screenshot>
  </screenshots>
</application>
EOF
mkdir -p %{buildroot}%{_datadir}/%{name}/library/architecture
cp -a Architect8-LCAD %{buildroot}%{_datadir}/%{name}/library/architecture
mkdir -p %{buildroot}%{_datadir}/%{name}/library/electronics
cp -a Electronic8-LCAD %{buildroot}%{_datadir}/%{name}/library/electronics
%{_fixperms} %{buildroot}
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/*/lib*.so.* usr/*/lib*.so.* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n librecad-devel -f %{oreon_filedir}/librecad-devel.list
%files -n librecad-fonts -f %{oreon_filedir}/librecad-fonts.list
%files -n librecad-langs -f %{oreon_filedir}/librecad-langs.list
%files -n librecad-parts -f %{oreon_filedir}/librecad-parts.list
%files -n librecad-patterns -f %{oreon_filedir}/librecad-patterns.list

%changelog

%autochangelog
