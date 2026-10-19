%global source0_hash 5560d2c26b4329c7756fc6e2bbeb14320f66f25d49618ed55725bddf72790d95
%ifnarch s390x
%bcond check 0
%endif
%global debug_package %{nil}
%global goipath         github.com/xiang90/probing
Version:                0.0.2
%global tag             0.0.2
%gometa
%global common_description %{expand:
Go project for probing.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Go project for probing
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{version}/probing-%{version}.tar.gz
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
