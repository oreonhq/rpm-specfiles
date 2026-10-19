%global source0_hash 3df5124d5ad3a98312ffd7ba6a9b36230e4f8a3e66d3ce0f425e336c32d216eb
Name:           lame
Version:        4.0
Release:        1%{?dist}
Summary:        Free MP3 audio compressor
License:        LGPL-2.0-or-later AND LGPL-2.1-or-later
URL:            http://lame.sourceforge.net/
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch1:         %{name}-noexecstack.patch
Patch2:         libmp3lame-symbols.patch
%ifarch %{ix86}
%endif
Requires:       %{name}-libs = %{version}-%{release}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig(libmpg123)
# /oreon:deps
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make test
%files -f %{oreon_filedir}/main.list
%files -n lame-libs -f %{oreon_filedir}/lame-libs.list
%files -n lame-devel -f %{oreon_filedir}/lame-devel.list

%changelog

%autochangelog
