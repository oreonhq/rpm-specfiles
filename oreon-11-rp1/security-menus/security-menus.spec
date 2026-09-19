%global source0_hash 94c3e410d91abfebe8a7e52848a64cd43d6ff46b00b589a4ac2cd93f034c8357

Name:           security-menus
Version:        38
Release:        8%{?dist}
Summary:        Menu Structure for the Fedora Security Lab

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            https://pagure.io/security-lab
Source0:        https://releases.pagure.org/security-lab/%{name}-%{version}.tar.xz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  desktop-file-utils

Requires:       redhat-menus
Requires:       xfce4-terminal

%description
This Package adds a Security Lab sub-menu to the xdg menu structure for 
GNOME and other desktop enviroments.

%{name} is listed among Fedora Security Lab packages.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -n security-menu
rm -rf security-{dc3dd,scanmem}*.desktop

%build
# nothing to build

%install
make install DESTDIR=%{buildroot}
for file in %{buildroot}/%{_datadir}/applications/*.desktop; do 
    desktop-file-validate $file
done

%files
%doc AUTHORS COPYING README
%config(noreplace) %{_sysconfdir}/xdg/menus/applications-merged/*.menu
%{_datadir}/desktop-directories/*.directory
%{_datadir}/applications/*.desktop

%changelog
%autochangelog
