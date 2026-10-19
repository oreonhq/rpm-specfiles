%global source0_hash d7a146d2917eb8b5cc95276dbf0e3d03c7464d2b19c1675357857c989301dbb4
%{?mingw_package_header}
%global majorver 9
%global minorver 0
%global fullver %{majorver}.%{minorver}
Name:          mingw-tk
Version:       9.0.4
Release:        1%{?dist}
Summary:        MinGW Windows graphical toolkit for the Tcl scripting language
License:       TCL
URL:           http://tcl.sourceforge.net/
Source0:        https://downloads.sourceforge.net/sourceforge/tcl/tk%{version}-src.tar.gz
BuildArch:     noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-tcl
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-tcl
# /oreon:deps
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
%global oreon_srcdir tk%{version}
%oreon_prep
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
ln -s libtcl9tk%{majorver}%{minorver}.dll.a %{buildroot}%{mingw32_libdir}/libtk.dll.a
ln -s libtcl9tk%{majorver}%{minorver}.dll.a %{buildroot}%{mingw64_libdir}/libtk.dll.a
mkdir -p %{buildroot}/%{mingw32_libdir}/tk%{fullver}
mkdir -p %{buildroot}/%{mingw64_libdir}/tk%{fullver}
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
rm -rf %{buildroot}%{mingw32_mandir}/man1/ %{buildroot}%{mingw32_mandir}/man3/ %{buildroot}%{mingw32_mandir}/mann/
rm -rf %{buildroot}%{mingw64_mandir}/man1/ %{buildroot}%{mingw64_mandir}/man3/ %{buildroot}%{mingw64_mandir}/mann/
%oreon_autofiles mingw32-tk usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-tk usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-tk -f %{oreon_filedir}/mingw32-tk.list
%files -n mingw64-tk -f %{oreon_filedir}/mingw64-tk.list

%changelog

%autochangelog
