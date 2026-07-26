%global source0_hash 6cd6b1d82cbf2c7a0b0affbd67c0ec32460ef6a13f6b41dfdd6f308fd651f102

%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

%global oname  gle-graphics

Summary:       Graphics Layout Engine
Name:          gle
Version:       4.2.5
Release:       31%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:       GPL-2.0-or-later
URL:           http://www.gle-graphics.org/
Source0:       http://downloads.sourceforge.net/glx/gle-graphics-%{version}f-src.tar.gz
Source1:       http://downloads.sourceforge.net/glx/GLEusersguide.pdf
# https://sourceforge.net/p/glx/mailman/glx-devel/?viewmonth=201708
Patch:         gle-4.2.5-gcc7.patch
Patch:         gle-gcc15-complex.patch
BuildRequires: cairo-devel
BuildRequires: dos2unix
BuildRequires: gcc-c++
BuildRequires: ghostscript
BuildRequires: libX11-devel
BuildRequires: libXt-devel
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: libstdc++-devel >= 3.0
BuildRequires: libtiff-devel
BuildRequires: make
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libGLU-devel
BuildRequires: ncurses-devel
BuildRequires: poppler-glib-devel
BuildRequires: qt-devel >= 4.1.1
BuildRequires: tex(latex)
BuildRequires: tex(rotating.sty)
BuildRequires: tex(supertabular.sty)
BuildRequires: xorg-x11-proto-devel
BuildRequires: zlib-devel
Requires:      ghostscript
Requires:      tex(latex)
Requires:      tex(rotating.sty)
Requires:      tex(supertabular.sty)

%description
GLE (Graphics Layout Engine) is a high-quality graphics package for
scientists, combining a user-friendly scripting language with a full
range of facilities for producing publication-quality graphs,
diagrams, posters and slides. GLE provides LaTeX quality fonts
together with a flexible graphics module which allows the user to
specify any feature of a graph. Complex pictures can be drawn with
user-defined subroutines and simple looping structures. Current output
formats include EPS, PS, PDF, JPEG, and PNG.

%package -n    qgle
Summary:       QT frontend to GLE
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description -n qgle
GLE (Graphics Layout Engine) is a high-quality graphics package for
scientists, combining a user-friendly scripting language with a full
range of facilities for producing publication-quality graphs,
diagrams, posters and slides. GLE provides LaTeX quality fonts
together with a flexible graphics module which allows the user to
specify any feature of a graph. Complex pictures can be drawn with
user-defined subroutines and simple looping structures. Current output
formats include EPS, PS, PDF, JPEG, and PNG.

This package contains the QT frontend.

%package       doc
Summary:       User documentation for GLE
BuildArch:     noarch

%description doc
GLE (Graphics Layout Engine) is a high-quality graphics package for
scientists, combining a user-friendly scripting language with a full
range of facilities for producing publication-quality graphs,
diagrams, posters and slides. GLE provides LaTeX quality fonts
together with a flexible graphics module which allows the user to
specify any feature of a graph. Complex pictures can be drawn with
user-defined subroutines and simple looping structures. Current output
formats include EPS, PS, PDF, JPEG, and PNG.

This package contains the user documentation.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{oname}-%{version}
install -p -m 0644 %{SOURCE1} .
touch -r README.txt configure.ac

%build
export CXXFLAGS="-std=c++14 $RPM_OPT_FLAGS"
%configure --with-qt=%{_libdir}/qt4 \
           --with-jpeg              \
           --with-png               \
           --with-tiff              \
           --with-z                 \
           --with-x                 \
           --with-rpath=no          \
           --with-debug=yes         \
           --with-libgle=yes        \
           --with-extrafonts=yes    \
           --docdir=%{_pkgdocdir}   \
           CPPFLAGS="%{optflags} -std=c++14" \
           CXXFLAGS="%{optflags}"
make
# %{?_smp_mflags} build fails

# docs
make doc

%install
%make_install
mv %{buildroot}/%{_pkgdocdir}/gle-manual.pdf .
rm -rf %{buildroot}/%{_pkgdocdir}

# Some fixes
dos2unix LICENSE.txt
rm -f %{buildroot}%{_libdir}/pkgconfig/gle-graphics.pc

%files
%license LICENSE.txt
%doc README.txt src/gui/readme.txt
%{_bindir}/gle
%{_bindir}/glebtool
%{_bindir}/manip
%{_datadir}/gle-graphics
%{_mandir}/man1/gle.1*
%{_libdir}/libgle-graphics-%{version}.so

%files -n qgle
%license LICENSE.txt
%{_bindir}/qgle

%files doc
%license LICENSE.txt
%doc gle-manual.pdf GLEusersguide.pdf

%changelog
%autochangelog
