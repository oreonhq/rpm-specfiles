%global source0_hash 562b362f04a83940d1882049488c0c3c4f9dd5d1c2129d1af5b00cfa24493007

%global date 2024-03-24
%global git 7098bdd27548

#WARNING: should be monotonically incremented
%global rel 11

# WARNING: You should probably never touch those fields
Version:	2026-04-11-be35975ac877
Name:		dtv-scan-tables
Summary:	Digital TV scan tables
Release:	%{rel}.%(echo %{date} | tr -d -)git%{git}%{?dist}.3

#2013-07-19: License discussed in: https://bugzilla.redhat.com/show_bug.cgi?id=986051#c4
#and https://gitlab.com/fedora/legal/fedora-license-data/-/issues/580#note_2155500881
License:	LicenseRef-Not-Copyrightable
URL:		https://git.linuxtv.org/dtv-scan-tables.git
Source0:	https://linuxtv.org/downloads/dtv-scan-tables/dtv-scan-tables-%{date}-%{git}.tar.bz2
BuildArch:	noarch
%if 0%{?fedora} >= 40
BuildRequires:	dvb-tools
%else
BuildRequires:	v4l-utils >= 1.4.0
%endif
BuildRequires:  make
# FPC permission for Conflicts:
# https://lists.fedoraproject.org/pipermail/packaging/2013-July/009346.html
# https://fedorahosted.org/fpc/ticket/316
Conflicts:	dvb-apps < 1.1.2-6.1488.f3a70b206f0f

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

%files legacy
%license COPYING COPYING.LGPL
%{_datadir}/dvbv3/

%files
%license COPYING COPYING.LGPL
%{_datadir}/dvbv5/

%changelog
%autochangelog
