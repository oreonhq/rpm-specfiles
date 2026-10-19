%global source0_hash 562b362f04a83940d1882049488c0c3c4f9dd5d1c2129d1af5b00cfa24493007
%global date 2024-03-24
%global git 7098bdd27548
%global rel 11
Version:	1
Name:		dtv-scan-tables
Summary:        Digital TV scan tables
Release:        1%{?dist}
License:	LicenseRef-Not-Copyrightable
URL:		https://git.linuxtv.org/dtv-scan-tables.git
Source0:        https://linuxtv.org/downloads/%{name}/%{name}-%{date}-%{git}.tar.bz2
BuildArch:	noarch
Conflicts:	dvb-apps < 1.1.2-6.1488.f3a70b206f0f
# oreon:deps
BuildRequires:  make
BuildRequires:  v4l-utils
# /oreon:deps
%description
This package contains digital TV scan tables that are used by TV applications
to scan for channels.

%package legacy
Summary:	Digital TV scan tables in the legacy DVBv3 format
%description legacy
This package contains digital TV scan tables that are used by TV applications
to scan for channels in the legacy DVBv3 format, compatible with the old
dvb-apps.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -T -c
%{__tar} xf %{SOURCE0} --transform="s,/usr/share/dvb/,,"

%build

make dvbv3
%install
make DATADIR=%{buildroot}/%{_datadir} install install_v3
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n dtv-scan-tables-legacy -f %{oreon_filedir}/dtv-scan-tables-legacy.list

%changelog

%autochangelog
