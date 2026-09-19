%global source0_hash 333d8b584739b5229546afde34ba969d0241228dc76a8b43c26673f35a888d4e

# This package depends on automagic byte compilation
# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_2
%global py_byte_compile 1

Name: system-switch-java
Version: 1.1.8
Release: 16%{?dist}
Summary: A tool for changing the default Java toolset

# Automatically converted from old format: GPLv2+ and BSD - review is highly recommended.
License: GPL-2.0-or-later AND LicenseRef-Callaway-BSD
URL: https://pagure.io/%{name}
Source0: http://releases.pagure.org/%{name}/%{name}-%{name}-%{version}.tar.gz
Patch0: pythonversion.bad.patch
# ask autopoint to use gettext installed on the system to prevent mismatch in version
Patch1: configure.patch

BuildArch: noarch

BuildRequires: make
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: python3-devel
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: gettext-devel
BuildRequires: glib2-devel
BuildRequires: autoconf
BuildRequires: automake

Requires: /usr/sbin/alternatives
Requires: libglade2
Requires: python3-newt
Requires: python3-gobject-base
Requires: python3
Requires: usermode
Requires: usermode-gtk

%description
The system-switch-java package provides an easy-to-use tool to select
the default Java toolset for the system.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n system-switch-java-system-switch-java-1.1.8
%patch -P0
%patch -P1

%build
sh ./autogen.sh
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
rm -rf %{buildroot}/usr/share/system-switch-java/__pycache__/*
%find_lang %{name}
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/%{name}.desktop

%files -f %{name}.lang
%license COPYING COPYING.icon
%doc AUTHORS README
%{_bindir}/%{name}
%{_sbindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/switch_java_functions.py*
%{_datadir}/%{name}/switch_java_gui.py*
%{_datadir}/%{name}/switch_java_tui.py*
%{_datadir}/%{name}/switch_java_globals.py*
%{_datadir}/%{name}/switch_java_boot.py*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}/system-switch-java.glade
%config(noreplace) /etc/pam.d/%{name}
%config(noreplace) /etc/security/console.apps/%{name}

%changelog
%autochangelog
