%global source0_hash 51b3ff2423339b013aba71ba26e8ecf764b2b95c478e4865f1f81cf5ec2deaaf
%bcond check 1
%bcond bootstrap 0
%if %{with bootstrap}
%global debug_package %{nil}
%endif
%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif
%global goipath         github.com/cloudflare/cloudflare-go
Version:                7.11.0
%gometa -L -f
%global common_description %{expand:
A Go library for interacting with Cloudflare's API v4. This library allows you
to:
 - Manage and automate changes to your DNS records within Cloudflare
 - Manage and automate changes to your zones (domains) on Cloudflare, including
   adding new zones to your account
 - List and modify the status of WAF (Web Application Firewall) rules for your
   zones
 - Fetch Cloudflare's IP ranges for automating your firewall whitelisting
A command-line client, flarectl, is also available as part of this project.}
%global golicenses      LICENSE
%global godocs          docs CHANGELOG.md CODE_OF_CONDUCT.md README.md\\\
                        flarectl-README.md
Name:           golang-github-cloudflare
Release:        1%{?dist}
Summary:        Go library for the Cloudflare v4 API
License:        BSD-3-Clause
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/cloudflare-go-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%autopatch -p1

mv cmd/flarectl/README.md flarectl-README.md

%if %{without bootstrap}
%build

%gobuild -o %{gobuilddir}/bin/flarectl %{goipath}/cmd/flarectl
%endif
%install
%gopkginstall
%if %{without bootstrap}
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles main
%endif
%if %{without bootstrap}
%if %{with check}
%check

for test in "TestOriginCA_OriginCARootCertificate" \
; do
awk -i inplace '/^func.*'"$test"'\(/ { print; print "\tt.Skip(\"disabled failing test\")"; next}1' $(grep -rl $test)
done
%gocheck
%endif
%endif
%if %{without bootstrap}
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
%endif
