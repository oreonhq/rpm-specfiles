%global source0_hash 36dfdc79c750930dd57e2c4a4dee2a6ab1a1fe65cd8fc4dc047dbfb6f2cfa15b
Name:           pstoedit
Version:        4.3
Release:        1%{?dist}
Summary:        Translates PostScript and PDF graphics into other vector formats
License:        GPL-2.0-or-later
URL:            http://www.pstoedit.net
Source0:        https://github.com/woglu/pstoedit/archive/refs/tags/v%{version}.tar.gz#/pstoedit-%{version}.tar.gz
Patch0:         %{name}-pkglibdir.patch
Patch1:         %{name}-fix-gcc12.patch
Patch2:         %{name}-force_CXXFLAGS.patch
Requires:       ghostscript%{?_isa}
# oreon:deps
BuildRequires:  ImageMagick-c++-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  chrpath
BuildRequires:  desktop-file-utils
BuildRequires:  dos2unix
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gd-devel
BuildRequires:  ghostscript
BuildRequires:  libEMF-devel
BuildRequires:  libtool
BuildRequires:  libzip-devel
BuildRequires:  make
BuildRequires:  plotutils-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  texlive-babel
BuildRequires:  texlive-babel-english
BuildRequires:  texlive-fancyhdr
BuildRequires:  texlive-latex
BuildRequires:  texlive-latex-base-dev
BuildRequires:  texlive-scheme-basic
BuildRequires:  texlive-texlive-scripts
# /oreon:deps
%description
Pstoedit converts PostScript and PDF files to various vector graphic
formats. The resulting files can be edited or imported into various
drawing packages. Pstoedit comes with a large set of integrated format
drivers.

%package gui
Summary:        Qt GUI of %{name}
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  desktop-file-utils
Requires:       %{name}%{?_isa} = 0:%{version}-%{release}
%description gui
PstoeditQtGui provides an alternative to the command driven operation. The
GUI provides access to almost all options and features that are supported by
pstoedit. In addition it supports the conversion of multiple files in one job
and also provides some shortcuts to some of Ghostscript’s high level
output devices.

%package devel
Summary:        Files for developing programs that will use %{name}
Requires:       %{name}%{?_isa} = 0:%{version}-%{release}
%description devel
This package contains libraries and header files needed for
developing %{name} applications.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n pstoedit-%{version}

dos2unix doc/*.htm

%build

autoreconf -if --warnings=all
export OPTFLAGS="%{optflags}"
%configure --disable-static --enable-docs=yes \
           --with-magick --with-libplot --with-emf --with-gui
%make_build
%install
%make_install
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -pm 644 doc/pstoedit.1 $RPM_BUILD_ROOT%{_mandir}/man1/
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'
chrpath -d $RPM_BUILD_ROOT%{_bindir}/pstoedit
chrpath -d $RPM_BUILD_ROOT%{_bindir}/PstoeditQtGui
desktop-file-edit --remove-category=Utility $RPM_BUILD_ROOT%{_datadir}/applications/PstoeditQtGui.desktop
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n pstoedit-gui -f %{oreon_filedir}/pstoedit-gui.list
%files -n pstoedit-devel -f %{oreon_filedir}/pstoedit-devel.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.3-1
- Import
