%global source0_hash 957bb498b2df717f0ad449a8147d2fa7670796ec91c214cbd3f6d6e40c77ea62

Summary: Front-end for CD rippers and Ogg Vorbis encoders
Name: grip
Version: 4.2.4
Release: %autorelease
Epoch: 1
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
Source0: http://downloads.sourceforge.net/grip/grip-%{version}.tar.gz
# This fixes code which is not used right now; still keeping it
Patch0: grip-64bit-fix.patch
URL: https://sourceforge.net/projects/grip/
Requires: vorbis-tools
%if 0%{?fedora}
Recommends: lame
%endif
BuildRequires: meson
BuildRequires: gcc gcc-c++
BuildRequires: curl-devel
BuildRequires: gettext
BuildRequires: id3lib-devel
BuildRequires: cdparanoia-devel
BuildRequires: pkgconfig(gtk+-2.0)
BuildRequires: desktop-file-utils

%description
Grip is a GTK+ based front-end for CD rippers (such as cdparanoia and
cdda2wav) and Ogg Vorbis encoders. Grip allows you to rip entire tracks or
just a section of a track. Grip supports the CDDB protocol for
accessing track information on disc database servers.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1

%build

pushd po
iconv -f koi8-r -t utf-8 ru.po > ru.po.tmp
mv ru.po.tmp ru.po

sed -i 's/Content-Type: text\/plain; charset=koi8-r\\n/Content-Type: text\/plain; charset=utf-8\\n/' ru.po
popd

%meson
%meson_build

%install
%meson_install

cat >> %{buildroot}%{_datadir}/applications/grip.desktop << EOF
StartupWMClass=Grip
EOF

desktop-file-install \
	--dir $RPM_BUILD_ROOT/%{_datadir}/applications \
	--delete-original \
	--add-category X-AudioVideoImport \
	--add-category AudioVideo \
	$RPM_BUILD_ROOT%{_datadir}/applications/grip.desktop

# I think this is a KDE specific path; delete for now - until understood
rm -rf $RPM_BUILD_ROOT%{_datadir}/apps/

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc README ChangeLog CREDITS AUTHORS TODO
%{_bindir}/grip
%{_datadir}/pixmaps/grip.png
%{_datadir}/pixmaps/griptray.png
%{_datadir}/gnome/help/grip
%{_datadir}/applications/*
%{_datadir}/solid/actions/grip-audiocd.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_mandir}/man1/*

%changelog
%autochangelog
