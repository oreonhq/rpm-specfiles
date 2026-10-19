%global source0_hash 8fc80a9a315803c46005cd603aaef74cf0622905d8206ecd9dffe22aa0500c21
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/daviddengcn/go-assert
%global commit          ba7e68aeeff6e81e6a7699c9e603d342e4b2b919
%gometa
%global common_description %{expand:
Testing utils for Go.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Testing utils for Go
License:        BSD-3-Clause
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/go-assert-%{commit}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/daviddengcn/go-algs/ed)
BuildRequires:  golang(github.com/daviddengcn/go-villa)
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
