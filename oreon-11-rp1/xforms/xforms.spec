%global source0_hash 78cc6b07071bbeaa1f906e0a22d5e9980e48f8913577bc082d661afe5cb75696

Summary:        GUI toolkit based on Xlib for X Window Systems
Name:           xforms
Version:        1.2.4
Release:        29%{?dist}
License:        LGPL-2.1-or-later
URL:            http://xforms-toolkit.org/
Source0:        https://download.savannah.nongnu.org/releases/%{name}/%{name}-%{version}%{?pre}.tar.gz
Source1:        https://download.savannah.nongnu.org/releases/%{name}/%{name}-%{version}%{?pre}.tar.gz.sig
Source2:        gpgkey-B5049F22184B56AF7C3AFBDBEB9474E50D5C15EB.gpg
Patch0:         xforms-1.2.4-gcc10.patch
BuildRequires:  gnupg2
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  libjpeg-devel
BuildRequires:  libXpm-devel
BuildRequires:  libGL-devel
BuildRequires:  libX11-devel
# import/export: png, sgi (optional?)
Requires:       netpbm-progs
# import eps,ps (optional?)
#Requires:       ghostscript
# eww, http://lists.nongnu.org/archive/html/xforms-development/2010-05/msg00000.html
Requires:       xorg-x11-fonts-ISO8859-1-75dpi
Requires:       xorg-x11-fonts-ISO8859-1-100dpi

%description
XForms is a GUI toolkit based on Xlib for X Window Systems. It features a
rich set of objects, such as buttons, sliders, browsers, and menus etc.
integrated into an easy and efficient object/event callback execution model
that allows fast and easy construction of X-applications. In addition, the
library is extensible and new objects can easily be created and added to
the library.

%package devel
Summary:        Development files for the XForms toolkit library
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libGL-devel
Requires:       libX11-devel

%description devel
The xforms-devel package includes header files and libraries necessary for
developing programs which use the XForms toolkit library.

%package doc
Summary:        Documentation files for the XForms toolkit library
BuildRequires:  texi2html
BuildRequires:  texinfo
BuildRequires:  texinfo-tex
BuildRequires:  ImageMagick
BuildArch:      noarch

%description doc
XForms is a GUI toolkit based on Xlib for X Window Systems. This package
contains the documentation for developing applications that use the XForms
toolkit library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n %{name}-%{version}%{?pre} -p1

# rpath hack
sed -i -e 's|"/lib /usr/lib|"/%{_lib} %{_libdir}|' configure

%build
%configure \
  --disable-demos \
  --enable-docs --htmldir=%{_pkgdocdir}/html --pdfdir=%{_pkgdocdir} \
  --disable-static \
  --enable-optimization="$RPM_OPT_FLAGS"

%make_build X_PRE_LIBS=""

%install
%make_install INSTALL='install -p'

rm -rfv demos/.deps
cp -r demos/ $RPM_BUILD_ROOT%{_pkgdocdir}/

## Unpackaged files
rm -fv  $RPM_BUILD_ROOT%{_libdir}/lib*.la
rm -rfv $RPM_BUILD_ROOT%{_infodir}/{dir,xforms_images}

%ldconfig_scriptlets

%files
%license COPYING.LIB Copyright
%doc ChangeLog README
%{_libdir}/libflimage.so.2*
%{_libdir}/libformsGL.so.2*
%{_libdir}/libforms.so.2*
%exclude %{_pkgdocdir}/demos/
%exclude %{_pkgdocdir}/html/
%exclude %{_pkgdocdir}/xforms.pdf

%files devel
%{_bindir}/fd2ps
%{_bindir}/fdesign
%{_includedir}/*.h
%{_libdir}/lib*.so
%{_mandir}/man1/*
%{_mandir}/man5/*

%files doc
%{_infodir}/xforms.info*
%{_pkgdocdir}/demos/
%{_pkgdocdir}/html/
%{_pkgdocdir}/xforms.pdf

%changelog
%autochangelog
