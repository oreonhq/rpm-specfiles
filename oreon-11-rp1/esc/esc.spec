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
%if ! 0%{?rhel} >= 9
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

Source0: https://www.dogtagpki.org/pki/sources/esc/%{escname}.tar.bz2 
Source1: https://www.dogtagpki.org/pki/sources/esc/esc
# originally https://www.dogtagpki.org/pki/sources/esc/esc.desktop, since modified
Source2: esc.desktop
Source3: https://www.dogtagpki.org/pki/sources/esc/esc.png
Patch0: esc-gcc11.patch
Patch1: esc-1.1.2-fix1.patch
Patch2: esc-1.1.2-fix2.patch
Patch3: esc-1.1.2-fix3.patch
Patch4: esc-1.1.2-fix4.patch
Patch5: esc-1.1.2-fix5.patch
Patch6: esc-1.1.2-fix6.patch
Patch7: esc-1.1.2-fix7.patch
Patch8: esc-1.1.2-fix8.patch
Patch9: esc-1.1.2-fix9.patch
Patch10: esc-1.1.2-fix10.patch
Patch11: esc-1.1.2-fix11.patch
Patch12: esc-1.1.2-fix12.patch
Patch13: esc-1.1.2-fix13.patch


%description
Enterprise Security Client allows the user to enroll and manage their
cryptographic smartcards.

%prep
%autosetup -c -p1 -n %{escname}


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

cp %{SOURCE3} %{buildroot}%{icondir}
cp %{SOURCE3} %{buildroot}%{pixmapdir}/esc.png

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
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1.2-23
- Prepare for Oreon 11 (RP1)
