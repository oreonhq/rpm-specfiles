%global source0_hash dee5bcc0566ba2dc95b9c3b4cadd5e8b3bb2798a54a2a8d8652708915fe45d50

#https://bugzilla.redhat.com/show_bug.cgi?id=455071

%global _hardened_build 1
%global minorversion 0.6
%global xfceversion 4.16

Name:           xfce4-mpc-plugin
Version:        0.6.0
Release:        %autorelease
Summary:        MPD client for the Xfce panel

License:        ISC
URL:            http://goodies.xfce.org/projects/panel-plugins/%{name}
#VCS: git:git://git.xfce.org/panel-plugins/xfce4-mpc-plugin
Source0:        http://archive.xfce.org/src/panel-plugins/%{name}/%{minorversion}/%{name}-%{version}.tar.xz

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  libxfce4ui-devel >= %{xfceversion}
BuildRequires:  xfce4-panel-devel >= %{xfceversion}
BuildRequires:  exo-devel >= 0.5.0
BuildRequires:  libmpd-devel >= 0.12
BuildRequires:  meson
Requires:       xfce4-panel >= %{xfceversion}

%description
A simple client plugin for MPD, the Music Player Daemon.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%meson
%meson_build

%install
%meson_install

# FIXME: make sure debuginfo is generated properly (#795107)
chmod -c +x %{buildroot}%{_libdir}/xfce4/panel/plugins/*.so

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS README
%license COPYING
%{_libdir}/xfce4/panel/plugins/*.so
%{_datadir}/xfce4/panel/plugins/*.desktop

%changelog
%autochangelog
