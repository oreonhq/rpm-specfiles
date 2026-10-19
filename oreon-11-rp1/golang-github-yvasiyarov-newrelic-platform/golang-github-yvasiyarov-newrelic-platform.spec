%global source0_hash c65bda15b3429c54e2dbb1d50aa8661f85ec6bb1166852c3617bff97c95ea0fd
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/yvasiyarov/newrelic_platform_go
%global commit          9c099fbc30e90de5bb5c5f94aa5fd08f2daeaacd
%gometa
%global godevelheader %{expand:
Obsoletes:      golang-github-yvasiyarov-newrelic_platform_go-devel < 0-0.9
}
%global common_description %{expand:
This package provide very simple interface to NewRelic Platform.}
%global golicenses      LICENSE
%global godocs          examples README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Newrelic Platform SDK for Go
License:        LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/newrelic_platform_go-%{commit}.tar.gz
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
