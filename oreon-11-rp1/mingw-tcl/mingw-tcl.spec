%global source0_hash 5d265f3499b588681825d8093177830707b7035ad866b17189a3a6ab6dade0ff
%{?mingw_package_header}
%global majorver 9
%global minorver 0
%global fullver %{majorver}.%{minorver}
Name:          mingw-tcl
Version:       9.0.4
Release:        1%{?dist}
Summary:        MinGW Windows Tool Command Language, pronounced tickle
License:       TCL
URL:           http://tcl.sourceforge.net/
Source0:        https://downloads.sourceforge.net/sourceforge/tcl/tcl-core%{version}-src.tar.gz
BuildArch:     noarch
Patch1:        tcl-mingw.patch
Patch2:        tcl-nativetclsh.patch
Patch3:        tcl-configure.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  m4
BuildRequires:  make
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-zlib
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-zlib
BuildRequires:  tcl
# /oreon:deps
%description
The Tcl (Tool Command Language) provides a powerful platform for
creating integration applications that tie together diverse
applications, protocols, devices, and frameworks. When paired with the
Tk toolkit, Tcl provides a fastest and powerful way to create
cross-platform GUI applications.  Tcl can also be used for a variety
of web-related tasks and for creating powerful command languages for
applications.

%package -n mingw32-tcl
Summary: MinGW Windows Tool Command Language, pronounced tickle
%description -n mingw32-tcl
The Tcl (Tool Command Language) provides a powerful platform for
creating integration applications that tie together diverse
applications, protocols, devices, and frameworks. When paired with the
Tk toolkit, Tcl provides a fastest and powerful way to create
cross-platform GUI applications.  Tcl can also be used for a variety
of web-related tasks and for creating powerful command languages for
applications.

%package -n mingw64-tcl
Summary: MinGW Windows Tool Command Language, pronounced tickle
%description -n mingw64-tcl
The Tcl (Tool Command Language) provides a powerful platform for
creating integration applications that tie together diverse
applications, protocols, devices, and frameworks. When paired with the
Tk toolkit, Tcl provides a fastest and powerful way to create
cross-platform GUI applications.  Tcl can also be used for a variety
of web-related tasks and for creating powerful command languages for
applications.

%{?mingw_debug_package}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n tcl%{version}
# Delete precompiled binaries to be sure
rm -rf libtommath/win32
rm -rf libtommath/win64
rm -rf libtommath/win64-arm

%build

pushd win
autoconf
%mingw_configure --disable-threads --enable-shared
%mingw32_make -C build_win32 TCL_LIBRARY=%{mingw32_datadir}/tcl%{fullver}
%mingw64_make -C build_win64 TCL_LIBRARY=%{mingw64_datadir}/tcl%{fullver}
popd
%install
pushd win
%mingw32_make -C build_win32 install INSTALL_ROOT=%{buildroot} TCL_LIBRARY=%{mingw32_datadir}/tcl%{fullver}
%mingw64_make -C build_win64 install INSTALL_ROOT=%{buildroot} TCL_LIBRARY=%{mingw64_datadir}/tcl%{fullver}
%mingw32_make -C build_win32 install-libraries INSTALL_ROOT=%{buildroot} TCL_LIBRARY=%{mingw32_datadir}/tcl%{fullver}
%mingw64_make -C build_win64 install-libraries INSTALL_ROOT=%{buildroot} TCL_LIBRARY=%{mingw64_datadir}/tcl%{fullver}
popd
mv %{buildroot}%{mingw32_bindir}/tclsh%{majorver}.%{minorver} %{buildroot}%{mingw32_bindir}/tclsh%{majorver}%{minorver}.exe
mv %{buildroot}%{mingw64_bindir}/tclsh%{majorver}.%{minorver} %{buildroot}%{mingw64_bindir}/tclsh%{majorver}%{minorver}.exe
ln -s tclsh%{majorver}%{minorver}.exe %{buildroot}%{mingw32_bindir}/tclsh.exe
ln -s tclsh%{majorver}%{minorver}.exe %{buildroot}%{mingw64_bindir}/tclsh.exe
ln -s libtcl%{majorver}%{minorver}.dll.a %{buildroot}%{mingw32_libdir}/libtcl.dll.a
ln -s libtcl%{majorver}%{minorver}.dll.a %{buildroot}%{mingw64_libdir}/libtcl.dll.a
mkdir -p %{buildroot}%{mingw32_libdir}/tcl%{fullver}
mkdir -p %{buildroot}%{mingw64_libdir}/tcl%{fullver}
ln -s ../tclConfig.sh %{buildroot}%{mingw32_libdir}/tcl%{fullver}/tclConfig.sh
ln -s ../tclConfig.sh %{buildroot}%{mingw64_libdir}/tcl%{fullver}/tclConfig.sh
mkdir -p %{buildroot}%{mingw32_includedir}/tcl-private/{generic,win}
mkdir -p %{buildroot}%{mingw64_includedir}/tcl-private/{generic,win}
find generic win -maxdepth 1 -name "*.h" -exec cp -p '{}' %{buildroot}%{mingw32_includedir}/tcl-private/'{}' ';'
find generic win -maxdepth 1 -name "*.h" -exec cp -p '{}' %{buildroot}%{mingw64_includedir}/tcl-private/'{}' ';'
cp -p win/build_win32/tclUuid.h %{buildroot}%{mingw32_includedir}/tcl-private/win/tclUuid.h
cp -p win/build_win64/tclUuid.h %{buildroot}%{mingw64_includedir}/tcl-private/win/tclUuid.h
(
cd %{buildroot}%{mingw32_includedir}
for i in *.h ; do
    [ -f %{buildroot}%{mingw32_includedir}/tcl-private/generic/$i ] && ln -sf ../../$i %{buildroot}%{mingw32_includedir}/tcl-private/generic || :;
done
)
(
cd %{buildroot}%{mingw64_includedir}
for i in *.h ; do
    [ -f %{buildroot}%{mingw64_includedir}/tcl-private/generic/$i ] && ln -sf ../../$i %{buildroot}%{mingw64_includedir}/tcl-private/generic || : ;
done
)
mv %{buildroot}%{mingw32_libdir}/dde* %{buildroot}%{mingw32_libdir}/tcl%{fullver}/
mv %{buildroot}%{mingw64_libdir}/dde* %{buildroot}%{mingw64_libdir}/tcl%{fullver}/
mv %{buildroot}%{mingw32_libdir}/reg* %{buildroot}%{mingw32_libdir}/tcl%{fullver}/
mv %{buildroot}%{mingw64_libdir}/reg* %{buildroot}%{mingw64_libdir}/tcl%{fullver}/
rm -rf %{buildroot}%{mingw32_mandir}/man1/ %{buildroot}%{mingw32_mandir}/man3/ %{buildroot}%{mingw32_mandir}/mann/
rm -rf %{buildroot}%{mingw64_mandir}/man1/ %{buildroot}%{mingw64_mandir}/man3/ %{buildroot}%{mingw64_mandir}/mann/
%oreon_autofiles mingw32-tcl usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-tcl usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-tcl -f %{oreon_filedir}/mingw32-tcl.list
%files -n mingw64-tcl -f %{oreon_filedir}/mingw64-tcl.list

%changelog

%autochangelog
