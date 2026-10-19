%global source0_hash ee3cc6cd71a8822f7c18b5486b4b81cb2c1a7c3b08027d17a722024873a9dfc1
%bcond check 1
%global debug_package %{nil}
%global goipath         github.com/op/go-logging
Version:                2.0.0
%global commit          970db520ece77730c7e4724c61121037378659d9
%gometa
%global common_description %{expand:
Package Logging implements a logging infrastructure for Go. Its output format is
customizable and supports different logging backends like syslog, file and
memory. Multiple backends can be utilized with different log levels per backend
and logger.}
%global golicenses      LICENSE
%global godocs          examples CONTRIBUTORS README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Golang logging library
License:        LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/go-logging-%{commit}.tar.gz
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
