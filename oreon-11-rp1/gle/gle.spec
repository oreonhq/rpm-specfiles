%global source1_hash 02c13fe038f8b4b7726ac3e6a74410e299f50cdccb2b040d7ed1fbc99b9cfbef
%global source0_hash 6cd6b1d82cbf2c7a0b0affbd67c0ec32460ef6a13f6b41dfdd6f308fd651f102
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}
%global oname  gle-graphics
Summary:        Graphics Layout Engine
Name:          gle
Version:       4.2.5f
Release:        1%{?dist}
License:       GPL-2.0-or-later
URL:           http://www.gle-graphics.org/
Source0:        http://downloads.sourceforge.net/glx/gle-graphics-%{version}f-src.tar.gz
Source1:       http://downloads.sourceforge.net/glx/GLEusersguide.pdf
Patch:         gle-4.2.5-gcc7.patch
Patch:         gle-gcc15-complex.patch
Requires:      ghostscript
Requires:      tex(latex)
Requires:      tex(rotating.sty)
Requires:      tex(supertabular.sty)
# oreon:deps
BuildRequires:  cairo-devel
BuildRequires:  dos2unix
BuildRequires:  gcc-c++
BuildRequires:  ghostscript
BuildRequires:  libX11-devel
BuildRequires:  libXt-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libstdc++-devel
BuildRequires:  libtiff-devel
BuildRequires:  make
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  ncurses-devel
BuildRequires:  poppler-glib-devel
BuildRequires:  qt-devel
BuildRequires:  tex(latex)
BuildRequires:  tex(rotating.sty)
BuildRequires:  tex(supertabular.sty)
BuildRequires:  xorg-x11-proto-devel
BuildRequires:  zlib-devel
# /oreon:deps
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
make doc
%install
%make_install
mv %{buildroot}/%{_pkgdocdir}/gle-manual.pdf .
rm -rf %{buildroot}/%{_pkgdocdir}
dos2unix LICENSE.txt
rm -f %{buildroot}%{_libdir}/pkgconfig/gle-graphics.pc
%oreon_autofiles qgle usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n qgle -f %{oreon_filedir}/qgle.list
%files -n gle-doc -f %{oreon_filedir}/gle-doc.list

%changelog

%autochangelog
