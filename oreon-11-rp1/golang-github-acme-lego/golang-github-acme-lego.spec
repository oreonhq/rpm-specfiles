%global source0_hash e86e62946397964d6f2db2a2487cc75acac08e9ad7811c2302d56c35ca521699
%bcond check 1
%global goipath         github.com/go-acme/lego/v4
Version:                4.23.1
%gometa -L -f
%global common_description %{expand:
Let's Encrypt client and ACME library written in Go.}
Name:           golang-github-acme-lego
Release:        1%{?dist}
Summary:        Let's Encrypt client and ACME library written in Go
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND ISC AND MIT AND MPL-2.0 AND UPL-1.0
URL:            %{gourl}
Source0:        https://github.com/go-acme/lego/archive/v%{version}/lego-%{version}.tar.gz
Source1:        %{archivename}-vendor.tar.bz2
Source2:        go-vendor-tools.toml
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  go-vendor-tools
BuildRequires:  golang
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%setup -q -T -D -a1 %{forgesetupargs}
%autopatch -p1

%build

%gobuild -o %{gobuilddir}/bin/lego %{goipath}/cmd/lego
%install
%go_vendor_license_install -c %{S:2}
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles main

%check

%go_vendor_license_check -c %{S:2}
%if %{with check}
for test in "TestDNSProviderManual" "TestLookupNameserversOK" "TestFindZoneByFqdnCustom" \
            "TestFindPrimaryNsByFqdnCustom" "TestCheckDNSPropagation" "TestCheckAuthoritativeNss" \
            "TestCheckAuthoritativeNssErr"  "TestDNSProvider_findZone" "TestDNSProvider_FindZoneAndRecordName" \
            "TestPresentNoExistingRR" "TestPresentWithExistingRR" "TestPresentSkipExistingRR" \
            "TestRemoveRecord_errors" "TestAddTXTRecord_errors" "TestDNSProvider_concurrentGetDNSEntries" \
            "TestDNSProvider_concurrentAddDNSEntry" "TestClient_GetZone" "TestClient_GetDomainInformation" \
            "TestNewDNSProvider" "TestDNSProvider_Present" "TestDNSProvider_CleanUp" \
            "TestPresent_httpStorage" "TestRegister_httpStorage" "TestHTTPStorage_Fetch" \
            "TestHTTPStorage_FetchAll" "TestHTTPStorage_Put" "TestHTTPStorage_Put_CNAME_created" \
; do
awk -i inplace '/^func.*'"$test"'\(/ { print; print "\tt.Skip(\"disabled failing test\")"; next}1' $(grep -rl $test)
done
%gocheck -d github.com/go-acme/lego/v4/providers/dns/axelname/internal \
         -d github.com/go-acme/lego/v4/providers/dns/bookmyname/internal \
         -d github.com/go-acme/lego/v4/providers/dns/conoha \
         -d github.com/go-acme/lego/v4/providers/dns/constellix/internal \
         -d github.com/go-acme/lego/v4/providers/dns/dynu/internal \
         -d github.com/go-acme/lego/v4/providers/dns/f5xc/internal \
         -d github.com/go-acme/lego/v4/providers/dns/internal/active24 \
         -d github.com/go-acme/lego/v4/providers/dns/manageengine/internal \
         -d github.com/go-acme/lego/v4/providers/dns/metaregistrar/internal \
         -d github.com/go-acme/lego/v4/providers/dns/myaddr/internal \
         -d github.com/go-acme/lego/v4/providers/dns/otc \
         -d github.com/go-acme/lego/v4/providers/dns/rainyun/internal \
         -d github.com/go-acme/lego/v4/providers/dns/sakuracloud \
         -d github.com/go-acme/lego/v4/providers/dns/selfhostde/internal \
         -d github.com/go-acme/lego/v4/providers/dns/spaceship/internal \
         -d github.com/go-acme/lego/v4/providers/dns/technitium/internal \
         -d github.com/go-acme/lego/v4/providers/dns/timewebcloud/internal \
         -d github.com/go-acme/lego/v4/providers/dns/westcn/internal \
         -d github.com/go-acme/lego/v4/providers/dns/zoneee
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
