Name:       xmodmap
Version:    1.0.11
Release:    10%{?dist}
Summary:    Edit and display the X11 core keyboard map

License:    MIT AND MIT-open-group
URL:        https://www.x.org
Source0:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz
# oreon url source checksums begin
%global source0_sha256 9a2f8168f7b0bc382828847403902cb6bf175e17658b36189eac87edda877e81
%global source0_file xmodmap-1.0.11.tar.xz
# oreon url source checksums end

BuildRequires:  automake libtool
BuildRequires:  gcc make
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

Obsoletes:  xorg-x11-server-utils < 7.7-40

%description
The xmodmap program is used to edit and display the keyboard modifier
map and keymap table that are used by client applications to convert
event keycodes into keysyms.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/xmodmap-1.0.11.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "9a2f8168f7b0bc382828847403902cb6bf175e17658b36189eac87edda877e81" || { echo "oreon: Source0 SHA256 mismatch for xmodmap-1.0.11.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup

%build
autoreconf -v --install
%configure --disable-silent-rules
%make_build

%install
%make_install

%files
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.11-10
- Prepare for Oreon 11 (RP1)
