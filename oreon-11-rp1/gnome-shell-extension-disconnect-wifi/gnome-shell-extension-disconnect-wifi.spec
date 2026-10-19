%global source0_hash d8cfdb823bd975df6f6fa765eed0f25efc5c7e740c580ecb38faa4952a1b4de2
%global extuuid		disconnect-wifi@kgshank.net
%global extdir		%{_datadir}/gnome-shell/extensions/%{extuuid}
%global gschemadir	%{_datadir}/glib-2.0/schemas
%global gitname		gse-disconnect-wifi
%global giturl		https://github.com/kgshank/%{gitname}
Name:		gnome-shell-extension-disconnect-wifi
Version:	17
Release:        20%{?dist}
Summary:        GNOME Shell Extension Disconnect Wifi by kgshank
License:	GPL-3.0-or-later
URL:		https://extensions.gnome.org/extension/904/disconnect-wifi/
Source0:        %{giturl}/archive/V%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:		%{giturl}/compare/V17...master.patch#/%{name}-17_update_to_V18.patch
BuildArch:	noarch
Requires:	gnome-shell-extension-common
# oreon:deps

# /oreon:deps
%description
Adds a Disconnect option for Wifi in status menu, when a network is
connected.  Shows a Reconnect option, after network is disconnected.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gitname}-%{version} -p 1

%build

%{__mv} %{extuuid}/license COPYING
%{_bindir}/find . -name '*.po' -print -delete
%{_bindir}/find . -name '*.pot' -print -delete
%{_bindir}/find . -type f -print | %{_bindir}/xargs %{__chmod} -c -x
%install
%{__mkdir} -p %{buildroot}%{extdir}
%{__cp} -pr %{extuuid}/* %{buildroot}%{extdir}
%{__cp} -pr %{extuuid}/locale %{buildroot}%{_datadir}
%{__rm} -fr %{buildroot}%{extdir}/{LICENSE,README*,locale,schemas}
%find_lang %{name} --all-name
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
