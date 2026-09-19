%global source0_hash none

Name:           ast
Version:        9.2.12
Release:        4%{?dist}
Summary:        A Library for Handling World Coordinate Systems in Astronomy

# proj.c proj.h wcsmath.h wcstrig.c wcstrig.h are LGPLv2+
# Automatically converted from old format: LGPLv3+ and LGPLv2+ - review is highly recommended.
License:        LGPL-3.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:            http://starlink.eao.hawaii.edu/starlink/AST
Source0:        https://github.com/Starlink/ast/releases/download/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-gfortran
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  cminpack-devel
BuildRequires:  erfa-devel
BuildRequires:  libpal-devel

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
# Do not conflict with libast (bug #978262)
# -std=gnu17 needed for gcc 15 compatibility https://github.com/Starlink/ast/issues/27
%configure CPPFLAGS="-I%{_includedir}/star" CFLAGS="%{optflags} -std=gnu17" --disable-static --libdir=%{_libdir}/%{name} --with-external_cminpack --with-external_pal
%make_build

%install
%make_install
find %buildroot -name '*.la' -delete
# Setup ld.so.conf.d
mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d
echo %{_libdir}/%{name} > %{buildroot}%{_sysconfdir}/ld.so.conf.d/%{name}_%{_arch}.conf
# Docs are installed to the wrong location, don't need source
mkdir -p %{buildroot}%{_pkgdocdir}
mv %{buildroot}%{_prefix}/docs/*.pdf %{buildroot}%{_pkgdocdir}/
rm -r %{buildroot}%{_prefix}/docs
rm -r %{buildroot}%{_datadir}/ast
rm -r %{buildroot}%{_prefix}/{help,manifests,news}
# This references an uninstalled library
rm %{buildroot}%{_bindir}/ast_link_adam
# These reference other libraries
rm %{buildroot}%{_libdir}/%{name}/libast_{drama,ems,pgplot{,3d}}.so*

%check
make check

%files
%license COPYING*
%config(noreplace) %{_sysconfdir}/ld.so.conf.d/%{name}_%{_arch}.conf
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*.so.9*

%files devel
%{_bindir}/ast_link
%{_includedir}/*
%{_libdir}/%{name}/*.so

%files doc
%{_pkgdocdir}/

%changelog
%autochangelog
