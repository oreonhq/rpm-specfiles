%global source2_hash ed9c1fa927fcd878cce955fb0bdc586876ee1ae234666be75c3bbd6e5b2a094b
%global source0_hash ed9c1fa927fcd878cce955fb0bdc586876ee1ae234666be75c3bbd6e5b2a094b
%global wtf_ver 20230906
Summary:        Collection of text-based games
Name: bsd-games
Version: 2.17
Release:        84%{?dist}
License: LicenseRef-Callaway-BSD AND LicenseRef-Callaway-BSD-with-advertising
URL: ftp://metalab.unc.edu/pub/Linux/games/
Source0:        ftp://metalab.unc.edu/pub/Linux/games/bsd-games-%{version}.tar.gz
Source1: config.params
Source2: https://downloads.sourceforge.net/bsdwtf/wtf-%{wtf_ver}.tar.gz
Patch0: bsd-games-2.17-debian.patch
Patch1: bsd-games-2.17-ospeed.patch
Patch2: bsd-games-2.17-getline.patch
Patch3: bsd-games-2.17-utmpstruct.patch
Patch4: bsd-games-2.17-setresgid.patch
Patch5: bsd-games-2.17-tetrisgid.patch
Patch6: bsd-games-2.17-hackgid.patch
Patch7: bsd-games-2.17-phantasiagid.patch
Patch8: bsd-games-2.17-monop-rename.patch
Patch9: bsd-games-2.17-banner-rename.patch
Patch10: bsd-games-2.17-stdio-c++.patch
Patch11: bsd-games-2.17-nolibtermcap.patch
Patch12: bsd-games-2.17-tetris-rename.patch
Patch13: bsd-games-2.17-gcc43.patch
Patch14: bsd-games-2.17-bogglewords.patch
Patch16: bsd-games-2.17-backgammonsize.patch
Patch17: bsd-games-2.17-adventurecrc.patch
Patch18: bsd-games-2.17-wtfrpm.patch
Patch19: bsd-games-2.17-adventureinit.patch
Patch20: bsd-games-2.17-backgammonrecursion.patch
Patch21: bsd-games-2.17-huntversion.patch
Patch22: bsd-games-2.17-getrandom.patch
Patch23: bsd-games-2.17-printf.patch
Patch24: bsd-games-2.17-printw.patch
Patch25: bsd-games-c99.patch
Patch26: atc.patch
Patch27: boggle_fread_chk.patch
# oreon:deps
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  libfl-static
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  words
# /oreon:deps
%description
Bsd-games includes adventure, arithmetic, atc, backgammon, battlestar,
bcd, caesar, canfield, cfscores, cribbage, go-fish, gomoku,
hunt, mille, mpoly, morse, number, phantasia, pig, pom, ppt, primes,
quiz, rain, random, robots, rot13, sail, snake, snscore, teachgammon,
bsd-fbg, trek, worm, worms and wump.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -a2
install -p -m 755 %{SOURCE1} .
%patch -P0 -p1 -b .debian
%patch -P1 -p1 -b .ospeed
%patch -P2 -p1 -b .getline
%patch -P3 -p1 -b .utmpstruct
%patch -P4 -p1 -b .setresgid
%patch -P5 -p1 -b .tetrisgid
%patch -P6 -p1 -b .hackgid
%patch -P7 -p1 -b .phantasiagid
%patch -P8 -p1 -b .monop.rename
%patch -P9 -p0 -b .banner.rename
%patch -P10 -p0 -b .cplusplus
%patch -P11 -p0 -b .nolibtermcap
%patch -P12 -p0 -b .tetris.rename
%patch -P13 -p1 -b .gcc43
%patch -P14 -p0 -b .wordlimit
%patch -P16 -p0 -b .backgammonsize
%patch -P17 -p0 -b .adventurecrc
pushd wtf-%{wtf_ver}
%patch -P18 -p1 -b .wtfrpm
popd
%patch -P19 -p0 -b .adventureinit
%patch -P20 -p1 -b .backgammonrecursion
%patch -P21 -p1 -b .huntversion
%patch -P22 -p1 -b .getrandom
%patch -P23 -p1 -b .printf
%patch -P24 -p1 -b .printw
%patch -P25 -p1 -b .c99
%patch -P26 -p1 -b .atc
%patch -P27 -p1 -b .fread_chk

# Create a sysusers.d config file
cat >bsd-games.sysusers.conf <<EOF
g gamehack -
g gamesail -
g gamephant -
EOF

%build

sed -i.bak -e "s#@DESTDIR@#$RPM_BUILD_ROOT#" \
    -e "s#@bindir@#%{_bindir}#" \
    -e "s#@docdir@#%{_docdir}#" \
    -e "s#@sbindir@#%{_sbindir}#" \
    -e "s#@datadir@#%{_datadir}#" \
    -e "s#@libdir@#%{_libdir}#" \
    -e "s#@mandir@#%{_mandir}#" \
    -e "s#@var@#%{_var}#" \
    -e "s#@RPM_OPT_FLAGS@#$RPM_OPT_FLAGS#" \
    config.params 
./configure
%make_build RPM_OPT_FLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE"
cp hunt/README README.hunt
%install
rm -rf $RPM_BUILD_ROOT
%make_install RPM_BUILD_ROOT="$RPM_BUILD_ROOT"
mv $RPM_BUILD_ROOT/%{_bindir}/monop $RPM_BUILD_ROOT/%{_bindir}/mpoly
mv $RPM_BUILD_ROOT/%{_mandir}/man6/monop.6.gz $RPM_BUILD_ROOT/%{_mandir}/man6/mpoly.6.gz
mv $RPM_BUILD_ROOT/%{_bindir}/banner $RPM_BUILD_ROOT/%{_bindir}/vert-banner
mv $RPM_BUILD_ROOT/%{_mandir}/man6/banner.6.gz $RPM_BUILD_ROOT/%{_mandir}/man6/vert-banner.6.gz
mv $RPM_BUILD_ROOT/%{_bindir}/tetris-bsd $RPM_BUILD_ROOT/%{_bindir}/bsd-fbg
mv $RPM_BUILD_ROOT/%{_mandir}/man6/tetris-bsd.6.gz $RPM_BUILD_ROOT/%{_mandir}/man6/bsd-fbg.6.gz
rm -f $RPM_BUILD_ROOT/%{_docdir}/trek.me
pushd wtf-%{wtf_ver}
install -p -m 0755 wtf $RPM_BUILD_ROOT%{_bindir}/
gzip wtf.6
install -p -m 0644 wtf.6.gz $RPM_BUILD_ROOT%{_mandir}/man6/
install -p -m 0644 acronyms* $RPM_BUILD_ROOT%{_datadir}/misc/
mv $RPM_BUILD_ROOT%{_datadir}/misc/acronyms-o.real $RPM_BUILD_ROOT%{_datadir}/misc/acronyms-o
popd
install -m0644 -D bsd-games.sysusers.conf %{buildroot}%{_sysusersdir}/bsd-games.conf
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
