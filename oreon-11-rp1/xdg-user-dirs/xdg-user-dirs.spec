%global source0_hash ec6f06d7495cdba37a732039f9b5e1578bcb296576fde0da40edb2f52220df3c

%global _changelog_trimtime %(date +%s -d "1 year ago")


Name:		xdg-user-dirs
Version:	0.18
Release:	12%{?dist}
Summary:	Handles user special directories

License:	GPL-2.0-or-later AND MIT
URL:		https://freedesktop.org/wiki/Software/xdg-user-dirs
Source0:        https://user-dirs.freedesktop.org/releases/%{name}-%{version}.tar.gz

# Backports from upstream
Patch0001:	0001-Add-a-systemd-service-to-run-xdg-user-dirs-update.patch
Patch0002:	0002-Install-systemd-service-file.patch
# https://gitlab.freedesktop.org/xdg/xdg-user-dirs/-/merge_requests/16
Patch0003:      0003-Fix-autopoint-invocation.patch

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	gettext-devel
BuildRequires:	git-core
BuildRequires:	docbook-style-xsl
BuildRequires:	libxslt
BuildRequires:	systemd-rpm-macros
%if 0%{?fedora} && 0%{?fedora} < 42
BuildRequires:  desktop-file-utils
%endif

Requires:	%{_sysconfdir}/xdg/autostart

%description
Contains xdg-user-dirs-update that updates folders in a users
homedirectory based on the defaults configured by the administrator.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -S git_am

%conf
autoreconf -fiv -I ./m4
%configure

%build
%make_build

%install
%make_install

%find_lang %name

%if 0%{?fedora} && 0%{?fedora} < 42
desktop-file-edit --remove-key=X-systemd-skip %{buildroot}%{_sysconfdir}/xdg/autostart/xdg-user-dirs.desktop
rm -rf %{buildroot}%{_userunitdir}
%endif

%if ! (0%{?fedora} && 0%{?fedora} < 42)
%post
%systemd_user_post xdg-user-dirs.service

%preun
%systemd_user_preun xdg-user-dirs.service

%postun
%systemd_user_postun_with_reload xdg-user-dirs.service
%endif


%files -f %{name}.lang
%license COPYING
%doc NEWS AUTHORS README
%{_bindir}/*
%config(noreplace) %{_sysconfdir}/xdg/user-dirs.conf
%config(noreplace) %{_sysconfdir}/xdg/user-dirs.defaults
%{_sysconfdir}/xdg/autostart/*
%{_mandir}/man1/*
%{_mandir}/man5/*
%if ! (0%{?fedora} && 0%{?fedora} < 42)
%{_userunitdir}/xdg-user-dirs.service
%endif


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.18-12
- Prepare for Oreon 11 (RP1)
