%global source0_hash 0451aa7fae4a9bda7344f4bbaac9c18b7181a4d98a310ad4dfd2d003d4ddf60b

%global commit 6beed311c2ecb3f9662f35ecc06948bd89ed9455
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           wordwarvi
Version:        1.1
Release:        24.git%{shortcommit}%{?dist}
Summary:        Side-scrolling shoot 'em up '80s style arcade game
# Automatically converted from old format: GPLv2+ and CC-BY and CC-BY-SA - review is highly recommended.
License:        GPL-2.0-or-later AND LicenseRef-Callaway-CC-BY AND LicenseRef-Callaway-CC-BY-SA
URL:            https://smcameron.github.io/wordwarvi/
# The 1.1 release never got a tag in git, so we use the commit-id
Source0:        https://github.com/smcameron/wordwarvi/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
Source1:        %{name}.desktop
Source2:        %{name}.png
Source3:        %{name}.appdata.xml
BuildRequires: make
BuildRequires:  gcc
BuildRequires:  gtk2-devel portaudio-devel libvorbis-devel
BuildRequires:  desktop-file-utils libappstream-glib
Requires:       hicolor-icon-theme

%description
Word War vi is your basic side-scrolling shoot 'em up '80s style arcade game.
You pilot your "vi"per craft through core memory, rescuing lost .swp files,
avoiding OS defenses, and wiping out those memory hogging emacs processes.
When all the lost .swp files are rescued, head for the socket which will take
you to the next node in the cluster.

Note: Obviously, emacs is a fine editor and this is all very tongue in cheek,
so don't be getting all bent out of shape because you like emacs better than
vi, mmm-kay?

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{name}-%{commit}

%build
make %{?_smp_mflags} PREFIX=%{_prefix} CFLAGS="$RPM_OPT_FLAGS"

%install
make install PREFIX=%{_prefix} DESTDIR=$RPM_BUILD_ROOT

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
install -p -m 644 %{SOURCE2} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml

%files
%doc AUTHORS COPYING README changelog.txt sounds/Attribution.txt
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man6/%{name}.6*
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png

%changelog
%autochangelog
