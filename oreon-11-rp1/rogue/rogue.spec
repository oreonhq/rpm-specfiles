%global source0_hash aea2204f046576e06ba1bc53808cc193306e4a694a92a573e739289117f91a41

Name:             rogue
Version:          5.4.5
Release:          44%{?dist}
Summary:          The original graphical adventure game
License:          BSD-3-Clause
# TODO: Fix the source url
Source0:          https://github.com/phs/rogue/archive/v5.4.4/%{name}-5.4.4.tar.gz
URL:              https://github.com/phs/rogue
Patch0:           rogue-5.4.4-to-5.4.5.patch
Patch1:           rogue-5.4.5-writesave.patch
Patch2:           rogue-5.4.5-backspace.patch
Patch3:           rogue-5.4.5-ncurses.patch
Patch4:           rogue-5.4.5-setgroups.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:      %{ix86}

BuildRequires:    binutils
BuildRequires:    coreutils
BuildRequires:    desktop-file-utils
BuildRequires:    gcc
BuildRequires:    hostname
BuildRequires:    make
BuildRequires:    ncurses-devel
BuildRequires:    sed

%description
The one, the only, the original graphical adventure game that spawned
an entire genre.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-5.4.4
%patch -P0 -p1
%patch -P1 -p0
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1

%build
CFLAGS='%{build_cflags} -std=gnu17'
%configure \
    --enable-setgid=games \
    --enable-scorefile=%{_localstatedir}/games/roguelike/rogue54.scr \
    --enable-lockfile=%{_localstatedir}/games/roguelike/rogue54.lck \
    --docdir=%{_docdir}/%{name}
%make_build

%install
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_docdir}/rogue
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man6
mkdir -p $RPM_BUILD_ROOT/%{_localstatedir}/games/roguelike
%make_install
install -D -p -m644 \
    %{name}.png %{buildroot}/%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
desktop-file-install \
    --dir %{buildroot}%{_datadir}/applications %{name}.desktop

%files
%license LICENSE.TXT
%exclude %{_docdir}/%{name}/LICENSE.TXT
%doc %{_docdir}/%{name}
%attr(2755,games,games) %{_bindir}/%{name}
%{_mandir}/man6/%{name}.*
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%dir %attr(0775,games,games) %{_localstatedir}/games/roguelike
%config(noreplace) %attr(0664,games,games) %{_localstatedir}/games/roguelike/%{name}54.scr

%changelog
%autochangelog
