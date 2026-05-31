%global source0_hash b14a5238d287d2dcce4dd42bbd66ca65fa228e7e683708267f7b34036f7ba4b4
%global source1_hash 382dda1d14a07b3125a8b5084695aa9ba5cb0fff02e5aab69fd6c7e23cbcf4d7

%if 0%{?rhel} > 9
%global festival_backend 0
%else
%global festival_backend 1
%endif

Name:          speech-dispatcher
Version:       0.12.1
Release:       6%{?dist}
Summary:       To provide a high-level device independent layer for speech synthesis

# Almost all files are under GPL-2.0-or-later, however
# src/c/clients/spdsend/spdsend.h is licensed under GPLv2,
# which makes %%_bindir/spdsend GPLv2.
License:       GPL-2.0-or-later AND LGPL-2.1-only OR LGPL-2.0-only
URL:           http://devel.freebsoft.org/speechd
Source0:        https://github.com/brailcom/speechd/releases/download/%{version}/speech-dispatcher-%{version}.tar.gz
Source1:       http://www.freebsoft.org/pub/projects/sound-icons/sound-icons-0.1.tar.gz

Patch1:        0001-Remove-pyxdg-dependency.patch
#Patch2:        4ba45da405fe8dba5ed56725d20a388d6d0269a4.patch
#Patch3:        de9588a29ed6deda8ced1bab98abccebfe1ee788.patch

BuildRequires: alsa-lib-devel
BuildRequires: desktop-file-utils
BuildRequires: dotconf-devel
BuildRequires: espeak-ng-devel
%if 0%{?fedora} || 0%{?rhel} < 10
BuildRequires: flite-devel >= 2.0
%endif
BuildRequires: gcc
BuildRequires: gcc-c++
Buildrequires: glib2-devel
BuildRequires: help2man
Buildrequires: intltool
Buildrequires: libao-devel
Buildrequires: libtool-ltdl-devel
Buildrequires: libsndfile-devel
BuildRequires: make
Buildrequires: pulseaudio-libs-devel
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: systemd-rpm-macros
BuildRequires: texinfo
BuildRequires: systemd-devel

Requires:      %{name}-espeak-ng%{?_isa} = %{version}-%{release}
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
Obsoletes:     speech-dispatcher-baratinoo < 0.9.1
Obsoletes:     speech-dispatcher-kali < 0.9.1

%description
* Common interface to different TTS engines
* Handling concurrent synthesis requests – requests may come
  asynchronously from multiple sources within an application
  and/or from more different applications.
* Subsequent serialization, resolution of conflicts and
  priorities of incoming requests
* Context switching – state is maintained for each client
  connection independently, event for connections from
  within one application.
* High-level client interfaces for popular programming languages
* Common sound output handling – audio playback is handled by
  Speech Dispatcher rather than the TTS engine, since most engines
  have limited sound output capabilities.

%package        libs
Summary:        Development files for %{name}
License:        GPL-2.0-or-later
# split out of main package
Conflicts:      %{name} < 0.11.5-4

%description    libs
The %{name}-libs package contains runtime libraries for applications
that use %{name}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
License:        GPL-2.0-or-later

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package doc
Summary:        Documentation for speech-dispatcher
License:        GPL-2.0-or-later
Requires:       %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
speechd documentation

%package utils
Summary:        Various utilities for speech-dispatcher
License:        GPL-2.0-or-later
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       python3-speechd = %{version}-%{release}
Requires:       pulseaudio-utils

%description utils
Various utilities for speechd

%package espeak-ng
Summary:        Speech Dispatcher espeak-ng module
Requires:       %{name}%{_isa} = %{version}-%{release}

%description espeak-ng
This package contains the espeak-ng output module for Speech Dispatcher.

%if %{festival_backend}
%package festival
Summary:        Speech Dispatcher festival module
Requires:       %{name}%{_isa} = %{version}-%{release}
Requires:       festival-freebsoft-utils

%description festival
This package contains the festival output module for Speech Dispatcher.
%endif

%if 0%{?fedora} || 0%{?rhel} < 10
%package flite
Summary:        Speech Dispatcher flite module
Requires:       %{name}%{_isa} = %{version}-%{release}
Requires:       flite%{?_isa} >= 2.0

%description flite
This package contains the flite output module for Speech Dispatcher.
%endif

%package -n python3-speechd
Summary:        Python 3 Client API for speech-dispatcher
License:        GPL-2.0-or-later

%description -n python3-speechd
Python 3 module for speech-dispatcher

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

tar xf %{SOURCE1}

%build
%configure --disable-static \
	--with-alsa --with-pulse --with-libao \
	--with-espeak-ng \
%if 0%{?fedora} || 0%{?rhel} < 10
	--with-flite \
%endif
	--without-oss --without-nas --without-espeak \
	--with-kali=no --with-baratinoo=no --with-ibmtts=no --with-voxin=no \
	--sysconfdir=%{_sysconfdir} --with-default-audio-method=pulse \
	--with-module-bindir=%{_libdir}/speech-dispatcher-modules/ \
	--with-systemdsystemunitdir=%{_unitdir} \
	--with-systemduserunitdir=%{_prefix}/lib/systemd/user/

%make_build

%install
%make_install

install -p -m 0644 sound-icons-0.1/* %{buildroot}%{_datadir}/sounds/%{name}/

%find_lang speech-dispatcher

#Remove %%{_infodir}/dir file
rm -f %{buildroot}%{_infodir}/dir

find %{buildroot} -name '*.la' -delete

# Move the config files from /usr/share to /etc
mkdir -p %{buildroot}%{_sysconfdir}/speech-dispatcher/clients
mkdir -p %{buildroot}%{_sysconfdir}/speech-dispatcher/modules
mv %{buildroot}%{_datadir}/speech-dispatcher/conf/speechd.conf %{buildroot}%{_sysconfdir}/speech-dispatcher/
mv %{buildroot}%{_datadir}/speech-dispatcher/conf/clients/* %{buildroot}%{_sysconfdir}/speech-dispatcher/clients
mv %{buildroot}%{_datadir}/speech-dispatcher/conf/modules/* %{buildroot}%{_sysconfdir}/speech-dispatcher/modules

# Create log dir
mkdir -p -m 0700 %{buildroot}%{_localstatedir}/log/speech-dispatcher/

# Verify the desktop files
desktop-file-validate %{buildroot}/%{_datadir}/speech-dispatcher/conf/desktop/speechd.desktop

# enable pulseaudio as default with a fallback to alsa
sed 's/# AudioOutputMethod "pulse,alsa"/AudioOutputMethod "pulse,alsa"/' %{buildroot}%{_sysconfdir}/speech-dispatcher/speechd.conf

# explicitly enable espeak-ng module, othervise it falls back to espeak-ng-mbrola and it has bad pronunciation
sed -i 's/#AddModule "espeak-ng"                "sd_espeak-ng" "espeak-ng.conf"/AddModule "espeak-ng"                "sd_espeak-ng" "espeak-ng.conf"/' %{buildroot}%{_sysconfdir}/speech-dispatcher/speechd.conf



# Remove Festival related files if needed, we can't disable their generation by any other means (e. g. configure option).
# And if not done, we're getting an error about installed but unpackaged files.
%if %{festival_backend} == 0
rm %{buildroot}%{_sysconfdir}/speech-dispatcher/modules/festival.conf
rm %{buildroot}%{_libdir}/speech-dispatcher-modules/sd_festival
%endif

%post 
%systemd_post speech-dispatcherd.service

%postun
%systemd_postun_with_restart speech-dispatcherd.service

%preun
%systemd_preun speech-dispatcherd.service

%files -f speech-dispatcher.lang
%license COPYING.LGPL
%doc NEWS README.md
%dir %{_sysconfdir}/speech-dispatcher/
%dir %{_sysconfdir}/speech-dispatcher/clients
%dir %{_sysconfdir}/speech-dispatcher/modules
%config(noreplace) %{_sysconfdir}/speech-dispatcher/speechd.conf
%config(noreplace) %{_sysconfdir}/speech-dispatcher/clients/*.conf
%config(noreplace) %{_sysconfdir}/speech-dispatcher/modules/*.conf
%exclude %{_sysconfdir}/speech-dispatcher/modules/espeak*.conf
%exclude %{_sysconfdir}/speech-dispatcher/modules/festival.conf
%exclude %{_sysconfdir}/speech-dispatcher/modules/flite.conf
%{_bindir}/speech-dispatcher
%{_datadir}/speech-dispatcher/
%dir %{_libdir}/speech-dispatcher-modules/
%{_libdir}/speech-dispatcher-modules/sd_cicero
%{_libdir}/speech-dispatcher-modules/sd_dummy
%{_libdir}/speech-dispatcher-modules/sd_generic
%{_libdir}/speech-dispatcher-modules/sd_openjtalk

%dir %{_libdir}/speech-dispatcher
%{_libdir}/speech-dispatcher/spd*.so
%{_datadir}/sounds/speech-dispatcher
%{_mandir}/man1/speech-dispatcher.1*
%dir %attr(0700, root, root) %{_localstatedir}/log/speech-dispatcher/
%{_unitdir}/speech-dispatcherd.service
%{_prefix}/lib/systemd/user/speech-dispatcher.service
%{_prefix}/lib/systemd/user/speech-dispatcher.socket

%files libs
%license COPYING.LGPL
%{_libdir}/libspeechd.so.2
%{_libdir}/libspeechd.so.2.6.0
%{_libdir}/libspeechd_module.so.0
%{_libdir}/libspeechd_module.so.0.0.0

%files devel
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc

%files doc
%{_infodir}/*

%files utils
%{_bindir}/spd-conf
%{_bindir}/spd-say
%{_bindir}/spdsend
%{_mandir}/man1/spd-conf.1*
%{_mandir}/man1/spd-say.1*

%files espeak-ng
%config(noreplace) %{_sysconfdir}/speech-dispatcher/modules/espeak-ng.conf
%{_libdir}/speech-dispatcher-modules/sd_espeak-ng
%{_libdir}/speech-dispatcher-modules/sd_espeak-ng-mbrola

%if %{festival_backend}
%files festival
%config(noreplace) %{_sysconfdir}/speech-dispatcher/modules/festival.conf
%{_libdir}/speech-dispatcher-modules/sd_festival
%endif

%if 0%{?fedora} || 0%{?rhel} < 10
%files flite
%config(noreplace) %{_sysconfdir}/speech-dispatcher/modules/flite.conf
%{_libdir}/speech-dispatcher-modules/sd_flite
%endif

%files -n python3-speechd
%{python3_sitearch}/speechd*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.12.1-6
- Prepare for Oreon 11 (RP1)
