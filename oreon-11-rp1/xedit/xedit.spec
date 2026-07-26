%global source0_hash b00d488b29cd007fadf9a4e44193cbdd72b48c94080be5ebc02565f21f9a2a71

Name:		xedit
Version:	1.2.4
Release:	6%{?dist}
Summary:	Simple text editor for X
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz
Source1:	%{name}.desktop
# Automatically converted from old format: MIT and BSD - review is highly recommended.
License:	LicenseRef-Callaway-MIT AND LicenseRef-Callaway-BSD
BuildRequires:	libtool make
BuildRequires:	desktop-file-utils
BuildRequires:	libXaw-devel
BuildRequires:	xorg-x11-util-macros
Patch0:		xedit-hunspell.patch
Requires:	xorg-x11-xbitmaps
Requires:	hunspell
Requires:	hunspell-en
Requires:	grep
Requires:	words
Requires:	ctags
Requires:	xorg-x11-fonts-misc
Requires:	xorg-x11-fonts-75dpi
Requires:	xorg-x11-fonts-100dpi

%description
Xedit provides a simple text editor for X.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%configure --with-lispdir=%{_datadir}/X11/%{name}

%install
make install DESTDIR=${RPM_BUILD_ROOT} INSTALL="install -p"
install -D -m 644 %{SOURCE1} ${RPM_BUILD_ROOT}%{_datadir}/applications/%{name}.desktop
desktop-file-validate ${RPM_BUILD_ROOT}%{_datadir}/applications/%{name}.desktop

%check
make check

%files
%doc AUTHORS ChangeLog COPYING README
%{_bindir}/%{name}
%{_datadir}/X11/%{name}
%{_datadir}/X11/app-defaults/Xedit
%{_datadir}/X11/app-defaults/Xedit-color
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/xedit.1*

%changelog
%autochangelog
