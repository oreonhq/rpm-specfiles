%global source0_hash f3e39a19c3dddcb12747879ebeefb4186327e32fb560b06f58bc6dd6f0a6e611

Name:           jwm
Version:        2.4.6
Release:        3%{?dist}
Summary:        Joe's Window Manager

License:        MIT
URL:            http://joewing.net/projects/jwm/
Source0:        https://github.com/joewing/jwm/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop

Patch0:		gettext_021.patch

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gcc
BuildRequires:	gettext-devel
BuildRequires:	make
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(fribidi)
BuildRequires:	pkgconfig(libjpeg)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:	pkgconfig(pango)
BuildRequires:	pkgconfig(xft)
BuildRequires:	pkgconfig(xinerama)
BuildRequires:	pkgconfig(xmu)
BuildRequires:	pkgconfig(xpm)
BuildRequires:	pkgconfig(xrender)
Recommends:	/usr/bin/xterm
Recommends:	/usr/bin/xlock

%description
JWM is a window manager for the X11 Window System. It's written in C and uses
only Xlib at a minimum. The following libraries can also be used if available:

* cairo and librsvg2 for SVG icons and backgrounds.
* fribidi for bi-directional text support.
* libjpeg for JPEG icons and backgrounds.
* libpng for PNG icons and backgrounds.
* libXext for the shape extension.
* libXrender for the render extension.
* libXmu for rounded corners.
* libXft for anti-aliased and true type fonts.
* libXinerama for multiple head support.
* libXpm for XPM icons and backgrounds.

JWM supports MWM and Extended Window Manager Hints (EWMH).

Note that the Fedora package is built with all supported features enabled.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Preserve timestamps in installation
sed -i -e 's|install -m|install -pm|g' Makefile.in

%build
./autogen.sh
%configure
%make_build

%install
%make_install

mkdir -p %{buildroot}%{_datadir}/xsessions
install -Dpm0644 %{SOURCE1} %{buildroot}%{_datadir}/xsessions/

%find_lang %{name}

%files -f %{name}.lang
%license LICENSE
%doc README.md
%config(noreplace) %{_sysconfdir}/system.jwmrc
%{_bindir}/%{name}
%{_datadir}/xsessions/%{name}.desktop
%{_datadir}/%{name}/
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
