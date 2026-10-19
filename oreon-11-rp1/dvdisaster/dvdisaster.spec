%global source0_hash 9c4c53d9e67855eb04ef87b7525045b4c5b34a9e782c44615dac3ba1a2950f39
%bcond_with	dvdrom
Summary:        Additional error protection for CD/DVD media
Name: dvdisaster
Version: 0.79.5
Release:        1%{?dist}
License: GPL-2.0-or-later
URL: http://dvdisaster.net
Source0:        http://dvdisaster.net/downloads/dvdisaster-%{version}.tar.bz2
Patch1: dvdisaster-0.79.5-dvdrom.patch
Patch0: dvdisaster-configure-c99.patch
Requires: xdg-utils
# oreon:deps
BuildRequires:  bzip2-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  gtk2-devel
BuildRequires:  libpng-devel
BuildRequires:  make
# /oreon:deps
%description
%{name} provides a margin of safety against data loss on CD and DVD media
caused by scratches or aging. It creates error correction data,
which is used to recover unreadable sectors if the disc becomes damaged
at a later time.

%description -l de
%{name} erzeugt einen Sicherheitspuffer gegen Datenverluste, die auf
CD- und DVD-Datenträgern durch Alterung oder Kratzer entstehen. Es erzeugt
Fehlerkorrekturdaten, um bei nachfolgenden Datenträger-Problemen unlesbare
Sektoren zu rekonstruieren.

%description -l it
%{name} offre un margine di sicurezza contro la perdita di dati dei supporti
CD e DVD causata dall'invecchiamento e dai graffi. Crea dei dati di correzione
degli errori che saranno poi utilizzati per recuperare i settori illeggibili
se il supporto dovesse danneggiarsi col tempo.

%description -l cs
%{name} poskytuje dodatečnou ochranu proti ztrátě dat na médiích CD a DVD
způsobených poškrábáním nebo stárnutím. Vytváří data oprav chyb, která
jsou použita pro obnovu nečitelných sektorů, pokud se disk později
poškodí.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%{?_with_dvdrom:%patch1 -p1 -b .dvdrom}
%patch -P0 -p1

%build

export CFLAGS="$RPM_OPT_FLAGS -fcommon"
%configure	\
	--docdir=%{_docdir} \
	--docsubdir=%{name} \
	--localedir=%{_datadir}/locale
make
%install
make install BUILDROOT=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_bindir}/*-uninstall.sh
install -d $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -p -m644 -D contrib/dvdisaster48.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/dvdisaster48.png
for NN in 16 24 32 48 64
do
    install -p -m644 -D contrib/dvdisaster${NN}.png \
		$RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${NN}x${NN}/apps/dvdisaster${NN}.png
done
desktop-file-install \
	--dir ${RPM_BUILD_ROOT}%{_datadir}/applications	\
	--add-category=AudioVideo \
	--add-category=DiscBurning \
	contrib/%{name}.desktop
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
