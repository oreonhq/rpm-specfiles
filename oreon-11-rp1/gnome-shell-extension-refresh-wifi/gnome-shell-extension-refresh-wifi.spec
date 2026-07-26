%global source0_hash dbf764a277c123ba439ce3760888474ede77bd9e4d19513b59a86f3b91df50ae

%global extuuid		refresh-wifi@kgshank.net
%global extdir		%{_datadir}/gnome-shell/extensions/%{extuuid}
%global gschemadir	%{_datadir}/glib-2.0/schemas
%global gitname		gse-refresh-wifi
%global giturl		https://github.com/kgshank/%{gitname}

Name:		gnome-shell-extension-refresh-wifi
Version:	6.0
Release:	20%{?dist}
Summary:	GNOME Shell Extension Refresh Wifi Connections by kgshank

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:	GPL-3.0-or-later
URL:		https://extensions.gnome.org/extension/905/refresh-wifi-connections/
Source0:	%{giturl}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

# Update to untagged version 8.
Patch0:		%{giturl}/compare/6.0...master.patch#/%{name}-6.0_update_to_v8.patch

BuildArch:	noarch

Requires:	gnome-shell-extension-common

%description
Introduce a manual scan button for new wifi network scan.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gitname}-%{version} -p 1

%build
# Place license file on toplevel.
%{__mv} %{extuuid}/license COPYING

# Set proper permissions on files.
%{_bindir}/find . -type f -print | %{_bindir}/xargs %{__chmod} -c -x

%install
%{__mkdir} -p %{buildroot}%{extdir}
%{__cp} -pr %{extuuid}/* %{buildroot}%{extdir}

%files
%license COPYING
%doc README.md
%{extdir}

%changelog
%autochangelog
