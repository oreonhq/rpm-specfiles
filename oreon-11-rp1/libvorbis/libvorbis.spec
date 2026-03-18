%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

Summary:	The Vorbis General Audio Compression Codec
Name:		libvorbis
Version:	1.3.7
Release:	14%{?dist}
Epoch:		1
License:	BSD-3-Clause
URL:		https://www.xiph.org/
Source:		https://downloads.xiph.org/releases/vorbis/%{name}-%{version}.tar.xz
BuildRequires:  gcc
BuildRequires:	pkgconfig(ogg) >= 1.0
BuildRequires: make

%description
Ogg Vorbis is a fully open, non-proprietary, patent- and royalty-free,
general-purpose compressed audio format for audio and music at fixed
and variable bitrates.

The libvorbis package contains runtime libraries for use in programs
that support Ogg Vorbis.

%package devel
Summary: Development tools for Vorbis applications
Requires:	%{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description devel
The libvorbis-devel package contains the header files and documentation
needed to develop applications with Ogg Vorbis.

%package devel-docs
Summary: Documentation for developing Vorbis applications
Requires: %{name}-devel = %{epoch}:%{version}-%{release}
BuildArch: noarch

%description devel-docs
Documentation for developing applications with libvorbis.

%prep

%setup -q
sed -i "s/-ffast-math//" configure
sed -i "s/-mcpu=750//" configure

%build
%configure --disable-static
%make_build

%install
%make_install docdir=%{_pkgdocdir}
# remove unpackaged files from the buildroot
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%check
make check

%files
%doc AUTHORS
%license COPYING
%{_libdir}/libvorbis.so.*
%{_libdir}/libvorbisfile.so.*
%{_libdir}/libvorbisenc.so.*

%files devel
%{_includedir}/vorbis
%{_libdir}/libvorbis.so
%{_libdir}/libvorbisfile.so
%{_libdir}/libvorbisenc.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/aclocal/vorbis.m4

%files devel-docs
%{_pkgdocdir}/*
%exclude %{_pkgdocdir}/doxygen-build.stamp

%ldconfig_scriptlets

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3.7-14
- Prepare for Oreon 11 (RP1)
