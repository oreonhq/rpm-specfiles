%global source0_hash 8382218ae37669e457fd552bf4690ad3b2b91d8a52701655a457e191d3da4e74

%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}
%global version_data 1.7

Summary:        Sokoban clone
Name:           berusky
Version:        1.7.1
Release:        34%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
Source:         http://www.anakreon.cz/download/%{name}-%{version}.tar.gz
Source1:        berusky.desktop
Source2:        berusky.png
Source3:        berusky.appdata.xml
Source4:        http://www.anakreon.cz/download/%{name}-data-%{version_data}.tar.gz
Source5:        berusky.ini.in
Patch1:         berusky-1.7.1-sdl-build.patch
Patch2:         berusky-1.7.1-data-dir.patch
Patch3:         berusky-1.7.1-events-num.patch
Patch4:         berusky-gcc11-build.patch
URL:            http://www.anakreon.cz/?q=node/1
Requires:       SDL SDL_image
Obsoletes:      berusky-data
Conflicts:      berusky-data
BuildRequires:  gcc-c++
BuildRequires:  gcc
BuildRequires:  SDL-devel SDL_image-devel desktop-file-utils
BuildRequires:  gtk2-devel
BuildRequires:  autoconf
BuildRequires: make

%description
Berusky is a 2D logic game based on an ancient puzzle named Sokoban.

An old idea of moving boxes in a maze has been expanded with new logic
items such as explosives, stones, special gates and so on.
In addition, up to five bugs can cooperate and be controlled by the player.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version} -b 4
%patch -P1 -p1 -b .sdl-build
%patch -P2 -p1 -b .data-dir
%patch -P3 -p1 -b .events-num
%patch -P4 -p1 -b .build

%build
export CXXFLAGS="-std=c++14 $RPM_OPT_FLAGS"
autoconf
%configure

make %{?_smp_mflags}

%install
%make_install

mkdir -p %{buildroot}%{_pkgdocdir}
mv %{buildroot}%{_prefix}/doc/berusky/* %{buildroot}%{_pkgdocdir}

rm -rf %{buildroot}/%{_datadir}/%{name}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
cp %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata/
cp %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/appdata/

# Game data install
cd ../%{name}-data-%{version_data}
mkdir -p %{buildroot}%{_datadir}/%{name}

cp -r GameData %{buildroot}%{_datadir}/%{name}
cp -r Graphics %{buildroot}%{_datadir}/%{name}
cp -r Levels   %{buildroot}%{_datadir}/%{name}
cp README   %{buildroot}%{_datadir}/%{name}
cp COPYING  %{buildroot}%{_datadir}/%{name}

mkdir -p %{buildroot}%{_datadir}/%{name}
%{__sed} -e 's,/__PREFIX__,%{_prefix},g' %{SOURCE5} > %{buildroot}%{_datadir}/%{name}/%{name}.ini

%files
%{_pkgdocdir}
%exclude %{_pkgdocdir}/INSTALL
%exclude %{_pkgdocdir}/NEWS
%{_bindir}/berusky
%{_datadir}/applications/berusky.desktop
%{_datadir}/icons/hicolor/128x128/apps/berusky.png
%{_datadir}/appdata/berusky.appdata.xml
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*

%changelog
%autochangelog
