%global source0_hash cc6c27210fd2216a4150c940d0ab87c7d747a5bb85abf3bc4a51cbfb24ed3f76
%global source1_hash ea2a65d8dbbbae4e2e0df119dc38847c1100b929e5268943a541484facb56d6d
%global source2_hash 81e6a4caf98635746405f3c7d6a8d3e7a0698c0d12c03fdd5f8e45c86987d323

%global common_description %{expand:
GeoLite2 databases are free IP geolocation databases comparable to, but less
accurate than, MaxMind's GeoIP2 databases.  This product includes GeoLite2 data
created by MaxMind, available from http://www.maxmind.com.}


Name:           geolite2
# Upstream changed their license on 2019-12-30.  This is the last version
# released under CC-BY-SA.
# https://bugzilla.redhat.com/show_bug.cgi?id=1786211
Version:        20191217
Release:        16%{?dist}
Summary:        Free IP geolocation databases
# This work is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License
# This database incorporates GeoNames geographical data, which is made available under the Creative Commons Attribution 3.0 License
License:        CC-BY-SA-4.0 AND CC-BY-3.0
URL:            https://dev.maxmind.com/geoip/geoip2/geolite2/
Source0:        https://github.com/P3TERX/GeoLite.mmdb/raw/download/GeoLite2-ASN.mmdb
Source1:        https://github.com/P3TERX/GeoLite.mmdb/raw/download/GeoLite2-City.mmdb
Source2:        https://github.com/P3TERX/GeoLite.mmdb/raw/download/GeoLite2-Country.mmdb
BuildArch:      noarch


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


%files asn
%dir %{_datadir}/GeoIP
%verify(not md5 size mtime) %{_datadir}/GeoIP/GeoLite2-ASN.mmdb


%files city
%dir %{_datadir}/GeoIP
%verify(not md5 size mtime) %{_datadir}/GeoIP/GeoLite2-City.mmdb


%files country
%dir %{_datadir}/GeoIP
%verify(not md5 size mtime) %{_datadir}/GeoIP/GeoLite2-Country.mmdb


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 20191217-16
- Import
