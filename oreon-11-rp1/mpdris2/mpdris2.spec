%global source0_hash d0f0467841e7866310cff44a1063334a9c776a64fd594815d926670b765fbee6
%global tarname mpDris2
Name:           mpdris2
Version:        0.9.1
Release:        1%{?dist}
Summary:        Provide MPRIS 2 support to mpd
License:        GPL-3.0-or-later
URL:            https://github.com/eonpatapon/%{name}
Source0:        https://github.com/eonpatapon/%{name}/archive/%{version}.tar.gz#/%{tarname}-%{version}.tar.gz
Patch0:         mpdris2-0.9.1-currentsong.patch
BuildArch:      noarch
Requires:       python3-dbus python3-mpd2 python3-gobject python3-mutagen
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  make
BuildRequires:  python3-devel
# /oreon:deps
%description
mpDris2 provides MPRIS 2 support to mpd (Music Player Daemon).

mpDris2 is run in the user session and monitors a local or distant 
mpd server

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{tarname}-%{version} -p1

%build

env NOCONFIGURE=1 ./autogen.sh
export PYTHON=%{__python3}
%configure --docdir=%{_pkgdocdir}
make %{?_smp_mflags}
%install
%make_install
rm -fv %{buildroot}%{_docdir}/%{name}/COPYING
rm -fv %{buildroot}%{_docdir}/%{name}/README
sed -i '1 s:#!.*:#!%{__python3}:' %{buildroot}%{_bindir}/%{tarname}
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
%find_lang %{tarname}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
