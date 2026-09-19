%global source0_hash 9c4c53d9e67855eb04ef87b7525045b4c5b34a9e782c44615dac3ba1a2950f39

%bcond_with	dvdrom

Summary: Additional error protection for CD/DVD media
Name: dvdisaster
Version: 0.79.5
Release: 24%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: http://dvdisaster.net
Source0: http://dvdisaster.net/downloads/dvdisaster-%{version}.tar.bz2

# Nothing illegal, just a scratch wiping from the media
# (legally bought) with a probably copyrighted content,
# but see http://bugzilla.redhat.com/231574 why it is
# not enabled by default...
Patch1: dvdisaster-0.79.5-dvdrom.patch

Patch0: dvdisaster-configure-c99.patch

BuildRequires: gcc
BuildRequires: glib2-devel >= 2.32.0
BuildRequires: gtk2-devel >= 2.6.0
BuildRequires: gettext, desktop-file-utils
BuildRequires: bzip2-devel, libpng-devel
BuildRequires: make
Requires: xdg-utils

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

# can not build locales with %{?_smp_mflags}
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

%files -f %{name}.lang
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_datadir}/icons/hicolor/*/apps/*

%{_docdir}/%{name}
%lang(de) %{_docdir}/%{name}/CREDITS.de

%{_mandir}/man1/*
%lang(de) %{_mandir}/de/man1/*

%changelog
%autochangelog
