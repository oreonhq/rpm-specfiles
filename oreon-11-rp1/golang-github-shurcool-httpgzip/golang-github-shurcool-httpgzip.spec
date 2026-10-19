%global source0_hash 0eb6a7686cd89456487c2ab0079a93613d98507dd6e057cb579e61d4ccaad589
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/shurcooL/httpgzip
%global commit          320755c1c1b0484e6179c9a5b68aabcc0dae5ac2
%gometa
%global common_description %{expand:
Package httpgzip provides net/http-like primitives that use gzip compression
when serving HTTP requests.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Net/http-like primitives that use gzip compression when serving HTTP requests
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/httpgzip-%{commit}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(golang.org/x/net/http/httpguts)
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
