%global source0_hash 68cc45f0076b615ccf5bc2bf196c454fda2921a0790e5c8fde728a686a146f8d
Name:           l3afpad
Version:        0.8.18.1.11
Release:        1%{?dist}
Summary:        Simple text editor forked from Leafpad, supports GTK+ 3.x
License:        GPL-2.0-or-later
URL:            http://www.calno.com/%{name}/
Source0:        http://www.calno.com/%{name}/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gtk3-devel
BuildRequires:  intltool
BuildRequires:  make
# /oreon:deps
%description
L3afpad is a simple GTK+ text editor that emphasizes simplicity.
As development focuses on keeping weight down to a minimum, only
the most essential features are implemented in the editor.
L3afpad is simple to use, is easily compiled, requires few
libraries, and starts up quickly. 

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q %{nam}

%build

%configure
make %{?_smp_mflags}
%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
desktop-file-install %{buildroot}/%{_datadir}/applications/%{name}.desktop
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
