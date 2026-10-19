%global source0_hash c59266db0266a8b21fea6231eeb03d7d46c7bdd2d60009c351eb06436821d598
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/urfave/negroni
Version:                2.0.2
%gometa
%global goaltipaths     github.com/urfave/negroni/v2
%global common_description %{expand:
Idiomatic http middleware for golang.}
%global golicenses      LICENSE
%global godocs          CHANGELOG.md README.md translations/*.md
%global goaltipaths     github.com/codegangsta/negroni
Name:           %{goname}
Release:        1%{?dist}
Summary:        Idiomatic http middleware for Golang
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/negroni-%{version}.tar.gz
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
