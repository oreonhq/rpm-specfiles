%global source0_hash d0ca030c0a3a9283d5945f5576877f08becdbf2b983e12a634d0597a1a1678b5
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/bshuster-repo/logrus-logstash-hook
Version:                1.1.0
%gometa
%global common_description %{expand:
Use this hook to send the logs to Logstash.}
%global golicenses      LICENSE
%global godocs          CHANGELOG.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Logstash hook for logrus
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/logrus-logstash-hook-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/sirupsen/logrus)
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
