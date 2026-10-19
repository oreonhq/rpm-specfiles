%global source0_hash 7f5a9e8aff8bff4ab6764f23db05f6c3414150463227180465df490039c0073d
%bcond check 0
%global goipath         github.com/kardianos/service
Version:                1.3.0
%global debug_package   %{nil}
%gometa
%global common_description %{expand:
service will install / un-install, start / stop, and run a program as a
service (daemon). Currently supports Windows XP+, Linux/(systemd | Upstart |
SysV), and OSX/Launchd.}
%global golicenses      LICENSE
%global godocs          example README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Run go programs as a service on major platforms
License:        zlib
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/service-%{version}.tar.gz
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

%gocheck -d .
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
