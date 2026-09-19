%global source0_hash 0589b3928fc474b8fdcbb4b0128f2f72db57bbbc8846cdc96563d68a9d727d0c

Name:           abe
Version:        1.1
Release:        56%{?dist}

Summary:        Scrolling, platform-jumping, ancient pyramid exploring game
License:        GPL-1.0-or-later
URL:            http://abe.sourceforge.net/
Source0:        http://downloads.sourceforge.net/abe/%{name}-%{version}.tar.gz
Source1:        %{name}-icons.tar.xz
Source2:        %{name}.appdata.xml
# Enable changing the video settings.  Sent upstream 2 Apr 2006:
# https://sourceforge.net/tracker/?func=detail&aid=1463202&group_id=70141&atid=526743
Patch0:         %{name}-1.1-settings.patch
# Fix a double free() bug.  Sent upstream 15 Mar 2011:
# https://sourceforge.net/tracker/?func=detail&aid=3214269&group_id=70141&atid=526745
Patch1:         %{name}-1.1-doublefree.patch
# Fix an incorrect printf format specifier.  Sent upstream 15 Mar 2011:
# https://sourceforge.net/tracker/?func=detail&aid=3214270&group_id=70141&atid=526745
Patch2:         %{name}-1.1-format.patch
# Add support for aarch64.  Sent upstream 25 Mar 2013:
# https://sourceforge.net/tracker/?func=detail&aid=3609029&group_id=70141&atid=526743
Patch3:         %{name}-1.1-aarch64.patch
# Fix build failure with -Werror=format-security
Patch4:         %{name}-1.1-format-security.patch
Patch5:         %{name}-1.1-configure-c99.patch
Patch6:         %{name}-finishdrawmap.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libXi-devel
BuildRequires:  libXmu-devel
BuildRequires:  SDL-devel
BuildRequires:  SDL_mixer-devel
BuildRequires: make

Requires:       hicolor-icon-theme

%description
A scrolling, platform-jumping, key-collecting, ancient pyramid exploring game,
vaguely in the style of similar games for the Commodore+4.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0
%patch -P1
%patch -P2
%patch -P3
%patch -P4
%patch -P5
%patch -P6

# Fix the FSF's address
sed 's/59 Temple Place, Suite 330, Boston, MA  02111-1307/51 Franklin Street, Suite 500, Boston, MA  02110-1335/' COPYING > COPYING.new
touch -r COPYING COPYING.new
mv -f COPYING.new COPYING

%build
%configure --with-data-dir=%{_datadir}/%{name}
sed -i "s|^CFLAGS =.*|CFLAGS = ${RPM_OPT_FLAGS} \$\(SDL_CFLAGS\)|" src/Makefile
%make_build

%install
%make_install

# make install does not copy the game data files.
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{name}
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/appdata/
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/applications/
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/
cp -p -r images maps sounds $RPM_BUILD_ROOT/%{_datadir}/%{name}
tar xJf %{SOURCE1} -C $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT/%{_datadir}/appdata/

cat << EOF > %{name}.desktop
[Desktop Entry]
Name=Abe
Comment="Abe's Amazing Adventure"
Exec=abe
Icon=abe
Terminal=false
Type=Application
Categories=Game;ArcadeGame;
EOF

desktop-file-install --dir $RPM_BUILD_ROOT/%{_datadir}/applications/ %{name}.desktop

%files
%doc README
%license COPYING
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
%autochangelog
