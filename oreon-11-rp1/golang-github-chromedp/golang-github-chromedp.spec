%global source0_hash bd7689a02d9c99d46ef063b2259e4b6f4cef2fc505c2e5eaa91af04277a0db2f
%ifarch x86_64
%bcond check 0
%else
%bcond check 1
%endif
%global debug_package %{nil}
%global goipath         github.com/chromedp/chromedp
Version:                0.16.0
%gometa
%global common_description %{expand:
A faster, simpler way to drive browsers supporting the Chrome DevTools
Protocol.}
%global goextensions    js
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Drive browsers supporting the Chrome DevTools Protocol
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/chromedp-%{version}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  chromium
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/chromedp/cdproto)
BuildRequires:  golang(github.com/gobwas/ws)
BuildRequires:  golang(github.com/mailru/easyjson)
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

%install
%gopkginstall
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
