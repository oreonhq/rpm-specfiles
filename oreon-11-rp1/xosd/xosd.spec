%global source0_hash 4f1fa96f4895baee6a3cba40f188a0da23bbac9d68e8c326d749e084143cb508
Name:           xosd
Version:        2.2.14
Release:        1%{?dist}
Summary:        On-screen display library for X
License:        GPL-2.0-or-later AND GPL-1.0-or-later
URL:            https://sourceforge.net/projects/libxosd/
Source0:        https://downloads.sourceforge.net/libxosd/%{name}-%{version}.tar.gz
Patch0:         %{name}-aclocal18.patch
Patch1:         %{name}-2.2.14-Do-not-install-some-manual-pages-twice.patch
Requires:       xorg-x11-fonts-misc
Obsoletes:      xmms-%{name} < 2.2.14-15
Obsoletes:      %{name}-xmms <= 2.2.12
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  glibc-common
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  perl-interpreter
# /oreon:deps
%description
XOSD displays text on your screen, sounds simple right? The difference
is it is unmanaged and shaped, so it appears transparent. This gives
the effect of an On Screen Display, like your TV/VCR etc.

%package        devel
Summary:        Development files for the XOSD on-screen display library
License:        GPL-2.0-or-later AND MIT-open-group
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libX11-devel
Requires:       libXext-devel
Requires:       libXinerama-devel
%description    devel
Header files and documentation for developing applications that use the XOSD
on-screen display.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p0
%patch -P1 -p1
# XMMS is dead, gdk-pixbuf-0 is dead. Dropping xmms plug-in.
sed -i -e '/AM_PATH_GTK/,+1 d' -e '/AM_PATH_XMMS/,+1 d' \
    -e '/AM_PATH_GDK_PIXBUF/,+1 d' configure.ac
# Update config.sub to support aarch64, bug #926836
autoreconf -i -f
for f in ChangeLog man/xosd_{create,destroy,display,is_onscreen,set_bar_length}.3 ; do
    iconv -f iso-8859-1 -t utf-8 "$f" > "${f}.utf8"
    touch -r "$f" "${f}.utf8"
    mv "${f}.utf8" "$f"
done

%build

%configure --disable-dependency-tracking --disable-static \
    --disable-gtktest --disable-gdk_pixbuftest \
    --disable-new-plugin --disable-old-plugin \
    --disable-beep_media_player_plugin\
    --enable-xinerama
%{make_build}
perl -pi -e "s|$RPM_OPT_FLAGS\\s*|| ; s|\\s*-Wall||" script/xosd-config
%install
%{make_install}
rm -f $RPM_BUILD_ROOT{%{_libdir},%{xmms_plugdir}}/*.la
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n xosd-devel -f %{oreon_filedir}/xosd-devel.list

%changelog

%autochangelog
