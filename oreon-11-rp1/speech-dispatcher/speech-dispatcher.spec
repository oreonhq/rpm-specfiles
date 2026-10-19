%global source0_hash b14a5238d287d2dcce4dd42bbd66ca65fa228e7e683708267f7b34036f7ba4b4
%global source1_hash 382dda1d14a07b3125a8b5084695aa9ba5cb0fff02e5aab69fd6c7e23cbcf4d7
%global festival_backend 1
Name:          speech-dispatcher
Version:       0.12.1
Release:        1%{?dist}
Summary:        To provide a high-level device independent layer for speech synthesis
License:       GPL-2.0-or-later AND LGPL-2.1-only OR LGPL-2.0-only
URL:           http://devel.freebsoft.org/speechd
Source0:        https://github.com/brailcom/speechd/releases/download/%{version}/speech-dispatcher-%{version}.tar.gz
Source1:       https://www.freebsoft.org/pub/projects/sound-icons/sound-icons-0.1.tar.gz
Patch1:        0001-Remove-pyxdg-dependency.patch
Requires:      %{name}-espeak-ng%{?_isa} = %{version}-%{release}
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
Obsoletes:     speech-dispatcher-baratinoo < 0.9.1
Obsoletes:     speech-dispatcher-kali < 0.9.1
# oreon:deps
BuildRequires:  alsa-lib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  dotconf-devel
BuildRequires:  espeak-ng-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel
BuildRequires:  help2man
BuildRequires:  intltool
BuildRequires:  libao-devel
BuildRequires:  libsndfile-devel
BuildRequires:  libtool-ltdl-devel
BuildRequires:  make
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  texinfo
# /oreon:deps
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

%package festival
Summary:        Speech Dispatcher festival module
Requires:       %{name}%{_isa} = %{version}-%{release}
Requires:       festival-freebsoft-utils
%description festival
This package contains the festival output module for Speech Dispatcher.

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
rm -f %{buildroot}%{_infodir}/dir
find %{buildroot} -name '*.la' -delete
mkdir -p %{buildroot}%{_sysconfdir}/speech-dispatcher/clients
mkdir -p %{buildroot}%{_sysconfdir}/speech-dispatcher/modules
mv %{buildroot}%{_datadir}/speech-dispatcher/conf/speechd.conf %{buildroot}%{_sysconfdir}/speech-dispatcher/
mv %{buildroot}%{_datadir}/speech-dispatcher/conf/clients/* %{buildroot}%{_sysconfdir}/speech-dispatcher/clients
mv %{buildroot}%{_datadir}/speech-dispatcher/conf/modules/* %{buildroot}%{_sysconfdir}/speech-dispatcher/modules
mkdir -p -m 0700 %{buildroot}%{_localstatedir}/log/speech-dispatcher/
desktop-file-validate %{buildroot}/%{_datadir}/speech-dispatcher/conf/desktop/speechd.desktop
sed 's/# AudioOutputMethod "pulse,alsa"/AudioOutputMethod "pulse,alsa"/' %{buildroot}%{_sysconfdir}/speech-dispatcher/speechd.conf
sed -i 's/#AddModule "espeak-ng"                "sd_espeak-ng" "espeak-ng.conf"/AddModule "espeak-ng"                "sd_espeak-ng" "espeak-ng.conf"/' %{buildroot}%{_sysconfdir}/speech-dispatcher/speechd.conf
%if %{festival_backend} == 0
rm %{buildroot}%{_sysconfdir}/speech-dispatcher/modules/festival.conf
rm %{buildroot}%{_libdir}/speech-dispatcher-modules/sd_festival
%oreon_autofiles python3-speechd usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%post 

%systemd_post speech-dispatcherd.service
%postun

%systemd_postun_with_restart speech-dispatcherd.service
%preun

%systemd_preun speech-dispatcherd.service
%files -f %{oreon_filedir}/main.list
%files -n speech-dispatcher-libs -f %{oreon_filedir}/speech-dispatcher-libs.list
%files -n speech-dispatcher-devel -f %{oreon_filedir}/speech-dispatcher-devel.list
%files -n speech-dispatcher-doc -f %{oreon_filedir}/speech-dispatcher-doc.list
%files -n speech-dispatcher-utils -f %{oreon_filedir}/speech-dispatcher-utils.list
%files -n speech-dispatcher-espeak-ng -f %{oreon_filedir}/speech-dispatcher-espeak-ng.list
%files -n speech-dispatcher-festival -f %{oreon_filedir}/speech-dispatcher-festival.list
%files -n python3-speechd -f %{oreon_filedir}/python3-speechd.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.12.1-6
- Prepare for Oreon 11 (RP1)
