%global source1_hash 3e07c02046bf3c2a73f060636997e0323dbe92a2d4ba43ef9e6b05a1031ae4c4
%global source0_hash 578a6e2cc10cd9e188b9edbd9dfb762dae7d49e47c4f46637e6c7626641a5cef
%bcond check 1
%global debug_package %{nil}
%global goipath         gopkg.in/logex.v1
%global forgeurl        https://github.com/chzyer/logex
Version:                1.1.10
%gometa
%global godevelheader %{expand:
Obsoletes:      golang-github-chzyer-logex-devel < 1.1.10-9
}
%global goaltipaths     github.com/chzyer/logex
%global common_description %{expand:
A Golang log library, supports tracking and level, wrap by standard log lib.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Log library, supports tracking and level, wrap by standard log lib
License:        MIT
URL:            %{gourl}
Source0:        %{forgeurl}/archive/v%{version}/logex-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/chzyer/logex/master/LICENSE
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
cp %{S:1} .

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
