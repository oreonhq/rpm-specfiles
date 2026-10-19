%global source0_hash f0c979fb35ec550a43246fc209add8f45ca550a382c94d6383bb3f01b1073799
Summary:        Game data files for Fish Fillets Next Generation
Name: fillets-ng-data
Version: 1.0.1
Release:        1%{?dist}
License: GPL-2.0-only
URL: http://fillets.sourceforge.net/
Source0:        http://downloads.sf.net/fillets/fillets-ng-data-%{version}.tar.gz
Patch0: fillets-ng-data-1.0.1-lua-5.2.patch
Patch1: fillets-ng-data-1.0.1-lua-invalid-string.patch
Patch2: fillets-ng-data-1.0.1-lua-cabin1-crash-fix.patch
Patch3: fillets-ng-data-1.0.1-lua-electromagnet-crash-fix.patch
Patch4: fillets-ng-data-1.0.1-lua-loadstring.patch
Patch5: fillets-ng-data-1.0.1-lua-engine-room-crash-fix.patch
Requires: gnu-free-sans-fonts
Requires: fillets-ng >= 1.0.1-10
%global fontlist font(freesans)
Requires: %{fontlist}
BuildArch: noarch
# oreon:deps
BuildRequires:  font(freesans)
BuildRequires:  fontconfig
# /oreon:deps
%description
Fish Fillets is strictly a puzzle game. The goal in every of the
seventy levels is always the same: find a safe way out. The fish utter
witty remarks about their surroundings, the various inhabitants of
their underwater realm quarrel among themselves or comment on the
efforts of your fish. The whole game is accompanied by quiet,
comforting music.

This package contains the data files required to run the game.

%prep

%setup -q
%patch -P0 -p0
%patch -P1 -p0
%patch -P2 -p0
%patch -P3 -p0
%patch -P4 -p0
%patch -P5 -p0

%build

%install
mkdir -p %{buildroot}%{_datadir}/fillets-ng
cp -a * %{buildroot}%{_datadir}/fillets-ng/
rm %{buildroot}%{_datadir}/fillets-ng/COPYING
rm -f %{buildroot}%{_datadir}/fillets-ng/font/copyright
for FONTFILE in %{buildroot}%{_datadir}/fillets-ng/font/*.ttf; do
    rm -f ${FONTFILE}
    ln -s "$(fc-match -f '%%{file}' 'Free Sans:Bold')" "${FONTFILE}"
done
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
