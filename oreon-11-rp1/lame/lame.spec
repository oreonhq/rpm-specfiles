# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 3df5124d5ad3a98312ffd7ba6a9b36230e4f8a3e66d3ce0f425e336c32d216eb
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           lame
Version:        4.0
Release:        %{autorelease}
Summary:        Free MP3 audio compressor
License:        LGPL-2.0-or-later AND LGPL-2.1-or-later
URL:            http://lame.sourceforge.net/
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch1:         %{name}-noexecstack.patch
Patch2:         libmp3lame-symbols.patch
Patch3:         frontend-utf8.patch

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig(libmpg123)
%ifarch %{ix86}
BuildRequires:  nasm
%endif
Requires:       %{name}-libs = %{version}-%{release}

%description
LAME is an open source MP3 encoder whose quality and speed matches
commercial encoders. LAME handles MPEG-1, 2 and 2.5 layer III encoding
with both constant and variable bitrates.

%package        libs
Summary:        LAME MP3 encoding library

%description    libs
LAME MP3 encoding library.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs = %{version}-%{release}

%description    devel
This package development files for %{name}.

%prep
%oreon_sha256
%autosetup -p1

%build
sed -i -e 's/^\(\s*hardcode_libdir_flag_spec\s*=\).*/\1/' configure
%ifarch %{ix86}
export CFLAGS="$RPM_OPT_FLAGS -ffast-math"
export ac_cv_header_xmmintrin_h=no
%endif
%configure \
  --disable-dependency-tracking \
  --disable-static \
%ifarch %{ix86}
  --enable-nasm \
%endif
  --enable-mp3rtp

%make_build

%install
%make_install INSTALL="install -p"
rm -f %{buildroot}%{_libdir}/*.la
ln -sf lame/lame.h %{buildroot}%{_includedir}/lame.h
rm -rf %{buildroot}%{_docdir}/%{name}

%check
make test

%files
%doc README TODO USAGE doc/html/*.html
%{_bindir}/lame
%{_bindir}/mp3rtp
%{_mandir}/man1/lame.1*

%files libs
%doc ChangeLog
%license COPYING LICENSE
%{_libdir}/libmp3lame.so.0{,.*}

%files devel
%doc API HACKING STYLEGUIDE
%{_includedir}/lame
%{_includedir}/lame.h
%{_libdir}/libmp3lame.so
%{_libdir}/pkgconfig/lame.pc

%changelog
%autochangelog
