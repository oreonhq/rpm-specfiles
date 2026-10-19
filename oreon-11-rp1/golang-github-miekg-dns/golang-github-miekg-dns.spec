%global source0_hash 7aa6cfd69a1235ab2b3f9fc2015a2d8d92068d4a241283cb7ac5d6d22c9b84a5
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/miekg/dns
Version:                1.1.73
%gometa -L
%global common_description %{expand:
Complete and usable DNS library. All Resource Records are supported, including
the DNSSEC types. It follows a lean and mean philosophy. If there is stuff you
should know as a DNS programmer there isn't a convenience function for it.
Server side and client side programming is supported, i.e. you can build servers
and resolvers with it.}
%global golicenses      COPYRIGHT LICENSE
%global godocs          AUTHORS CONTRIBUTORS README.md
Name:           golang-github-miekg-dns
Release:        1%{?dist}
Summary:        DNS library in Go
License:        BSD-3-Clause
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/dns-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
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
