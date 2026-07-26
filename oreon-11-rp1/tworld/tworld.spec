%global source0_hash bb867a05e18613260ffad597d8afef8210687495746857a7ad00ef0f2126e12a

Name:	 tworld
%global fullname Tile World

Version: 1.3.2
Release: 26%{?dist}
Summary: Intellectually engaging puzzle game

License: GPL-2.0-or-later
URL:     http://www.muppetlabs.com/~breadbox/software/tworld/
Source0: http://www.muppetlabs.com/~breadbox/pub/software/tworld/tworld-%{version}-CCLPs.tar.gz	

Source1: tworld-icon-16px.png
Source2: tworld-icon-32px.png
Source3: tworld-icon-48px.png
Source4: tworld.desktop
Source5: tworld.appdata.xml

BuildRequires: desktop-file-utils
BuildRequires: gcc
BuildRequires: libappstream-glib
BuildRequires: make
BuildRequires: SDL-devel

Requires: hicolor-icon-theme
Requires: %{name}-cclp = %{version}-%{release}
Requires: %{name}-data = %{version}-%{release}

%description
%{fullname} is a game made up of both intellectually engaging puzzles
and situations demanding fast reflexes. The object of each level
is simply to get out — i.e., to find and achieve the exit tile.
This simple task, however, can sometimes be extremely challenging.

%package data
Summary: Data files for %{name}
BuildArch: noarch

# The README says that all sound files and some of the graphics
# have been placed by their authors in the public domain.
License: GPL-2.0-or-later AND LicenseRef-Fedora-Public-Domain

%description data
Data files (graphics, sounds) required to play %{fullname}.

%package cclp
Summary: Level packs for %{name}
BuildArch: noarch

# For discussion regarding the license classification, see:
# https://gitlab.com/fedora/legal/fedora-license-data/-/issues/127
License: LicenseRef-CCLP1 AND LicenseRef-CCLP2

Requires: %{name}-data = %{version}-%{release}

%description cclp
Community-created level packs for %{fullname}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
cp -p %{SOURCE1} .
cp -p %{SOURCE2} .
cp -p %{SOURCE3} .
cp -p %{SOURCE4} .
cp -p %{SOURCE5} .

%build
%configure
make %{?_smp_mflags} prefix=%{_prefix}

%install
make install prefix=%{buildroot}%{_prefix} bindir=%{buildroot}%{_bindir} mandir=%{buildroot}%{_mandir}

install -m 755 -d %{buildroot}%{_datadir}/applications/
desktop-file-install  --dir=%{buildroot}%{_datadir}/applications/  %{name}.desktop

appstream-util validate-relax --nonet tworld.appdata.xml
install -m 755 -d %{buildroot}%{_metainfodir}
install -m 644 -p tworld.appdata.xml %{buildroot}%{_metainfodir}/%{name}.appdata.xml

for SIZE in 16 32 48; do
  install -m 755 -d %{buildroot}%{_datadir}/icons/hicolor/${SIZE}x${SIZE}/apps/
  install -m 644 -p \
    tworld-icon-${SIZE}px.png \
    %{buildroot}%{_datadir}/icons/hicolor/${SIZE}x${SIZE}/apps/%{name}.png
done

cp -a CCLPs %{buildroot}%{_datadir}/%{name}/
cat > %{buildroot}%{_datadir}/%{name}/sets/CCLP2-MS.dac <<EOF
file=CCLP2.dat
lastlevel=149
ruleset=ms
EOF

%files
%doc README BUGS docs/tworld.html
%license COPYING
%{_bindir}/%{name}
%{_mandir}/*/%{name}.*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_metainfodir}/%{name}.appdata.xml

%files data
%license COPYING
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/data
     %{_datadir}/%{name}/data/intro.dat
%dir %{_datadir}/%{name}/sets
     %{_datadir}/%{name}/sets/cc*.dac
     %{_datadir}/%{name}/sets/intro*.dac
%{_datadir}/%{name}/res

%files cclp
%docdir %{_datadir}/%{name}/CCLPs
        %{_datadir}/%{name}/CCLPs
%{_datadir}/%{name}/data/CCLP*.dat
%{_datadir}/%{name}/sets/CCLP*.dac

%changelog
%autochangelog
