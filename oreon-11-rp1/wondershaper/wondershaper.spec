%global source0_hash 83934b012bb510f66db0d289f3751fb98f501da53dc009c43d29400b53cc5978

Name:		wondershaper
Version:	1.2.1
Release:	26%{?dist}
Summary:	Simple Network Shaper
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		http://sourceforge.net/projects/wondershaper/
Source:		http://downloads.sourceforge.net/project/wondershaper/%{name}-%{version}.tar.gz
Requires:	iproute
Requires:	kernel-modules-extra
BuildArch:	noarch

%description
Many cable-modem and ADSL users experience horrifying latency
while uploading or downloading. They also notice that uploading
hampers downloading greatly. The Wondershaper neatly addresses
these issues, allowing users of a router with a Wondershaper to
continue using SSH over a loaded link happily.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
# Nothing to build.

%install
install -pDm 755 wshaper %{buildroot}/%{_sbindir}/%{name}

%files
%doc ChangeLog README
%license COPYING
%{_sbindir}/%{name}

%changelog
%autochangelog
