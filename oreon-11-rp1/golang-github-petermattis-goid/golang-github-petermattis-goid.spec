%global source0_hash d2c9714a2b765eb0615ea675b1141401eafda0eec36338773636cebcd5a9877a
%bcond check 1
%bcond bootstrap 0
%global debug_package %{nil}
%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif
%global goipath         github.com/petermattis/goid
%global commit          a731cc31b4fe99408872ab3e587b5972f29ff929
%gometa -L -f
%global common_description %{expand:
Programatically retrieve the current goroutine's ID.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           golang-github-petermattis-goid
Version:        0
Release:        1%{?dist}
Summary:        Programatically retrieve the current goroutine's ID
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/goid-%{commit}.tar.gz
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
