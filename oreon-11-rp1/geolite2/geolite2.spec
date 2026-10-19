%global source0_hash 19eb1c04e53989baa1292cbd3b3d0e9904f69be2ac64549163f857fdda73501e
%global source1_hash 798732869a88bfda98b9a15f870564ea8a5a6969754767175978195fdf87382d
%global source2_hash 7ce2f6f453ee36dfd154b3eb1f7e1b8f7ea0248cb655bf25a39d7bfa86c4abe0
%global common_description %{expand:
GeoLite2 databases are free IP geolocation databases comparable to, but less
accurate than, MaxMind's GeoIP2 databases.  This product includes GeoLite2 data
created by MaxMind, available from http://www.maxmind.com.}
Name:           geolite2
Version:        20191217
Release:        16%{?dist}
Summary:        Free IP geolocation databases
License:        CC-BY-SA-4.0 AND CC-BY-3.0
URL:            https://dev.maxmind.com/geoip/geoip2/geolite2/
Source0:        https://github.com/P3TERX/GeoLite.mmdb/raw/download/GeoLite2-ASN.mmdb
Source1:        https://github.com/P3TERX/GeoLite.mmdb/raw/download/GeoLite2-City.mmdb
Source2:        https://github.com/P3TERX/GeoLite.mmdb/raw/download/GeoLite2-Country.mmdb
BuildArch:      noarch
# oreon:deps

# /oreon:deps
%description %{common_description}

%package asn
Summary:        Free IP geolocation ASN database
%description asn %{common_description}

%package city
Summary:        Free IP geolocation city database
%description city %{common_description}

%package country
Summary:        Free IP geolocation country database
%description country %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
test "%{source2_hash}" = "none" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source2_hash}" || { echo "oreon: Source2 hash mismatch" >&2; exit 1; }; }

%install
install -D -p -m 0644 %{SOURCE0} %{buildroot}%{_datadir}/GeoIP/GeoLite2-ASN.mmdb
install -D -p -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/GeoIP/GeoLite2-City.mmdb
install -D -p -m 0644 %{SOURCE2} %{buildroot}%{_datadir}/GeoIP/GeoLite2-Country.mmdb
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n geolite2-asn -f %{oreon_filedir}/geolite2-asn.list
%files -n geolite2-city -f %{oreon_filedir}/geolite2-city.list
%files -n geolite2-country -f %{oreon_filedir}/geolite2-country.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 20191217-16
- Import
