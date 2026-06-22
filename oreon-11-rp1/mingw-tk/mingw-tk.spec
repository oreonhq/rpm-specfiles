%global source0_hash bf344efadb618babb7933f69275620f72454d1c8220130da93e3f7feb0efbf9b

%{?mingw_package_header}

%global majorver 9
%global minorver 0
%global fullver %{majorver}.%{minorver}

Name:          mingw-tk
Version:       9.0.3
Release:       1%{?dist}
Summary:       MinGW Windows graphical toolkit for the Tcl scripting language

License:       TCL
URL:           http://tcl.sourceforge.net/
Source0:       https://downloads.sourceforge.net/sourceforge/tcl/tk%{version}-src.tar.gz
BuildArch:     noarch

BuildRequires: make

BuildRequires: mingw32-tcl = %{version}
BuildRequires: mingw32-filesystem
BuildRequires: mingw32-gcc

BuildRequires: mingw64-tcl = %{version}
BuildRequires: mingw64-filesystem
BuildRequires: mingw64-gcc


%description
When paired with the Tcl scripting language, Tk provides a fast and powerful
way to create cross-platform GUI applications.


%package -n mingw32-tk
Summary:   MinGW Windows graphical toolkit for the Tcl scripting language

%description -n mingw32-tk
When paired with the Tcl scripting language, Tk provides a fast and powerful
way to create cross-platform GUI applications.


%package -n mingw64-tk
Summary:   MinGW Windows graphical toolkit for the Tcl scripting language

%description -n mingw64-tk
When paired with the Tcl scripting language, Tk provides a fast and powerful
way to create cross-platform GUI applications.


%{?mingw_debug_package}


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n tk%{version}


%build
pushd win

MINGW32_CONFIGURE_ARGS="--with-tcl=%{mingw32_libdir}"
MINGW64_CONFIGURE_ARGS="--with-tcl=%{mingw64_libdir}"
%{mingw_configure}
%{mingw32_make} -C build_win32 TCL_LIBRARY=%{mingw32_datadir}/tk%{fullver}
%{mingw64_make} -C build_win64 TCL_LIBRARY=%{mingw64_datadir}/tk%{fullver}
popd


%install
make install -C win/build_win32 INSTALL_ROOT=%{buildroot} TK_LIBRARY=%{mingw32_datadir}/tk%{fullver}
make install -C win/build_win64 INSTALL_ROOT=%{buildroot} TK_LIBRARY=%{mingw64_datadir}/tk%{fullver}

ln -s wish%{majorver}%{minorver}.exe %{buildroot}%{mingw32_bindir}/wish.exe
ln -s wish%{majorver}%{minorver}.exe %{buildroot}%{mingw64_bindir}/wish.exe

# for linking with -libtk
ln -s libtcl9tk%{majorver}%{minorver}.dll.a %{buildroot}%{mingw32_libdir}/libtk.dll.a
ln -s libtcl9tk%{majorver}%{minorver}.dll.a %{buildroot}%{mingw64_libdir}/libtk.dll.a

mkdir -p %{buildroot}/%{mingw32_libdir}/tk%{fullver}
mkdir -p %{buildroot}/%{mingw64_libdir}/tk%{fullver}

# postgresql and maybe other packages too need tclConfig.sh
# paths don't look at /usr/lib for efficiency, so we symlink into tcl8.5 for now
ln -s ../tkConfig.sh \
      %{buildroot}/%{mingw32_libdir}/tk%{fullver}/tkConfig.sh
ln -s ../tkConfig.sh \
      %{buildroot}/%{mingw64_libdir}/tk%{fullver}/tkConfig.sh

mkdir -p %{buildroot}/%{mingw32_includedir}/tk-private/{generic/ttk,win}
mkdir -p %{buildroot}/%{mingw64_includedir}/tk-private/{generic/ttk,win}
find generic win -name "*.h" -exec cp -p '{}' %{buildroot}/%{mingw32_includedir}/tk-private/'{}' ';'
find generic win -name "*.h" -exec cp -p '{}' %{buildroot}/%{mingw64_includedir}/tk-private/'{}' ';'
(
cd %{buildroot}/%{mingw32_includedir}
for i in *.h ; do
      [ -f %{buildroot}/%{mingw32_includedir}/tk-private/generic/$i ] && \
      ln -sf ../../$i %{buildroot}/%{mingw32_includedir}/tk-private/generic || : ;
done
)
(
cd %{buildroot}/%{mingw64_includedir}
for i in *.h ; do
      [ -f %{buildroot}/%{mingw64_includedir}/tk-private/generic/$i ] && \
      ln -sf ../../$i %{buildroot}/%{mingw64_includedir}/tk-private/generic || : ;
done
)

# Delete man files
rm -rf %{buildroot}%{mingw32_mandir}/man1/ %{buildroot}%{mingw32_mandir}/man3/ %{buildroot}%{mingw32_mandir}/mann/
rm -rf %{buildroot}%{mingw64_mandir}/man1/ %{buildroot}%{mingw64_mandir}/man3/ %{buildroot}%{mingw64_mandir}/mann/


%files -n mingw32-tk
%{mingw32_bindir}/wish.exe
%{mingw32_bindir}/wish%{majorver}%{minorver}.exe
%{mingw32_bindir}/tcl9tk%{majorver}%{minorver}.dll
%{mingw32_libdir}/libtcl9tk%{majorver}%{minorver}.dll.a
%{mingw32_libdir}/libtkstub.a
%{mingw32_libdir}/libtk.dll.a
%{mingw32_libdir}/tkConfig.sh
%{mingw32_libdir}/pkgconfig/tk.pc
%{mingw32_includedir}/*
%{mingw32_libdir}/tk%{fullver}/
%{mingw32_datadir}/tk%{majorver}.%{minorver}
%license license.terms

%files -n mingw64-tk
%{mingw64_bindir}/wish.exe
%{mingw64_bindir}/wish%{majorver}%{minorver}.exe
%{mingw64_bindir}/tcl9tk%{majorver}%{minorver}.dll
%{mingw64_libdir}/libtcl9tk%{majorver}%{minorver}.dll.a
%{mingw64_libdir}/libtkstub.a
%{mingw64_libdir}/libtk.dll.a
%{mingw64_libdir}/tkConfig.sh
%{mingw64_libdir}/pkgconfig/tk.pc
%{mingw64_includedir}/*
%{mingw64_libdir}/tk%{fullver}/
%{mingw64_datadir}/tk%{majorver}.%{minorver}
%license license.terms

%changelog
%autochangelog
