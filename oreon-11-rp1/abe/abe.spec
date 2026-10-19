%global source0_hash dfc4ea74c04c92175abc5c9d65cfa6aad218209854d87d87758878e303b677f7
Name:           abe
Version:        1.1
Release:        56%{?dist}
Summary:        Scrolling, platform-jumping, ancient pyramid exploring game
License:        GPL-1.0-or-later
URL:            http://abe.sourceforge.net/
Source0:        http://downloads.sourceforge.net/abe/%{name}-%{version}.tar.gz
Source1:        %{name}-icons.tar.xz
Source2:        %{name}.appdata.xml
Patch0:         %{name}-1.1-settings.patch
Patch1:         %{name}-1.1-doublefree.patch
Patch2:         %{name}-1.1-format.patch
Patch3:         %{name}-1.1-aarch64.patch
Patch4:         %{name}-1.1-format-security.patch
Patch5:         %{name}-1.1-configure-c99.patch
Patch6:         %{name}-finishdrawmap.patch
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  SDL-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libXi-devel
BuildRequires:  libXmu-devel
BuildRequires:  make
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
