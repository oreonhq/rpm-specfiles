%global source0_hash 2e86c11ec99758332a880b010f6cb4a57414d848038b7915ddc052df0812ca51

Name:           berusky2
Version:        0.12
Release:        17%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
Summary:        Sokoban clone
Source:         http://www.anakreon.cz/download/%{name}-%{version}.tar.gz
Source1:        berusky2.appdata.xml
Source2:        berusky2.png
URL:            http://www.anakreon.cz/en/Berusky2.htm

Requires:       berusky2-data >= 0.12
BuildRequires:  gcc-c++
BuildRequires:  gcc
BuildRequires:  SDL-devel
BuildRequires:  SDL_image-devel
BuildRequires:  gtk2-devel
BuildRequires:  desktop-file-utils
BuildRequires:  freealut-devel
BuildRequires:  openal-soft-devel
BuildRequires:  libvorbis-devel
BuildRequires: make
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64 %{mips} riscv64

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
#Uncomment to produce a debug build
#OPT_FLAGS=$(echo "$RPM_OPT_FLAGS" | %{__sed} -e 's/-O2//')
#export CXXFLAGS=$OPT_FLAGS
#export CFLAGS=$OPT_FLAGS
%configure

make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

# Move documentation so it can get installed to the right place.
mkdir _tmpdoc
mv %{buildroot}%{_usr}/doc/%{name}/* _tmpdoc/
rm -f _tmpdoc/INSTALL

# Install ini file
mkdir -p %{buildroot}%{_var}/games/%{name}
install -pm 644 %{buildroot}/%{_datadir}/%{name}/berusky3d.ini \
                %{buildroot}%{_var}/games/%{name}

# Install icon and desktop file
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
cp %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps

desktop-file-install --dir %{buildroot}/%{_datadir}/applications \
                     --add-category X-Fedora %{buildroot}/%{_datadir}/%{name}/berusky2.desktop

# Remove directory that will be owned by data package.
rm -rf %{buildroot}/%{_datadir}/%{name}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata/
cp %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/appdata/

%files
%doc _tmpdoc/*
%{_bindir}/berusky2
%{_datadir}/applications/berusky2.desktop
%{_datadir}/icons/hicolor/128x128/apps/berusky2.png
%{_datadir}/appdata/berusky2.appdata.xml
%dir %{_var}/games/%{name}
%{_var}/games/%{name}/*

%changelog
%autochangelog
