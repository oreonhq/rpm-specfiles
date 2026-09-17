%global source0_hash 9fc1799f7ea6a95c7c5882de98be85fc7d20ba0a4a6fcacae11c8c6b382bb207

Summary:        A MOD music file player library
Name:           libmikmod
Version:        3.3.13
Release:        3%{?dist}
# Automatically converted from old format: GPLv2 and LGPLv2+ - review is highly recommended.
License:        GPL-2.0-only AND LicenseRef-Callaway-LGPLv2+
URL:            http://mikmod.sourceforge.net/
Source0:        http://downloads.sourceforge.net/mikmod/libmikmod-%{version}.tar.gz
Patch0:         libmikmod-64bit.patch
Patch1:         libmikmod-multilib.patch
Patch2:         libmikmod-cflags.patch
BuildRequires:  gcc
BuildRequires:  alsa-lib-devel pulseaudio-libs-devel
BuildRequires:  autoconf automake libtool make

%description
libmikmod is a library used by the mikmod MOD music file player for
UNIX-like systems. Supported file formats include MOD, STM, S3M, MTM,
XM, ULT and IT.

%package devel
Summary:        Header files and documentation for compiling mikmod applications
Provides:       mikmod-devel = %{version}-%{release}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pulseaudio-libs-devel%{?_isa}

%description devel
This package includes the header files you will need to compile
applications for mikmod.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
autoreconf -vi
%configure --enable-dl --enable-alsa --disable-simd
%make_build

%install
%make_install INSTALL="install -p"
rm -f %{buildroot}%{_infodir}/dir %{buildroot}%{_libdir}/*.a
find %{buildroot} -name '*.la' -print -delete

%ldconfig_scriptlets

%files
%doc AUTHORS NEWS README TODO
%license COPYING.LIB COPYING.LESSER
%{_libdir}/libmikmod.so.3*

%files devel
%{_bindir}/%{name}-config
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/aclocal/%{name}.m4
%{_includedir}/mikmod.h
%{_infodir}/mikmod.info*
%{_mandir}/man1/%{name}-config*

%changelog
%autochangelog
