%global source0_hash be825de7f89175db5ead0cd3744d2761109c70943251a87092259163025520a9

Name:		xdg-user-dirs-gtk
Version:	0.16
Release:	2%{?dist}
Summary:	Gnome integration of special directories

License:	GPL-2.0-or-later
URL:		https://gitlab.gnome.org/GNOME/xdg-user-dirs-gtk
Source0:        https://download.gnome.org/sources/xdg-user-dirs-gtk/%{version}/%{name}-%{version}.tar.xz

# https://gitlab.gnome.org/GNOME/xdg-user-dirs-gtk/-/merge_requests/22
Patch0:		xdg-user-dirs-gtk-0.16-not-showin-kde.patch

BuildRequires:	desktop-file-utils
BuildRequires:	gcc
BuildRequires:	meson
BuildRequires:	systemd-rpm-macros
BuildRequires:	xdg-user-dirs
BuildRequires:	pkgconfig(gtk+-3.0)

Requires:	xdg-user-dirs

%description
Contains some integration of xdg-user-dirs with the gnome
desktop, including creating default bookmarks and detecting
locale changes.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

%build
%meson
%meson_build


%install
%meson_install

%find_lang %name

desktop-file-validate $RPM_BUILD_ROOT%{_sysconfdir}/xdg/autostart/user-dirs-update-gtk.desktop $RPM_BUILD_ROOT%{_datadir}/applications/user-dirs-update-gtk.desktop

%post
%systemd_user_post user-dirs-update-gtk.service

%preun
%systemd_user_preun user-dirs-update-gtk.service

%postun
%systemd_user_postun_with_restart user-dirs-update-gtk.service

%files -f %{name}.lang
%doc NEWS AUTHORS README ChangeLog
%license COPYING
%{_bindir}/xdg-user-dirs-gtk-update
%{_datadir}/applications/user-dirs-update-gtk.desktop
%{_userunitdir}/user-dirs-update-gtk.service
%config(noreplace) %{_sysconfdir}/xdg/autostart/user-dirs-update-gtk.desktop


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.16-2
- Prepare for Oreon 11 (RP1)
