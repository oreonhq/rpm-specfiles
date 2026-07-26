%global source0_hash 4f583b72c99be13eb06249d5b28bda2f8f204e07e67049bc00c6c60cfd0c352c

Name:           xsensors
Version:        0.80
Release:        24%{?dist}
Summary:        An X11 interface to lm_sensors

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
Url:            https://github.com/Mystro256/xsensors
Source:         https://github.com/Mystro256/%{name}/archive/%{version}.tar.gz

%if 0%{?rhel} >= 7 || 0%{?fedora}
BuildRequires:  gcc
BuildRequires:  gtk3-devel
BuildRequires:  libappstream-glib
%else
BuildRequires:  gtk2-devel
%endif
BuildRequires:  lm_sensors-devel
BuildRequires:  cairo-devel
BuildRequires:  glib2-devel
BuildRequires:  desktop-file-utils
BuildRequires:  make

# 32bit package serves very little purpose:
ExcludeArch: %{ix86}

%description
Xsensors is a simple GUI program that allows you to read useful data from the
lm_sensors library in a digital read-out like fashion, such as the temperature,
voltage ratings and fan speeds of the running computer.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
desktop-file-validate \
  %{buildroot}%{_datadir}/applications/%{name}.desktop
%if 0%{?rhel} >= 7 || 0%{?fedora}
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/%{name}.appdata.xml
%endif

%files
%doc AUTHORS COPYING README ChangeLog
%{_datadir}/%{name}/theme.tiff
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}.1*
%if 0%{?rhel} >= 7 || 0%{?fedora}
%{_datadir}/appdata/%{name}.appdata.xml
%else
%exclude %{_datadir}/appdata/%{name}.appdata.xml
%endif

%changelog
%autochangelog
