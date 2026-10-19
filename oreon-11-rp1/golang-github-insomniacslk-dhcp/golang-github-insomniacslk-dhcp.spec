%global source0_hash 5c33b86b8aa77ee7bcc7dd45397f3522f70f83de4ef44fc732db8a2f903c459c
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/insomniacslk/dhcp
%global commit          8c70d406f6d24a17219a5f543174c1f3f3ad9e35
%gometa -f
%global common_description %{expand:
DHCPv6 and DHCPv4 packet library, client and server written in Go.}
%global golicenses      LICENSE
%global godocs          examples CONTRIBUTORS.md README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        DHCPv6 and DHCPv4 packet library, client and server written in Go
License:        BSD-3-Clause
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/dhcp-%{commit}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%autopatch -p1

%install
%gopkginstall
%oreon_autofiles main
%if %{with check}
%check

%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
