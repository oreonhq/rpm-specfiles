%global source0_hash none

%global waddir  %{_datadir}/doom

Name:           freedoom

Version:        0.13.0
Release:        5%{?dist}
Summary:        Doom styled first person shooter game

License:        BSD-3-Clause
URL:            https://freedoom.github.io/
Source0:        https://github.com/freedoom/freedoom/releases/download/v%{version}/freedoom-%{version}.zip
Source1:        freedoom1.desktop
Source2:        freedoom2.desktop
Source3:        freedoom.png
Source4:        freedoom1.appdata.xml
Source5:        freedoom2.appdata.xml

BuildArch:      noarch
BuildRequires:  desktop-file-utils libappstream-glib
Requires:       prboom hicolor-icon-theme

%description
Freedoom: Phase 1 is a Doom styled first person shooter game using the
Doom engine, featuring Four chapters, nine levels each, totalling 36
levels.

There is a massive back catalog, spanning over two decades, containing
thousands of Doom levels and other modifications (“mods”) made by fans
of the original Doom game. Freedoom aims to be compatible with these and
allows most to be played without the original Doom datafiles.
Freedoom: Phase 1 aims for compatibility with The Ultimate Doom,
also known as plain Doom or Doom 1. 

%package -n     freedoom2
Summary:        Doom2 styled first person shooter game
Requires:       prboom hicolor-icon-theme

%description -n freedoom2
Freedoom: Phase 2 is a Doom2 styled first person shooter game using the
Doom engine. Freedoom: Phase 2 has 32 levels in one long chapter,
featuring extra monsters and a double-barrelled shotgun.

There is a massive back catalog, spanning over two decades, containing
thousands of Doom levels and other modifications (“mods”) made by fans
of the original Doom game. Freedoom aims to be compatible with these and
allows most to be played without the original Doom datafiles.
Freedoom: Phase 2 aims for compatibility with Doom II and Final Doom.

%prep
%setup -q

%build
# Game data files.  Nothing to build!

%install
mkdir -p %{buildroot}/%{waddir}
install -p -m 0644 freedoom1.wad freedoom2.wad %{buildroot}/%{waddir}
desktop-file-install --dir %{buildroot}/%{_datadir}/applications %{SOURCE1}
desktop-file-install --dir %{buildroot}/%{_datadir}/applications %{SOURCE2}
mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/48x48/apps/
install -p -m 644 %{SOURCE3} %{buildroot}/%{_datadir}/icons/hicolor/48x48/apps/
mkdir -p %{buildroot}%{_datadir}/appdata
install -p -m 644 %{SOURCE4} %{SOURCE5} %{buildroot}%{_datadir}/appdata
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/*.xml
ln -s /usr/share/doom/freedoom2.wad %{buildroot}%{waddir}/freedoom.wad
# crete  cmdline launchers from desktop commands
mkdir -p %{buildroot}/%{_bindir}
echo "#!%{_bindir}/bash" > %{buildroot}/%{_bindir}/%{name}1
echo "#!%{_bindir}/bash" > %{buildroot}/%{_bindir}/%{name}2
cat  %{SOURCE1} | grep "Exec" | sed "s/Exec.//" >> %{buildroot}/%{_bindir}/%{name}1
cat  %{SOURCE2} | grep "Exec" | sed "s/Exec.//" >> %{buildroot}/%{_bindir}/%{name}2
chmod 755 %{buildroot}/%{_bindir}/%{name}1
chmod 755 %{buildroot}/%{_bindir}/%{name}2

%files
%doc README.html CREDITS.txt
%license COPYING.txt
%{waddir}/%{name}1.wad
%{_datadir}/appdata/%{name}1.appdata.xml
%{_datadir}/applications/%{name}1.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_bindir}/%{name}1

%files -n freedoom2
%doc README.html CREDITS.txt
%license COPYING.txt
%{waddir}/%{name}.wad
%{waddir}/%{name}2.wad
%{_datadir}/appdata/%{name}2.appdata.xml
%{_datadir}/applications/%{name}2.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_bindir}/%{name}2

%changelog
%autochangelog
