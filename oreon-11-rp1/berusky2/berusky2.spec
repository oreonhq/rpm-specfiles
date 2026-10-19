%global source0_hash 2e86c11ec99758332a880b010f6cb4a57414d848038b7915ddc052df0812ca51
Name:           berusky2
Version:        0.12
Release:        17%{?dist}
License:        GPL-2.0-or-later
Summary:        Sokoban clone
Source0:        http://www.anakreon.cz/download/%{name}-%{version}.tar.gz
Source1:        berusky2.appdata.xml
Source2:        berusky2.png
URL:            http://www.anakreon.cz/en/Berusky2.htm
Requires:       berusky2-data >= 0.12
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64 %{mips} riscv64
# oreon:deps
BuildRequires:  SDL-devel
BuildRequires:  SDL_image-devel
BuildRequires:  desktop-file-utils
BuildRequires:  freealut-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gtk2-devel
BuildRequires:  libvorbis-devel
BuildRequires:  make
BuildRequires:  openal-soft-devel
# /oreon:deps
%description
Berusky 2 is a game that challenges your visual/spatial thinking
and ability to find a way to resolve a logic task. Using five bugs,
you'll go through an adventure full of various puzzles spread across
nine episodes. Individual episodes differ in appearance and difficulty,
which increases throughout the game.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%configure
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
mkdir _tmpdoc
mv %{buildroot}%{_usr}/doc/%{name}/* _tmpdoc/
rm -f _tmpdoc/INSTALL
mkdir -p %{buildroot}%{_var}/games/%{name}
install -pm 644 %{buildroot}/%{_datadir}/%{name}/berusky3d.ini \
                %{buildroot}%{_var}/games/%{name}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
cp %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
desktop-file-install --dir %{buildroot}/%{_datadir}/applications \
                     --add-category X-Fedora %{buildroot}/%{_datadir}/%{name}/berusky2.desktop
rm -rf %{buildroot}/%{_datadir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata/
cp %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/appdata/
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
