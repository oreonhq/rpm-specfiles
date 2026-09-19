%global source0_hash 7dd9356dc138464df4e82680ed385eaeea9b690ba4644b25124506eb1ec20484

Name:    sugar-chat
Version: 86
Release: 17%{?dist}
Summary: Chat client for Sugar
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL:     http://wiki.laptop.org/go/Chat
Source0: http://download.sugarlabs.org/sources/sucrose/fructose/Chat/Chat-%{version}.tar.bz2
 
BuildRequires: python3-devel
BuildRequires: sugar-toolkit-gtk3
BuildRequires: telepathy-glib
BuildRequires: telepathy-glib-devel
BuildRequires: gettext

Requires: sugar 
Requires: telepathy-mission-control

BuildArch: noarch

%description
The chat activity provides a chat client for the Sugar interface.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n Chat-%{version}

sed -i 's/python/python3/' setup.py

%build
python3 ./setup.py build

%install
mkdir -p $RPM_BUILD_ROOT%{sugaractivitydir}
python3 ./setup.py install --prefix=$RPM_BUILD_ROOT/%{_prefix}
rm %{buildroot}%{_prefix}/share/applications/*.desktop || true

# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_3
%py_byte_compile %{python3} %{buildroot}%{_datadir}/{sugaractivitydir}/Chat.activity/

%find_lang org.laptop.Chat

%files -f org.laptop.Chat.lang
%license COPYING
%doc NEWS
%{sugaractivitydir}/Chat.activity/

%changelog
%autochangelog
