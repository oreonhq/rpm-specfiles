%global source0_hash 76630734d2b77222b4c5d89b0fa36ee8ce4a1fa2acae3af6ede75c704104357a
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/google/shlex
%global commit          e7afc7fbc51079733e9468cdfd1efcd7d196cd1d
%gometa
%global common_description %{expand:
Go-shlex is a simple lexer for Go that supports shell-style quoting, commenting,
and escaping.}
%global golicenses      COPYING
%global godocs          README
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Automatically exported from code.google.com/p/go-shlex
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/shlex-%{commit}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

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
