%global source0_hash dfe7adc5876ef0670e7eba2907799bdbb8875ce58bb4208e1a52169bd16a47ca
%global glib2_version 2.80.0
%global gcr_version 3.27.90
%global gcrypt_version 1.2.2
%bcond_without ssh_agent
%global tarball_version %(echo %{version} | tr '~' '.')
%global major_version %(echo %{tarball_version} | cut -d "." -f 1)
Name:           gnome-keyring
Version:        51.1
Release:        1%{?dist}
Summary:        Framework for managing passwords and other secrets
License:        GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.1-or-later AND ((GPL-2.0-or-later OR LGPL-3.0-or-later) OR BSD-3-Clause) AND (MPL-1.1 OR GPL-2.0-or-later OR LGPL-2.1-or-later)
URL:            https://wiki.gnome.org/Projects/GnomeKeyring
Source0:        https://download.gnome.org/sources/%{name}/51/%{name}-%{version}.tar.xz
Patch:          78.patch
%if %{with ssh_agent}
%endif
%if %{with ssh_agent}
Requires: /usr/bin/ssh-add
Requires: /usr/bin/ssh-agent
%endif
Requires: gcr3
# oreon:deps
BuildRequires:  /usr/bin/ssh-add
BuildRequires:  /usr/bin/ssh-agent
BuildRequires:  /usr/bin/xsltproc
BuildRequires:  docbook-dtds
BuildRequires:  docbook-style-xsl
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  git-core
BuildRequires:  intltool
BuildRequires:  libgcrypt-devel
BuildRequires:  libselinux-devel
BuildRequires:  meson
BuildRequires:  pam-devel
BuildRequires:  pkgconfig(gcr-3)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libcap-ng)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(p11-kit-1)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
The gnome-keyring session daemon manages passwords and other types of
secrets for the user, storing them encrypted with a main password.
Applications can use the gnome-keyring library to integrate with the keyring.

%package pam
Summary: Pam module for unlocking keyrings
License: LGPL-2.1-or-later
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pam%{?_isa}
%description pam
The gnome-keyring-pam package contains a pam module that can
automatically unlock the "login" keyring when the user logs in.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
# check for human errors
if [ `echo "%{version}" | grep -cE "\.alpha|\.beta|\.rc"` = "1" ]; then echo "Error: Use tilde in Version field in front of alpha/beta/rc; checked '%{version}'" 1>&2; exit 1; fi

%autosetup -S git -n %{name}-%{tarball_version}

%build

%meson \
           -Dpam=true \
           -Dsystemd=enabled \
           -Dpkcs11-config=%{_datadir}/p11-kit/modules \
%if %{with ssh_agent}
           -Dssh-agent=true
%else
           -Dssh-agent=false
%endif
%meson_build
%install
%meson_install
%find_lang %{name}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

%systemd_user_post gnome-keyring-daemon.service
%preun

%systemd_user_preun gnome-keyring-daemon.service
%files -f %{oreon_filedir}/main.list
%files -n gnome-keyring-pam -f %{oreon_filedir}/gnome-keyring-pam.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 50.0-1
- Prepare for Oreon 11 (RP1)
