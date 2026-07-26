%global source0_hash 42c28b9ef57998ad66bbbb3dfab00c6684715c643d9ccc9ac8da4d7cf296dd00

Name:           libsidplayfp
Version:        2.15.0
Release:        2%{?dist}
Summary:        SID chip music module playing library
# Zlib (src/utils/MD5/), GPL-2.0-only (src/builders/exsid-builder/) and GPL-2.0-or-later (the rest)
License:        GPL-2.0-or-later AND GPL-2.0-only AND Zlib
URL:            https://github.com/libsidplayfp
Source0:        https://github.com/libsidplayfp/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gcc gcc-c++ libtool doxygen
BuildRequires:  libftdi-c++-devel libgcrypt-devel
BuildRequires:  make
Provides:       bundled(md5-deutsch-c++)

%description
This library provides support for playing SID music modules originally
created on Commodore 64 and compatibles. It contains a processing engine
for MOS 6510 machine code and MOS 6581 Sound Interface Device (SID)
chip output. It is used by music player programs like SIDPLAY and
several plug-ins for versatile audio players.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
These are the files needed for compiling programs that use %{name}.

%package devel-doc
Summary:        API documentation for %{name}
BuildArch:      noarch

%description devel-doc
This package contains API documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
# Regenerate autofoo stuff, it is better to always build this from source
rm -r aclocal.m4 build-aux
autoreconf -ivf

%build
%configure --disable-static
make %{_smp_mflags} all doc

%install
%make_install INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%ldconfig_scriptlets

%files
%doc AUTHORS NEWS README TODO
%license COPYING
%{_libdir}/libsidplayfp.so.6*
%{_libdir}/libstilview.so.0*

%files devel
%{_libdir}/libsidplayfp.so
%{_libdir}/libstilview.so
%{_includedir}/sidplayfp/
%{_includedir}/stilview/
%{_libdir}/pkgconfig/*.pc

%files devel-doc
%doc docs/html

%changelog
%autochangelog
