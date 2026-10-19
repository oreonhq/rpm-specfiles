%global source0_hash 5b7a6c2c25b305b83cf55309358833708fbd4555c0c1a47a0a5c20030abd0fba
%bcond check 1
%bcond bootstrap 0
%global debug_package %{nil}
%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif
%global goipath         github.com/junegunn/go-shellwords
%global commit          2aa3b3277741a6ad31883f223d770221a85e9dd0
%gometa -L -f
%global common_description %{expand:
Parse line as shell words.}
%global golicenses      LICENSE
%global godocs          _example README.md
Name:           golang-github-junegunn-shellwords
Version:        0
Release:        1%{?dist}
Summary:        Parse line as shell words
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/go-shellwords-%{commit}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%autopatch -p1

%if %{without bootstrap}
%install
%gopkginstall
%oreon_autofiles main
%if %{without bootstrap}
%if %{with check}
%check

%gocheck
%endif
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
%endif
