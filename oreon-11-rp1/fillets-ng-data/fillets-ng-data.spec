%global source0_hash none

Summary: Game data files for Fish Fillets Next Generation
Name: fillets-ng-data
Version: 1.0.1
Release: 30%{?dist}
# The GPLv2 is included and nothing indicates "any later version". Exceptions :
# - images/menu/flags/ is Public Domain
# - font/ is GPLv2+ (taken from "freefont")
# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
URL: http://fillets.sourceforge.net/
Source: http://downloads.sf.net/fillets/fillets-ng-data-%{version}.tar.gz
# http://sourceforge.net/p/fillets/bugs/7/
Patch0: fillets-ng-data-1.0.1-lua-5.2.patch
Patch1: fillets-ng-data-1.0.1-lua-invalid-string.patch
Patch2: fillets-ng-data-1.0.1-lua-cabin1-crash-fix.patch
Patch3: fillets-ng-data-1.0.1-lua-electromagnet-crash-fix.patch
Patch4: fillets-ng-data-1.0.1-lua-loadstring.patch
Patch5: fillets-ng-data-1.0.1-lua-engine-room-crash-fix.patch
# For the TTF file used, instead of duplicating it 3 times here
Requires: gnu-free-sans-fonts
Requires: fillets-ng >= 1.0.1-10
%global fontlist font(freesans)
Requires: %{fontlist}
BuildRequires: fontconfig
BuildRequires: %{fontlist}
BuildArch: noarch

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
# Move along, nothing to see here! :-)

%install
mkdir -p %{buildroot}%{_datadir}/fillets-ng
cp -a * %{buildroot}%{_datadir}/fillets-ng/
rm %{buildroot}%{_datadir}/fillets-ng/COPYING

# Replace bundled copy of the fonts with symlinks to the original one
rm -f %{buildroot}%{_datadir}/fillets-ng/font/copyright
for FONTFILE in %{buildroot}%{_datadir}/fillets-ng/font/*.ttf; do
    rm -f ${FONTFILE}
    ln -s "$(fc-match -f '%%{file}' 'Free Sans:Bold')" "${FONTFILE}"
done

%files
%dir %{_datadir}/fillets-ng/
%license COPYING
%{_datadir}/fillets-ng/font/
%{_datadir}/fillets-ng/images/
%{_datadir}/fillets-ng/music/
%{_datadir}/fillets-ng/script/
%{_datadir}/fillets-ng/sound/
%doc %{_datadir}/fillets-ng/doc/

%changelog
%autochangelog
