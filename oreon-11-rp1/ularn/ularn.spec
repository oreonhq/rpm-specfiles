%global source0_hash 2d6c2a7e1d6fd0ac9f1ec38e4e2be25d6a1cf8883779aea9780ea0a76c83761a

Name:           ularn
Version:        1.5p4
Release:        48%{?dist}
Summary:        Simple roguelike game

License:        GPL-1.0-or-later
URL:            http://www.ularn.org
Source0:        http://downloads.sourceforge.net/ularn/Ularn-1.5ishPL4.tar.gz
Source1:        config.sh.in
Source2:        ularn.desktop
Source3:        ularn.png
Patch0:         ularn-build.patch
Patch1:         ularn-euid.patch
Patch2:         ularn-datadir.patch
Patch3:         ularn-drop-setgid.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  ncurses-devel
BuildRequires:  desktop-file-utils
Requires:       ncompress

%description
A text-based roguelike game based on the original Larn.  Travel through
dungeons collecting weapons, killing monsters, in order to find and sell the
Eye of Larn to save your sick daughter.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Ularn

# The configure script for this package is interactive.  However, it
# produces a config.sh script that can be customized if necessary.
# a pre-built config.sh script is used to avoid running an interactive
# configure script, but still must be customized slightly.
sed -e 's#@bindir@#%{_bindir}#' \
        -e 's#@datadir@#%{_datadir}#' \
        -e 's#@var@#%{_var}#' < %{SOURCE1} > config.sh
chmod +x config.h.SH
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1

%build
# This package requires C89 compatibility mode (bug 2155503).
%global build_type_safety_c 0

# Keep track of where we are.  Some of the configuration scripts change
# the current working directory.
builddir=`pwd`
. ./config.h.SH
${builddir}/Makefile.u.SH
cd ${builddir}
mv Makefile.u Makefile
CC="gcc $RPM_OPT_FLAGS -fcommon -std=gnu17" make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_var}/games
touch $RPM_BUILD_ROOT/%{_var}/games/Ularn-scoreboard

desktop-file-install \
        --dir ${RPM_BUILD_ROOT}%{_datadir}/applications         \
        %{SOURCE2}
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/32x32/apps/
install -p -m 644 %{SOURCE3} $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/32x32/apps/

# Note that the game is setgid games, and the score file is group writable.
%files
%attr(2755,root,games) %{_bindir}/Ularn
%{_datadir}/%{name}
%config(noreplace) %attr (0664,root,games) %{_var}/games/Ularn-scoreboard
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%doc README README.spoilers CHANGES.text Ularnopts
%license GPL

%changelog
%autochangelog
