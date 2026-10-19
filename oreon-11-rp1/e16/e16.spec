%global source0_hash 06b6ef593a1305170d9cb70714ea15b054a84a89f4d507c2a5d4d74da263de0d
Summary:        The Enlightenment window manager, DR16
Name:          e16
Version:       1.0.32
Release:        1%{?dist}
License:       LicenseRef-Callaway-MIT-with-advertising AND GPL-2.0-or-later
URL:           http://www.enlightenment.org/
Source0:        http://downloads.sourceforge.net/enlightenment/e16-%{version}.tar.xz
Patch:         0001-backgrounds-Save-backgrounds-after-modifying-one-in-.patch
Requires:      dejavu-sans-fonts
# oreon:deps
BuildRequires:  dbus-devel
BuildRequires:  desktop-file-utils
BuildRequires:  freetype-devel
BuildRequires:  gcc
BuildRequires:  imlib2-devel
BuildRequires:  libSM-devel
BuildRequires:  libXcomposite-devel
BuildRequires:  libXdamage-devel
BuildRequires:  libXfixes-devel
BuildRequires:  libXft-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXrender-devel
BuildRequires:  libXxf86vm-devel
BuildRequires:  libsndfile-devel
BuildRequires:  make
BuildRequires:  pango-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  xorg-x11-proto-devel
BuildRequires:  xorg-x11-xbitmaps
# /oreon:deps
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
rm -f %{buildroot}%{_datadir}/%{name}/fonts/COPYRIGHT.Vera
rm -f %{buildroot}%{_datadir}/%{name}/fonts/*.ttf
ln -s ../../fonts/dejavu/DejaVuSans.ttf %{buildroot}%{_datadir}/%{name}/fonts/normal.ttf
ln -s ../../fonts/dejavu/DejaVuSans-Bold.ttf %{buildroot}%{_datadir}/%{name}/fonts/bold.ttf
find %{buildroot}%{_libdir}/e16 -name lib*.la -delete
rm -rf %{buildroot}%{_datadir}/doc/%{name}
rm %{buildroot}/%{_bindir}/starte16
ln -s ../share/e16/misc/starte16 %{buildroot}/%{_bindir}/starte16
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
%find_lang %{name}
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
