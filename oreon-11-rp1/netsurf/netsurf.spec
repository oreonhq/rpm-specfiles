%global source0_hash 4dea880ff3c2f698bfd62c982b259340f9abcd7f67e6c8eb2b32c61f71644b7b
Name:           netsurf
Version:        3.11
Release:        1%{?dist}
Summary:        Compact graphical web browser
License:        GPL-2.0-only
URL:            https://www.netsurf-browser.org/
Source0:        https://download.netsurf-browser.org/netsurf/releases/source-full/netsurf-all-%{version}.tar.gz
# oreon:deps
BuildRequires:  /usr/bin/hostname
BuildRequires:  /usr/bin/perl
BuildRequires:  /usr/bin/xxd
BuildRequires:  bison
BuildRequires:  curl-devel
BuildRequires:  desktop-file-utils
BuildRequires:  expat-devel
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gdk-pixbuf2-modules-extra(x86-64)
BuildRequires:  gperf
BuildRequires:  gtk3-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(IO::Compress::Gzip)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libvncserver)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(sdl)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-atom)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  zlib-devel
# /oreon:deps
%description
NetSurf is a compact graphical web browser which aims for HTML5, CSS and
JavaScript support.

This package ships the version with GTK3 frontend that most users will
want to use.

%package fb
Summary:        Compact graphical web browser (framebuffer frontend)
Requires:       dejavu-sans-fonts >= 2.37-5
Requires:       dejavu-serif-fonts >= 2.37-5
Requires:       dejavu-sans-mono-fonts >= 2.37-5
%description fb
NetSurf is a compact graphical web browser which aims for HTML5, CSS and
JavaScript support.

This package ships the version with a special-purpose framebuffer frontend.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n netsurf-all-%{version}

%global common_make_opts V=1 PREFIX=%{_prefix} \\\
        NETSURF_USE_WEBP=YES \\\
        NETSURF_USE_NSSVG=YES \\\
        NETSURF_USE_ROSPRITE=NO \\\
        NETSURF_USE_NSPSL=YES \\\
        NETSURF_USE_NSLOG=YES \\\
        NETSURF_USE_HARU_PDF=NO \\\
        NETSURF_USE_VIDEO=NO

%global fb_make_opts %{common_make_opts} TARGET=framebuffer \\\
        NETSURF_USE_RSVG=NO \\\
        NETSURF_USE_FREETYPE2=YES \\\
        NETSURF_FB_FONTLIB=freetype \\\
        NETSURF_FB_FONT_SANS_SERIF=dejavu-sans-fonts/DejaVuSans.ttf \\\
        NETSURF_FB_FONT_SANS_SERIF_BOLD=dejavu-sans-fonts/DejaVuSans-Bold.ttf \\\
        NETSURF_FB_FONT_SANS_SERIF_ITALIC=dejavu-sans-fonts/DejaVuSans-Oblique.ttf \\\
        NETSURF_FB_FONT_SANS_SERIF_ITALIC_BOLD=dejavu-sans-fonts/DejaVuSans-BoldOblique.ttf \\\
        NETSURF_FB_FONT_SERIF=dejavu-serif-fonts/DejaVuSerif.ttf \\\
        NETSURF_FB_FONT_SERIF_BOLD=dejavu-serif-fonts/DejaVuSerif-Bold.ttf \\\
        NETSURF_FB_FONT_MONOSPACE=dejavu-sans-mono-fonts/DejaVuSansMono.ttf \\\
        NETSURF_FB_FONT_MONOSPACE_BOLD=dejavu-sans-mono-fonts/DejaVuSansMono-Bold.ttf \\\
        NETSURF_FB_FONT_CURSIVE=dejavu-serif-fonts/DejaVuSerif-Italic.ttf \\\
        NETSURF_FB_FONT_FANTASY=dejavu-sans-fonts/DejaVuSansCondensed-Bold.ttf \\\
        NETSURF_FB_FONTPATH=/usr/share/fonts

%global gtk_make_opts %{common_make_opts} TARGET=gtk3 \\\
        NETSURF_USE_RSVG=YES

%build

[ $(grep NETSURF_FB_FONT_ netsurf/frontends/framebuffer/Makefile.defaults |wc -l) = 10 ]
export CFLAGS='%{optflags}'
export CXXFLAGS='%{optflags}'
make %{?_smp_mflags} %{fb_make_opts}
make %{?_smp_mflags} %{gtk_make_opts}
%install
%make_install %{fb_make_opts}
%make_install %{gtk_make_opts}
mkdir -p %{buildroot}%{_datadir}/pixmaps \
        %{buildroot}%{_datadir}/applications
install -pm644 netsurf/frontends/gtk/res/netsurf.xpm \
        %{buildroot}%{_datadir}/pixmaps
sed 's/Exec=netsurf-gtk/Exec=netsurf-gtk3/;s/netsurf.png/netsurf/' \
        <netsurf/frontends/gtk/res/netsurf-gtk.desktop \
        >%{buildroot}%{_datadir}/applications/netsurf-gtk.desktop
desktop-file-validate \
        %{buildroot}%{_datadir}/applications/netsurf-gtk.desktop
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n netsurf-fb -f %{oreon_filedir}/netsurf-fb.list

%changelog

%autochangelog
