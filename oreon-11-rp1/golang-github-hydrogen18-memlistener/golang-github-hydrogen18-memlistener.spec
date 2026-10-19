%global source0_hash ea0cb3af7e1fc1e8b7ffd655f981bfb6cc5412071b14f1f5c3c609c5be01cbce
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/hydrogen18/memlistener
%global commit          dcc25e7acd91be02da6708e2fccafaa726375ac4
%gometa
%global common_description %{expand:
An in memory listener for testing socket & HTTP servers in Golang.}
%global golicenses      LICENSE
%global godocs          example
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        An in memory listener for testing socket & HTTP servers in Golang
License:        LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/memlistener-%{commit}.tar.gz
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
