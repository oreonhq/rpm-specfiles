%global source0_hash b8e34286278f4fef3e1bfe9685c395ccc0eb50c14d3a2fb4953dd00fbfd3af39
%global _changelog_trimtime %(date +%s -d "1 year ago")
Name:		xdg-user-dirs
Version:	0.20
Release:        1%{?dist}
Summary:        Handles user special directories
License:	GPL-2.0-or-later AND MIT
URL:		https://freedesktop.org/wiki/Software/xdg-user-dirs
Source0:        https://user-dirs.freedesktop.org/releases/%{name}-%{version}.tar.xz
Requires:	%{_sysconfdir}/xdg/autostart
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  docbook-style-xsl
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  git-core
BuildRequires:  libxslt
BuildRequires:  make
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
Contains xdg-user-dirs-update that updates folders in a users
homedirectory based on the defaults configured by the administrator.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -S git_am

%conf
autoreconf -fiv -I ./m4
%configure

%build

%make_build
%install
%make_install
%find_lang %name
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.18-12
- Prepare for Oreon 11 (RP1)
