%global source0_hash 5076ca48455a4ef4ead2cd880ba189b21937a9ad8fd458adfc133d7bb1c948c3
Name:           libklvanc
Version:        1.6.0
Release:        4%{?dist}
Summary:        VANC Processing Framework
License:        LGPL-2.1
URL:            https://github.com/stoth68000/libklvanc
Source0:        https://github.com/stoth68000/%{name}/archive/vid.obe.%{version}.tar.gz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  libtool
# /oreon:deps
%description
Libklvanc is a library which can be used for parsing/generation of Vertical
Ancillary Data (VANC) commonly found in the Serial Digital Interface (SDI) wire
protocol.

The library includes a general parser/decoder and an encoder for VANC lines, as
well as the ability to both decode and generate protocols commonly found in SDI,
including:

- SMPTE ST 334 - CEA-708 closed captions in VANC
- SMPTE ST 2016 Active Format Descriptor (AFD) and Bar Data
- SCTE-104 Ad triggers
- SMPTE ST 2038 arbitrary VANC encapsulation
- SMPTE ST 12-2 Timecodes
- SMPTE RDD 8 Subtitle Distribution packets
- SMPTE ST 2108-1 HDR/WCG Metadata Packing and Signaling

By providing both encoders and decoders, the library can be used for common use
cases involving both capture of SDI (and subsequent decoding) as well as
generation of VANC for inclusion in an SDI output interface. This includes
computing/validating checksums at various levels and dealing with subtle edge
cases related to VANC line formatting such as ensuring packets are contiguous.

The library also provides utility functions for various colorspaces VANC may be
represented in, including the V210 format typically used by BlackMagic Decklink
SDI cards.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%global oreon_srcdir %{name}-vid.obe.%{version}
%oreon_prep
%build

autoreconf -vif
%configure --disable-static
%make_build
doxygen doxygen/%{name}.doxyconf
%install
%make_install
rm -f %{buildroot}%{_libdir}/%{name}.la
rm -fr %{buildroot}%{_bindir}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libklvanc-devel -f %{oreon_filedir}/libklvanc-devel.list

%changelog

%autochangelog
