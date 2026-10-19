%global source0_hash 39026c6d4a139b9180192d1c37225aa3376fdf4f1a74d7debbdbb693d996afa4
Name:           minidlna
Version:        1.3.3
Release:        16%{?dist}
Summary:        Lightweight DLNA/UPnP-AV server targeted at embedded systems
License:        BSD-2-Clause AND BSD-3-Clause AND GPL-2.0-only AND GPL-2.0-or-later
URL:            http://sourceforge.net/projects/minidlna/
Source0:        http://downloads.sourceforge.net/%{name}/%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.service
Source2:        %{name}-tmpfiles.conf
Source3:        %{name}-licensing-breakdown.txt
Source4:        %{name}.logrotate
Source5:        %{name}.sysusers
Patch0:         %{name}-1.3.0-select_use_after_free.patch
Patch1:         0001-Add-compatibility-with-FFMPEG-7.0.patch
Patch2:         %{name}-CVE-2023-47430.patch
Recommends:     logrotate
%{?systemd_requires}
# oreon:deps
BuildRequires:  avahi-devel
BuildRequires:  flac-devel
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  libexif-devel
BuildRequires:  libid3tag-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libuuid-devel
BuildRequires:  libvorbis-devel
BuildRequires:  make
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  sqlite-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  zlib-devel
# /oreon:deps
%description
MiniDLNA (aka ReadyDLNA) is server software with the aim of being fully
compliant with DLNA/UPnP-AV clients.

The minidlna daemon serves media files (music, pictures, and video) to clients
on your local network.  Example clients include applications such as Totem and
XBMC, and devices such as portable media players, smartphones, and televisions.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Edit the default config file
sed -i 's|#log_dir=/var/log|#log_dir=/var/log/minidlna|' \
  %{name}.conf

%build

%configure \
  --disable-silent-rules \
  --with-db-path=%{_localstatedir}/cache/%{name} \
  --with-log-path=%{_localstatedir}/log/%{name} \
  --enable-tivo
%make_build
%install
%make_install
mkdir -p %{buildroot}%{_sysconfdir}/
install -p -m 644 minidlna.conf %{buildroot}%{_sysconfdir}/
mkdir -p %{buildroot}%{_unitdir}/
install -p -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/
mkdir -p %{buildroot}%{_mandir}/man5/
install -p -m 644 minidlna.conf.5 %{buildroot}%{_mandir}/man5/
mkdir -p %{buildroot}%{_mandir}/man8/
install -p -m 644 minidlnad.8 %{buildroot}%{_mandir}/man8/
install -p -D -m 0644 %{SOURCE5} %{buildroot}%{_sysusersdir}/%{name}.conf
mkdir -p %{buildroot}%{_tmpfilesdir}/
install -p -m 644 %{SOURCE2} %{buildroot}%{_tmpfilesdir}/%{name}.conf
mkdir -p %{buildroot}/run/
install -d -m 755 %{buildroot}/run/%{name}/
mkdir -p %{buildroot}/etc/logrotate.d
install -p -m 644 %{SOURCE4} %{buildroot}/etc/logrotate.d/minidlna
mkdir -p %{buildroot}%{_localstatedir}/cache/
install -d -m 755 %{buildroot}%{_localstatedir}/cache/%{name}/
mkdir -p %{buildroot}%{_localstatedir}/log/
install -d -m 755 %{buildroot}%{_localstatedir}/log/%{name}/
%find_lang %{name}
%oreon_autofiles main

%post

%tmpfiles_create %{_tmpfilesdir}/%{name}.conf
%systemd_post %{name}.service
%preun

%systemd_preun %{name}.service
%postun

%systemd_postun_with_restart %{name}.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
