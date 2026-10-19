%global source0_hash aafed5ecfd33db8492d0a25f4d2da42a6db81c29c0202eaaf3575be3a10312b2
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/gin-contrib/sse
Version:                1.1.2
%gometa
%global common_description %{expand:
Server-sent events (SSE) is a technology where a browser receives automatic
updates from a server via HTTP connection. The Server-Sent Events EventSource
API is standardized as part of HTML5[1] by the W3C.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Server-sent events implementation in Go. used by the gin framework
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/sse-%{version}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/stretchr/testify/assert)
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
