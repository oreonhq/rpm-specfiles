%global source0_hash c77b45b267ac5f5e03d00ab1b3f944d68c74e91601a1c8121e49040ff89d8b0a
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/frankban/quicktest
Version:                1.14.6
%gometa
%global common_description %{expand:
Quick helpers for testing Go applications.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Quick helpers for testing Go applications
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/quicktest-%{version}.tar.gz
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
