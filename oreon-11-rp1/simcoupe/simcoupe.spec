%global source0_hash bdd1360fea39a4a6ef42eb64e96c2556b00bb7aa5a77afdda84ad0d43e404773

Name:           simcoupe
Version:        1.0
Release:        38%{?dist}
Summary:        SAM Coupe emulator (spectrum compatible)
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.simcoupe.org
Source0:        http://downloads.sourceforge.net/%{name}/SimCoupe-%{version}.tar.gz
Source1:        B-DOS-License.txt
Patch0:         simcoupe-1.0-userpmopts.patch
Patch1:         simcoupe-1.0-saasound.patch
Patch2:         simcoupe-1.0-no-builtin-rom.patch
BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  SAASound-devel SDL-devel zlib-devel
BuildRequires:  ImageMagick desktop-file-utils
Requires:       samcoupe-rom hicolor-icon-theme

%description
SimCoupe emulates an 8bit Z80 based home computer, released in 1989 by Miles
Gordon Technology. The SAM Coupe was largely spectrum compatible, with much
improved hardware

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n SimCoupe
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
# Clean up bundled SAASound to avoid accidentally building against it.
rm -f Extern/SAASound.h Extern/SAASound.cpp
cp -a %{SOURCE1} .

%build
pushd SDL
make %{?_smp_mflags} CFLAGSRPM="%{optflags}"
popd

#Build icon image
convert SDL/SimCoupe.bmp -transparent '#ffffff' %{name}.png

#Build desktop icon
cat >%{name}.desktop<<EOF
[Desktop Entry]
Encoding=UTF-8
Name=SimCoupe
GenericName=SAM Coupe Emulator
Comment=%{summary}
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;Emulator;
EOF

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
install -pm 0755 SDL/%{name} %{buildroot}%{_bindir}
install -pm 0644 SDL/SimCoupe.bmp %{buildroot}%{_datadir}/%{name}
install -pm 0644 %{name}.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps

desktop-file-install \
%if 0%{?fedora} && 0%{?fedora} < 19
    --vendor fedora \
%endif
    --dir %{buildroot}%{_datadir}/applications \
    %{name}.desktop

%files
%doc ChangeLog.txt License.txt SimCoupe.txt B-DOS-License.txt
%{_bindir}/%{name}
%if 0%{?fedora} && 0%{?fedora} < 19
%{_datadir}/applications/fedora-%{name}.desktop
%else
%{_datadir}/applications/%{name}.desktop
%endif
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/%{name}

%changelog
%autochangelog
