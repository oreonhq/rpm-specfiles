%global source0_hash a124688b8755f715fc0f105ad9681601a3cb820a3cff81915d693a08cef44f70
%bcond check 1
%bcond bootstrap 0
%global debug_package %{nil}
%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif
%global goipath         github.com/jba/templatecheck
Version:                0.7.1
%gometa -L -f
%global common_description %{expand:
Checking Go templates for validity.}
%global golicenses      LICENSE
%global godocs          README.md TODO.txt
Name:           golang-github-jba-templatecheck
Release:        1%{?dist}
Summary:        Checking Go templates for validity
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/templatecheck-%{version}.tar.gz
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
