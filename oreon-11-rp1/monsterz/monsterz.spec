%global source0_hash 50828b8fa26d107bcc2bd134328f83c905b9f5e124846bdf239daf0eed34973d

Name:           monsterz
Version:        0.7.1
Release:        40%{?dist}
Summary:        Puzzle game, similar to Bejeweled or Zookeeper
License:        WTFPL
URL:            http://sam.zoy.org/monsterz/
Source0:        http://sam.zoy.org/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}.score
Patch0:         %{name}-0.7.1-userpmopts.patch
Patch1:         %{name}-0.7.1-64bitfix.patch
Patch2:         %{name}-0.7.1-blit-crash.patch
Patch3:         %{name}-0.7.1-py3.patch
BuildRequires: make
BuildRequires:  gcc
BuildRequires:  desktop-file-utils
BuildRequires:  python3-devel
Requires:       python3-pygame
Requires:       hicolor-icon-theme
Provides:       %{name}-data = %{version}-%{release}
Obsoletes:      %{name}-data < 0.7.1

%description
Monsterz is a little arcade puzzle game, similar to the famous Bejeweled or
Zookeeper. The goal of the game is to create rows of similar monsters, either
horizontally or vertically. The only allowed move is the swap of two adjacent
monsters, on the condition that it creates a row of three or more. When
alignments are cleared, pieces fall from the top of the screen to fill the
board again. Chain reactions earn you even more points.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p0
%patch -P3 -p1
%py3_shebang_fix .

%build
make %{?_smp_mflags} prefix=%{_usr} datadir=%{_datadir} pkgdatadir=%{_datadir}/%{name} CFLAGS="%{optflags}"

# Build desktop icon
cat >%{name}.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=Monsterz
GenericName=Monsterz Puzzle Game
Comment=%{summary}
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;StrategyGame;
EOF

%install
# Bypass make install as it requires root priviledges and the SRPM
# may not necessarily be built as root
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/{applications,icons/hicolor/64x64/apps}
mkdir -p %{buildroot}%{_datadir}/%{name}/{graphics,sound}
mkdir -p %{buildroot}%{_var}/games
install -pm0755 %{name} %{buildroot}%{_bindir}
install -pm0755 %{name}.py %{buildroot}%{_datadir}/%{name}
cp -a graphics/* %{buildroot}%{_datadir}/%{name}/graphics
cp -a sound/* %{buildroot}%{_datadir}/%{name}/sound

install -pm0664 %{SOURCE1} %{buildroot}%{_var}/games/%{name}

desktop-file-install \
                     --dir %{buildroot}%{_datadir}/applications \
                     %{name}.desktop

install -pm0644 graphics/icon.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/%{name}.png

%files
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%{_datadir}/%{name}
%attr(2755,root,games) %{_bindir}/%{name}
%attr(-,root,games) %config(noreplace) %{_var}/games/%{name}
%license COPYING
%doc AUTHORS README TODO

%changelog
%autochangelog
