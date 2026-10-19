%global source0_hash dffd82b8f254c3489c32098da831f33eac7136843d1e7ccb802f1254ad5b4219
Summary:        A MOD music file player library
Name:           libmikmod
Version:        3.3.14
Release:        1%{?dist}
License:        GPL-2.0-only AND LicenseRef-Callaway-LGPLv2+
URL:            http://mikmod.sourceforge.net/
Source0:        http://downloads.sourceforge.net/mikmod/libmikmod-%{version}.tar.gz
Patch0:         libmikmod-64bit.patch
Patch1:         libmikmod-multilib.patch
Patch2:         libmikmod-cflags.patch
# oreon:deps
BuildRequires:  alsa-lib-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pulseaudio-libs-devel
# /oreon:deps
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
%oreon_prep
%build

autoreconf -vi
%configure --enable-dl --enable-alsa --disable-simd
%make_build
%install
%make_install INSTALL="install -p"
rm -f %{buildroot}%{_infodir}/dir %{buildroot}%{_libdir}/*.a
find %{buildroot} -name '*.la' -print -delete
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libmikmod-devel -f %{oreon_filedir}/libmikmod-devel.list

%changelog

%autochangelog
