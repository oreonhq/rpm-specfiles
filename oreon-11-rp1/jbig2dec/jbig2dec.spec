%global source0_hash 7b63ff6470289547e7a3a0f145cb8ea6c2afffdd65645b7d87d3b7febc96fb3a

Name:		jbig2dec
Version:	0.20
Release:	%autorelease
Summary:	A decoder implementation of the JBIG2 image compression format 
License:	AGPL-3.0-or-later
URL:		https://jbig2dec.com
Source0:	https://github.com/ArtifexSoftware/jbig2dec/releases/download/%{version}/%{name}-%{version}.tar.gz
Requires:	%{name}-libs = %{version}-%{release}
BuildRequires:	libtool
BuildRequires:	libpng-devel
BuildRequires: make

%description
jbig2dec is a decoder implementation of the JBIG2 image compression format.
JBIG2 is designed for lossy or lossless encoding of 'bilevel' (1-bit
monochrome) images at moderately high resolution, and in particular scanned
paper documents. In this domain it is very efficient, offering compression
ratios on the order of 100:1.

%package libs 
Summary:	A decoder implementation of the JBIG2 image compression format

%description libs 
jbig2dec is a decoder implementation of the JBIG2 image compression format.
JBIG2 is designed for lossy or lossless encoding of 'bilevel' (1-bit
monochrome) images at moderately high resolution, and in particular scanned
paper documents. In this domain it is very efficient, offering compression
ratios on the order of 100:1.

This package provides the shared jbig2dec library.

%package devel
Summary:	Static library and header files for development with jbig2dec
Requires:	%{name}-libs = %{version}-%{release}

%description devel
jbig2dec is a decoder implementation of the JBIG2 image compression format.
JBIG2 is designed for lossy or lossless encoding of 'bilevel' (1-bit
monochrome) images at moderately high resolution, and in particular scanned
paper documents. In this domain it is very efficient, offering compression
ratios on the order of 100:1.

This package is only needed if you plan to develop or compile applications
which requires the jbig2dec library.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup


%build
autoreconf -fi
%configure --disable-static
%make_build


%install
%make_install
rm -f %{buildroot}%{_libdir}/*.la

%ldconfig_scriptlets libs


%files
%doc CHANGES COPYING LICENSE README
%{_bindir}/jbig2dec
%{_mandir}/man?/jbig2dec.1*

%files devel
%doc CHANGES COPYING LICENSE README
%{_includedir}/jbig2.h
%{_libdir}/libjbig2dec.so
%{_libdir}/pkgconfig/%{name}.pc

%files libs
%doc CHANGES COPYING LICENSE README
%{_libdir}/libjbig2dec.so.0
%{_libdir}/libjbig2dec.so.0.0.0



%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.20-1
- Prepare for Oreon 11 (RP1)
