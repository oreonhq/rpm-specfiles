%global source0_hash cebdb837a242a4f4a50c2a5a834d64ecf0fb35d34c1f37e45b2db34651a87901
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/tv42/httpunix
%global commit          2ba4b9c3382c77e7b9ea89d00746e6111d142a22
%gometa
%global common_description %{expand:
Go library to talk http over unix domain sockets.}
%global golicenses      LICENSE
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Go library to talk http over unix domain sockets
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/httpunix-%{commit}.tar.gz
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
