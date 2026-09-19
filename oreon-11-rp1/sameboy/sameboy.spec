%global source0_hash 2dadfcc71cb7a425bfde497087c85ec2999213e519e9ed5ee06f0d57fee38c51

Name:           sameboy
Version:        1.0.2
Release:        2%{?dist}
Summary:        Game Boy and Game Boy Color emulator written in C

License:        MIT
URL:            https://sameboy.github.io/
Source0:        https://github.com/LIJI32/SameBoy/archive/v%{version}/%{name}-%{version}.tar.gz

Requires:       hicolor-icon-theme
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  rgbds
BuildRequires:  desktop-file-utils
# SDL
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(gl)
# xdg-thumbnailer
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)

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

%autosetup -n SameBoy-%{version}

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

%files
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.bin
%{_datadir}/%{name}/*.sym
%{_datadir}/%{name}/background.bmp
%dir %{_datadir}/%{name}/Shaders
%{_datadir}/%{name}/Shaders/*.fsh
%{_datadir}/%{name}/Palettes/*.sbp
%{_datadir}/%{name}/LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/*/mimetypes/x-gameboy*rom.png
%license LICENSE
%doc README.md

%files thumbnailer
%{_bindir}/sameboy-thumbnailer
%{_datadir}/thumbnailers/sameboy.thumbnailer

%changelog
%autochangelog
