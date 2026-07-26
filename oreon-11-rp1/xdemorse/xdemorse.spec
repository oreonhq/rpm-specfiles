%global source0_hash 32de070badc9ef369b942ee36089c73935b5b7fc9fecf6d4d2418d2e3c02e9cf

Name:           xdemorse
Version:        3.5
Release:        20%{?dist}
Summary:        GTK based application for decoding and displaying Morse code signals

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.qsl.net/5b4az/pkg/morse/xdemorse/xdemorse.html
Source0:        http://www.qsl.net/5/5b4az//pkg/morse/%{name}/%{name}-%{version}.tar.bz2
#Wrapper script for user config
Source3:        xdemorse.sh.in
Patch0:         %{name}-3.5-desktopfile.patch
Patch1:         %{name}-3.5-Makefile.patch
Patch2: xdemorse-configure-c99.patch

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  gtk3-devel, desktop-file-utils, alsa-lib-devel

%description
xdemorse is a GTK+ graphical version of demorse, using the same
decoding engine as demorse.

It has an FFT-derived "waterfall" display of the incoming audio signal's
spectrum, as well as a 'scope-like display of the audio detector's output
and status of the mark/space discriminator ("slicer"). xdemorse also has
CAT for the FT-847 and this can be used to net the receiver's frequency
to the incoming signal, by clicking near its trace in the waterfall display.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .desktop
%patch -P1 -p1 -b .makefile
%patch -P2 -p1

%build

%configure
make %{?_smp_mflags}

%install
mkdir -p $RPM_BUILD_ROOT%{_pkgdocdir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps/
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1

make install DESTDIR=$RPM_BUILD_ROOT

#install default user configuration file
install -p -D -m 0644 .xdemorse/xdemorserc $RPM_BUILD_ROOT%{_datadir}/%{name}/
install -p -D -m 0644 .xdemorse/%{name}.glade $RPM_BUILD_ROOT%{_datadir}/%{name}/

#move original binary to libexecdir
mkdir -p $RPM_BUILD_ROOT%{_libexecdir}/
mv $RPM_BUILD_ROOT%{_bindir}/%{name} $RPM_BUILD_ROOT%{_libexecdir}/%{name}-bin

#install wrapper script
install -p -D -m 0755 %{SOURCE3} $RPM_BUILD_ROOT%{_bindir}/xdemorse

install -p -D -m 644 AUTHORS ChangeLog README doc/Morsecode.txt doc/%{name}.html $RPM_BUILD_ROOT%{_pkgdocdir}

%files
%{_pkgdocdir}
%license COPYING
%{_bindir}/*
%{_libexecdir}/*
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}/xdemorserc
%{_datadir}/%{name}/%{name}.glade
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man*/%{name}*

%changelog
%autochangelog
