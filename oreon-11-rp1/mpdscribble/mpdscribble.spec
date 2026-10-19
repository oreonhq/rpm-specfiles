%global source1_hash b2a7addc2adf43225e3007ce1919f7033e0d40a97473aa4b3f5d67e69d9115fc
%global source0_hash 20f89d945bf517c4d68bf77a77a359fdb13842ab1295e8d21eda79be2b5b35ce
Name:           mpdscribble
Version:        0.25
Release:        1%{?dist}
Summary:        A mpd client which submits information about tracks being played to Last.fm
License:        GPL-2.0-or-later AND BSD-2-Clause
URL:            https://www.musicpd.org/clients/%{name}/
Source0:        https://www.musicpd.org/download/%{name}/%{version}/%{name}-%{version}.tar.xz
Source1:        https://www.musicpd.org/download/%{name}/%{version}/%{name}-%{version}.tar.xz.sig
Source2:        0392335A78083894A4301C43236E8A58C6DB4512.gpg
Source3:        %{name}.tmpfiles.conf
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-g++
BuildRequires:  libcurl-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libmpdclient-devel
BuildRequires:  meson
BuildRequires:  systemd-devel
# /oreon:deps
%description
mpdscribble is a music player daemon (mpd) client which submits information
about tracks being played to Last.fm (formerly audioscrobbler)

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

# Create a sysusers.d config file
cat >mpdscribble.sysusers.conf <<EOF
u mpdscribble - 'Mpdscribble' %{_localstatedir}/cache/%{name} -
EOF

%build

%meson
%meson_build
%check

%meson_test
%install
%meson_install
install -D -m 0644 -p %{SOURCE3} %{buildroot}%{_tmpfilesdir}/%{name}.conf
install -d %{buildroot}%{_localstatedir}/run/%{name}
install -d %{buildroot}%{_localstatedir}/cache/%{name}
rm -rf %{buildroot}%{_defaultdocdir}
install -m0644 -D mpdscribble.sysusers.conf %{buildroot}%{_sysusersdir}/mpdscribble.conf
%oreon_autofiles main

%post

%systemd_post %{name}.service
%preun

%systemd_preun %{name}.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
