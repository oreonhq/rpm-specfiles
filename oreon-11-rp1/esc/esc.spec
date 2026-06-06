%global source0_hash 950ddb58b92a1f295cf96cef86c3f35bf453cd695f533657367ef2312bf7c085

Name: esc 
Version: 1.1.2
Release: 23%{?dist}
Summary: Enterprise Security Client Smart Card Client
License: GPL-1.0-or-later
URL: http://directory.fedora.redhat.com/wiki/CoolKey 

#BuildRequires: doxygen fontconfig-devel
BuildRequires: glib2-devel atk-devel
BuildRequires: pkgconfig
BuildRequires: nspr-devel nss-devel nss-static
#BuildRequires: libX11-devel libXt-devel

BuildRequires: pcsc-lite-devel
BuildRequires: desktop-file-utils
%if ! 0%{?rhel} >= 9 || (0%{?oreon} >= 11)
BuildRequires: pkgconfig(gconf-2.0)
%endif
BuildRequires: dbus-devel
BuildRequires: glib2-devel
BuildRequires: opensc
BuildRequires: gobject-introspection-devel
BuildRequires: gtk3-devel
BuildRequires: gjs-devel
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: chrpath
BuildRequires: cpio
BuildRequires: rpm


Requires: pcsc-lite nss nspr
Requires: dbus
Requires: opensc
Requires: gjs
Requires: gobject-introspection
Requires: gtk3
Requires: glib2

# multiple libraries in package-specific directory, linked against each other
AutoReqProv: 0

%define debug_build       0

%define escname %{name}-%{version}
%define escdir %{_libdir}/%{escname}
%define esc_chromepath   chrome/content/esc
%define esc_vendor esc 
%define icondir %{_datadir}/icons/hicolor/48x48/apps
%define pixmapdir  %{_datadir}/pixmaps
%define docdir    %{_defaultdocdir}/%{escname}

Source0:        https://download.rockylinux.org/pub/rocky/9/AppStream/source/tree/Packages/e/esc-1.1.2-16.el9.src.rpm
Source1:        esc
Source2:        esc.desktop
Patch0:        esc-gcc11.patch
Patch1:        esc-1.1.2-fix1.patch
Patch2:        esc-1.1.2-fix2.patch
Patch3:        esc-1.1.2-fix3.patch
Patch4:        esc-1.1.2-fix4.patch
Patch5:        esc-1.1.2-fix5.patch
Patch6:        esc-1.1.2-fix6.patch
Patch7:        esc-1.1.2-fix7.patch
Patch8:        esc-1.1.2-fix8.patch
Patch9:        esc-1.1.2-fix9.patch
Patch10:        esc-1.1.2-fix10.patch
Patch11:        esc-1.1.2-fix11.patch
Patch12:        esc-1.1.2-fix12.patch
Patch13:        esc-1.1.2-fix13.patch


%description
Enterprise Security Client allows the user to enroll and manage their
cryptographic smartcards.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
cd %{_sourcedir}
rpm2cpio %{SOURCE0} | cpio -id esc-1.1.2.tar.bz2 esc.png
cd %{builddir}
tar -xjf %{_sourcedir}/esc-1.1.2.tar.bz2
cd %{escname}
%autopatch -p1


%build
echo $RPM_BUILD_DIR

echo "build section" $PWD
cd esc 

autoreconf --force --install --verbose
%configure --bindir %{escdir} --libdir %{escdir}/lib --datadir %{_datadir}
%make_build -j1


%install
echo "install section" $PWD
cd esc
%make_install

mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{icondir}
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{pixmapdir}
mkdir -p %{buildroot}%{docdir}

echo "dir: "  %{buildroot}%{_bindir}/%{name}
sed -e 's;\$LIBDIR;'%{_libdir}';g'  %{SOURCE1} > %{buildroot}%{_bindir}/%{name}
chmod 755 %{buildroot}%{_bindir}/%{name}
chmod -x %{buildroot}%{escdir}/*.{conf,js,properties}

rm %{buildroot}%{escdir}/lib/*.a
rm %{buildroot}%{escdir}/lib/*.la
rm -r %{buildroot}%{_includedir}/coolkey-mgr/
rm -r %{buildroot}%{_datadir}/gir-*/

cp %{_sourcedir}/esc.png %{buildroot}%{icondir}
cp %{_sourcedir}/esc.png %{buildroot}%{pixmapdir}/esc.png

desktop-file-install --dir %{buildroot}%{_datadir}/applications %{SOURCE2}

#Get rid of rpath
chrpath --delete %{buildroot}%{escdir}/lib/libcoolkeymgr-1.0.so


%files
%license esc/LICENSE

%{_bindir}/esc
%dir %{escdir}
%{escdir}/lib
%{escdir}/*.js
%{escdir}/esc.properties
%{escdir}/opensc.esc.conf
%{_datadir}/applications/esc.desktop
%{icondir}/esc.png
%{pixmapdir}/esc.png

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1.2-23
- Import
