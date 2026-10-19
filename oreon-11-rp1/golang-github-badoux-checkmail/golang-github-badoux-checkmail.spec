%global source0_hash 910a5a470224bbbea3165a02fabb6872f78dc945d032bd299e11029b4523b280
%bcond check 0
%bcond_with network
%global debug_package %{nil}
%global goipath         github.com/badoux/checkmail
Version:                1.2.4
%gometa
%global common_description %{expand:
Golang package for email validation.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Golang package for email validation
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/checkmail-%{version}.tar.gz
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

%if %{without network}
%global gotestflags %{?gotestflags} -run TestValidateFormat
%endif
%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
