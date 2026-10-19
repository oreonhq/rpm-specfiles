%global source0_hash 7af0999eeee38176ea34f9f96b358e43e343c73edf6f56143f18794303ca8702
%define libver    4
Name:             klatexformula
Version:          4.1.0
Release:        15%{?dist}
Summary:        Application for easy image creating from a LaTeX equation
License:          GPL-2.0-or-later
URL:              http://klatexformula.sourceforge.net/
Source0:        http://downloads.sourceforge.net/klatexformula/%{name}-%{version}.tar.gz
Patch0:           painter_path.patch
Requires:         texlive-latex
Requires:         hicolor-icon-theme
Recommends:       texlive-dvisvgm
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  help2man
BuildRequires:  kf5-plasma-devel
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-qttools-static
BuildRequires:  qt5-qtx11extras-devel
# /oreon:deps
%description
This application provides a GUI for writing and generating an image
(e.g. PNG, JPG, BMP, etc.) from a LaTeX equation. The images can be dragged
and dropped or copied and pasted into other applications, or can be saved
to disk.

A command-line mode is available (e.g. for scripts) using the klatexformula_cmdl
executable.

%package -n libklatexformula
Summary:          Backend and tools libraries provided by KLatexFormula
Obsoletes:        libklfbackend < 4.0.0
Provides:         libklfbackend = %{version}
%description -n libklatexformula
C++/QT libraries containing functionality from klatexformula, including the klfbackend
library for integrating klatexformula functionality into other programs, and general
purpose tools that were written for klatexformula but have now been made into a library
for use in any application.

%package -n libklatexformula-devel
Summary:          Development files for libklatexformula
Requires:         qt5-qtbase-devel
Requires:         libklatexformula%{?_isa} = %{version}-%{release}
Obsoletes:        %{name}-devel < 4.0.0
Provides:         %{name}-devel = %{version}
Obsoletes:        libklfbackend-devel < 4.0.0
Provides:         libklfbackend-devel = %{version}
%description -n libklatexformula-devel
Development files for libklatexformula.

%package -n libklatexformula-static
Summary:          Static library for libklatexformula
Requires:         qt5-qtbase-devel
Requires:         libklatexformula-devel%{?_isa} = %{version}-%{release}
%description -n libklatexformula-static
Static library for the klfbackend library provided by libklatexformula.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%{cmake_kf5} \
        -DCMAKE_SKIP_RPATH=ON \
        -DKLF_LIBKLFAPP_STATIC=OFF \
        -DKLF_LIBKLFBACKEND_STATIC=OFF \
        -DKLF_LIBKLFTOOLS_STATIC=OFF \
        -DKLF_INSTALL_POST_UPDATEMIMEDATABASE=OFF \
        -DKLF_INSTALL_SHARE_PIXMAPS_DIR="" \
        -DKLF_NO_CMU_FONT=ON \
        -DKLF_INSTALL_LIB_DIR=%{_libdir} \
        -DKLF_INSTALL_KLFTOOLSDESPLUGIN=YES \
        -DKLF_INSTALL_ICON_THEME=%{_datadir}/icons/hicolor/ \
        -DKLF_INSTALL_DESKTOP_CATEGORIES="Qt;Office;" \
        -DKLF_INSTALL_DESKTOP_ICON="%{name}" \
        -DKLF_INSTALL_DESPLUGIN_DIR=%{_qt5_plugindir}/designer/ \
        %{nil}
%cmake_build
%install
%cmake_install
%py_byte_compile %{__python3} %{buildroot}%{_datadir}/%{name}/userscripts/pyklfuserscript
%oreon_autofiles libklatexformula usr/*/lib*.so.*
%oreon_autofiles libklatexformula-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles libklatexformula-static usr/*/lib*.so.*
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
%files -f %{oreon_filedir}/main.list
%files -n libklatexformula -f %{oreon_filedir}/libklatexformula.list
%files -n libklatexformula-devel -f %{oreon_filedir}/libklatexformula-devel.list
%files -n libklatexformula-static -f %{oreon_filedir}/libklatexformula-static.list

%changelog

%autochangelog
