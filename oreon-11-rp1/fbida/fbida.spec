%global source0_hash e8e5dcc28e5b95998ed71195fb9d38bba92b111a3683a3190f5a61f90083aa99

Summary:        FrameBuffer Imageviewer
Name:           fbida
Version:        2.15
Release:        1%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://www.kraxel.org/blog/linux/fbida/

%global git_tag %{name}-%{version}-1
Source:         https://gitlab.com/kraxel/%{name}/-/archive/%{git_tag}/%{name}-%{git_tag}.tar.gz

BuildRequires:  gcc
BuildRequires:  giflib-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libXpm-devel
BuildRequires:  libXt-devel
BuildRequires:  meson
BuildRequires:  motif-devel
BuildRequires:  perl-generators
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libsystemd) >= 237
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libtsm)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(poppler-glib)
BuildRequires:  pkgconfig(xkbcommon)

Requires:       ImageMagick

%description
fbi displays the specified file(s) on the linux console using the
framebuffer device. PhotoCD, jpeg, ppm, gif, tiff, xwd, bmp and png
are supported directly. For other formats fbi tries to use
ImageMagick's convert.

%package fbcon
Summary: Framebuffer-backed terminal emulator

%description fbcon
This is an X11 application providing a simple terminal emulator.

%package fbgs
Summary: Framebuffer Postscript Viewer
Requires: fbida%{?_isa} = %{version}-%{release}
Requires: ghostscript

%description fbgs
A wrapper script for viewing ps/pdf files on the framebuffer console using fbi

%package fbpdf
Summary: Framebuffer PDF Viewer

%description fbpdf
fbpdf displays PDF files on the framebuffer device.

%package ida
Summary: Motif based Imageviewer

%description ida
This is a X11 application (Motif based) for viewing images. Some basic
editing functions are available too.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{git_tag}

%build
%meson
%meson_build

%install
%meson_install
# Installing via meson misses the fbgs man page
install -m 644 -p man/fbgs.1 %{buildroot}%{_mandir}/man1/

%files
%license COPYING
%doc Changes README.md TODO
%doc %{_mandir}/man1/fbi*
%doc %{_mandir}/man1/exiftran*
%{_bindir}/fbi
%{_bindir}/exiftran

%files fbcon
%license COPYING
%{_bindir}/fbcon
%{_datadir}/wayland-sessions/fbcon.desktop

%files fbgs
%license COPYING
%doc %{_mandir}/man1/fbgs*
%{_bindir}/fbgs

%files fbpdf
%license COPYING
%{_bindir}/fbpdf

%files ida
%license COPYING
%doc %{_mandir}/man1/ida*
%{_bindir}/ida
%{_datadir}/X11/app-defaults/Ida

%changelog
%autochangelog
