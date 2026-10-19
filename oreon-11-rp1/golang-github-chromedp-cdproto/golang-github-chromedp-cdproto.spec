%global source0_hash 318573e41dff72fdddd94126269fb06f0ce680e177067de774fbd6a3c9d5342b
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/chromedp/cdproto
%global commit          3579568136296dcb43d7f4fde93600cb35d308cd
%gometa
%global common_description %{expand:
Package cdproto contains the generated commands, types, and events for the
Chrome DevTools Protocol domains.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Generated commands, types, and events for the Chrome DevTools Protocol domains
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/cdproto-%{commit}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

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
