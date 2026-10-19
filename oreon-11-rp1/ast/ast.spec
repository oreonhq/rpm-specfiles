%global source0_hash 43c558522767b8506b7a88edcacece3f5d814822f5fccd8949a9b7244fefa724
Name:           ast
Version:        9.2.12
Release:        1%{?dist}
Summary:        A Library for Handling World Coordinate Systems in Astronomy
License:        LGPL-3.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:            http://starlink.eao.hawaii.edu/starlink/AST
Source0:        https://github.com/Starlink/ast/releases/download/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cminpack-devel
BuildRequires:  erfa-devel
BuildRequires:  gcc-gfortran
BuildRequires:  libpal-devel
BuildRequires:  make
BuildRequires:  perl-interpreter
# /oreon:deps
%description
The AST library provides a comprehensive range of facilities for attaching
world coordinate systems to astronomical data, for retrieving and interpreting
that information and for generating graphical output based on it. It's main
selling points are:

* Ease of use.
* Facilities for generating plots of generalized non-linear, potentially
  discontinuous 2-D or 3-D coordinate systems, with detailed control of the
  appearance of the plot.
* Facilities for converting transparently between different coordinate
  systems, including a wide range of celestial, spectral and time coordinate
  systems.
* Facilities for searching a general collection of connected coordinate
  systems for a coordinate system with any given set of characteristics.
* Allows code for handling WCS information to be written in a general way
  without regard to the specific nature of the coordinate systems being
  handled (i.e. whether they represent sky positions, spectral positions,
  focal plane positions, pixel positions, etc).
* Flexible system for saving and retrieving WCS information, including (but
  not limited to) a range of different popular FITS descriptions.
* Written in C but has interfaces for C, Fortran, Java (via JNI), Perl, and
  UNIX shell.
* Extensive documentation. 

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

Applications should make use of the ast_link command for setting the
libraries to link to, e.g.:

  cc prog.c `ast_link` -o prog

%package        doc
Summary:        Documentation for %{name}
%description    doc
C and Fortran programming documentation for %{name}.

%prep

%setup -q
rm -r cminpack erfa erfa.h erfam.h pal pal.h
sed -i -e 's,cminpack/,cminpack-1/,' src/polymap.c
sed -i -e '1i#!/bin/bash' ast_link*
# Fix FSF address
sed -i -e 's/675 Mass Ave, Cambridge, MA 02139/51 Franklin Street, Fifth Floor, Boston, MA  02110-1301/' COPYING.LIB

%build

%configure CPPFLAGS="-I%{_includedir}/star" CFLAGS="%{optflags} -std=gnu17" --disable-static --libdir=%{_libdir}/%{name} --with-external_cminpack --with-external_pal
%make_build
%install
%make_install
find %buildroot -name '*.la' -delete
mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d
echo %{_libdir}/%{name} > %{buildroot}%{_sysconfdir}/ld.so.conf.d/%{name}_%{_arch}.conf
mkdir -p %{buildroot}%{_pkgdocdir}
mv %{buildroot}%{_prefix}/docs/*.pdf %{buildroot}%{_pkgdocdir}/
rm -r %{buildroot}%{_prefix}/docs
rm -r %{buildroot}%{_datadir}/ast
rm -r %{buildroot}%{_prefix}/{help,manifests,news}
rm %{buildroot}%{_bindir}/ast_link_adam
rm %{buildroot}%{_libdir}/%{name}/libast_{drama,ems,pgplot{,3d}}.so*
%oreon_autofiles ast-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles ast-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make check
%files -f %{oreon_filedir}/main.list
%files -n ast-devel -f %{oreon_filedir}/ast-devel.list
%files -n ast-doc -f %{oreon_filedir}/ast-doc.list

%changelog

%autochangelog
