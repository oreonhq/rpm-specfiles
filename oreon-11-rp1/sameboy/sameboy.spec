%global source0_hash 2dadfcc71cb7a425bfde497087c85ec2999213e519e9ed5ee06f0d57fee38c51
Name:           sameboy
Version:        1.0.2
Release:        1%{?dist}
Summary:        Game Boy and Game Boy Color emulator written in C
License:        MIT
URL:            https://sameboy.github.io/
Source0:        https://github.com/LIJI32/SameBoy/archive/v%{version}/%{name}-%{version}.tar.gz
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  rgbds
# /oreon:deps
%description
SameBoy is an open source Game Boy (DMG) and Game Boy Color (CGB) emulator,
written in portable C. It has a native Cocoa front-end for MacOS,
an SDL front-end for other operating systems, and a libretro core.
It also includes a text-based debugger with expression evaluation.

%package thumbnailer
Summary:        Thumbnailer for Game Boy and Game Boy Color games
%description thumbnailer
Thumbnailer for Game Boy and Game Boy Color games

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir SameBoy-%{version}
%oreon_prep
%build

%set_build_flags
%make_build \
    xdg-thumbnailer sdl \
    DATA_DIR=%{_datadir}/%{name}/
%install
mkdir -p %{buildroot}/%{_bindir} \
         %{buildroot}/%{_datadir}
%make_install \
    PREFIX=%{_prefix} \
    DATA_DIR=%{_datadir}/%{name}/ \
    FREEDESKTOP=true \
    CONF=debug
cd FreeDesktop
cp %{name}.desktop %{name}-terminal.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n sameboy-thumbnailer -f %{oreon_filedir}/sameboy-thumbnailer.list

%changelog

%autochangelog
