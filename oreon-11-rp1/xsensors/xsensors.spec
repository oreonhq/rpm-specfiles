%global source0_hash 4f583b72c99be13eb06249d5b28bda2f8f204e07e67049bc00c6c60cfd0c352c
Name:           xsensors
Version:        0.80
Release:        1%{?dist}
Summary:        An X11 interface to lm_sensors
License:        GPL-2.0-or-later
Url:            https://github.com/Mystro256/xsensors
Source0:        https://github.com/Mystro256/%{name}/archive/%{version}.tar.gz
ExcludeArch: %{ix86}
# oreon:deps
BuildRequires:  cairo-devel
BuildRequires:  desktop-file-utils
BuildRequires:  glib2-devel
BuildRequires:  gtk2-devel
BuildRequires:  lm_sensors-devel
BuildRequires:  make
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
