%global source0_hash 6504ec232fc188eff15220aef9b7369f8d3a174ba70229f1c982e35517d44a24

Summary:       The Enlightenment window manager, DR16
Name:          e16
Version:       1.0.31
Release:       3%{?dist}
# Automatically converted from old format: MIT with advertising and GPLv2+ - review is highly recommended.
License:       LicenseRef-Callaway-MIT-with-advertising AND GPL-2.0-or-later
URL:           http://www.enlightenment.org/
Source0:       http://downloads.sourceforge.net/enlightenment/e16-%{version}.tar.xz
Patch:         0001-backgrounds-Save-backgrounds-after-modifying-one-in-.patch
BuildRequires: dbus-devel
BuildRequires: desktop-file-utils
BuildRequires: freetype-devel
BuildRequires: gcc
BuildRequires: imlib2-devel
BuildRequires: libSM-devel
BuildRequires: libXcomposite-devel
BuildRequires: libXdamage-devel
BuildRequires: libXfixes-devel
BuildRequires: libXft-devel
BuildRequires: libXrandr-devel
BuildRequires: libXrender-devel
BuildRequires: libXxf86vm-devel
BuildRequires: libsndfile-devel
BuildRequires: make
BuildRequires: pango-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: xorg-x11-proto-devel
BuildRequires: xorg-x11-xbitmaps
Requires:      dejavu-sans-fonts

%description
Enlightenment is a window manager for the X Window System that is
designed to be powerful, extensible, configurable and pretty darned
good looking! It is one of the more graphically intense window
managers.

Enlightenment goes beyond managing windows by providing a useful and
appealing graphical shell from which to work. It is open in design and
instead of dictating a policy, allows the user to define their own
policy, down to every last detail.

This package will install the Enlightenment window manager, development
release 16.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
for f in ChangeLog AUTHORS ; do
    mv $f $f.iso88591
    iconv -o $f -f iso88591 -t utf8 $f.iso88591
    rm -f $f.iso88591
done

%build
%configure \
    --enable-pango   \
    --enable-mans    \
    --enable-modules \
    --enable-dbus    \
    --enable-visibility-hiding
%make_build

%install
%make_install
chmod 0644 %{buildroot}%{_datadir}/%{name}/themes/winter/ABOUT/MAIN

# Vera -> DejaVu
rm -f %{buildroot}%{_datadir}/%{name}/fonts/COPYRIGHT.Vera
rm -f %{buildroot}%{_datadir}/%{name}/fonts/*.ttf
ln -s ../../fonts/dejavu/DejaVuSans.ttf %{buildroot}%{_datadir}/%{name}/fonts/normal.ttf
ln -s ../../fonts/dejavu/DejaVuSans-Bold.ttf %{buildroot}%{_datadir}/%{name}/fonts/bold.ttf

# Remove unwanted files
find %{buildroot}%{_libdir}/e16 -name lib*.la -delete
rm -rf %{buildroot}%{_datadir}/doc/%{name}

# Fix absolute symlink
rm %{buildroot}/%{_bindir}/starte16
ln -s ../share/e16/misc/starte16 %{buildroot}/%{_bindir}/starte16

%check
# Desktop file
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%find_lang %{name}
%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog COMPLIANCE
%doc docs/e16.html
%{_bindir}/e*
%{_bindir}/starte16
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/lib*.so
%{_datadir}/%{name}
%{_datadir}/xsessions/*
%{_datadir}/gnome-session/sessions/%{name}-gnome.session
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
