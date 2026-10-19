%global source0_hash 363140ddedf035ef012e0b17a35d32210f51b7f160c3fb0e89d08aa83d1870e0
%bcond check 1
%global debug_package %{nil}
%global goipath         github.com/facebookgo/clock
%global commit          600d898af40aa09a7a93ecb9265d87b0504b6f03
%gometa
%global common_description %{expand:
Clock is a small library for mocking time in Go.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Version:        1.90.0
Release:        1%{?dist}
Summary:        Clock is a small library for mocking time in Go
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/clock-%{commit}.tar.gz
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
