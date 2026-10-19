%global source2_hash b659eb71eb06a45b6047b4e7678d38a5643fe1282fe8a9bee5a4ba31c582bf04
%global source0_hash e1f2ae665e49631c30f483e9048d4f6c7fc6f4854d945fbe3c68995c6bf5ec65
%global debug_package %{nil}
%bcond_without  gui
%global qt_ver 6
%global qmake %{_qt6_qmake}
Name:           ansifilter
Version:        2.24
Release:        1%{?dist}
Summary:        ANSI terminal escape code converter
License:        GPL-3.0-or-later
URL:            http://www.andre-simon.de/doku/ansifilter/ansifilter.php
Source0:        http://www.andre-simon.de/zip/%{name}-%{version}.tar.bz2
%if %{with gui}
Source1:        ansifilter.desktop
Source2:        http://www.andre-simon.de/img/af_icon.png
%endif
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  qt6-qtbase-devel
# /oreon:deps
%description
Ansifilter handles text files containing ANSI terminal escape codes. The
command sequences may be stripped or be interpreted to generate formatted
output (HTML, RTF, TeX, LaTeX, BBCode).

%if %{with gui}
%package        gui
Summary:        GUI for %{name} based on Qt5
BuildRequires:  desktop-file-utils
BuildRequires:  qt%{qt_ver}-qtbase-devel
BuildRequires: make
%description    gui
Ansifilter handles text files containing ANSI terminal escape codes. The
command sequences may be stripped or be interpreted to generate formatted
output (HTML, RTF, TeX, LaTeX, BBCode).

This is a GUI of %{name} based on Qt%{qt_ver}.
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

# Preserve timestamps.
sed -i 's|install -m|install -pm|g' makefile

%if %{with gui}
# Remove pre-configured files which may cause errors during building.
rm -frv src/qt-gui/moc_*.cpp
rm -frv src/qt-gui/Makefile*
%endif

# CRLF quickfix
find . -type f -exec sed -i 's/\r$//' {} + -print

%build

%make_build CFLAGS+="%{optflags} -c" LDFLAGS="%{?__global_ldflags}"
%if %{with gui}
%make_build all-gui QMAKE="%{qmake}"
%endif
%install
%make_install
%if %{with gui}
make install-gui DESTDIR=%{buildroot}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{S:1}
install -pDm644 %{S:2} %{buildroot}%{_datadir}/pixmaps/%{name}.png
%endif
rm -frv %{buildroot}%{_docdir}
%oreon_autofiles ansifilter-gui usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ansifilter-gui -f %{oreon_filedir}/ansifilter-gui.list

%changelog

%autochangelog
