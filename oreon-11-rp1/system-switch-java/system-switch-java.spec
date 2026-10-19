%global source0_hash 333d8b584739b5229546afde34ba969d0241228dc76a8b43c26673f35a888d4e
%global py_byte_compile 1
Name: system-switch-java
Version: 1.1.8
Release:        1%{?dist}
Summary:        A tool for changing the default Java toolset
License: GPL-2.0-or-later AND LicenseRef-Callaway-BSD
URL: https://pagure.io/%{name}
Source0:        http://releases.pagure.org/%{name}/%{name}-%{name}-%{version}.tar.gz
Patch0: pythonversion.bad.patch
Patch1: configure.patch
BuildArch: noarch
Requires: /usr/sbin/alternatives
Requires: libglade2
Requires: python3-newt
Requires: python3-gobject-base
Requires: python3
Requires: usermode
Requires: usermode-gtk
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  gettext-devel
BuildRequires:  glib2-devel
BuildRequires:  make
BuildRequires:  python3-devel
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
