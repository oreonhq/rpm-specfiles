%global source0_hash c28cd954b9076f17d05f7ee3e2f566f3c66bf0112215d0e9f77cfc4cc644f4b0
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/markbates/oncer
Version:                1.0.0
%gometa
%global common_description %{expand:
Oncer for Go.}
%global golicenses      LICENSE
%global godocs          SHOULDERS.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Oncer for Go
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/oncer-%{version}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/stretchr/testify/require)
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
