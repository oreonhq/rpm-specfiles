%global source0_hash 28f3dc1b5c0efd61203ab07233f774740d3bf08da4d8153fb5310db6cea0ebda
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/pmezard/go-difflib
Version:                1.0.0
%gometa
%global godevelheader %{expand:
Obsoletes:      golang-github-pmezard-go-difflib-devel < 0-0.15
}
%global common_description %{expand:
Go-difflib is a partial port of python 3 difflib package. Its main goal is to
make unified and context diff available in pure Go, mostly for testing
purposes.}
%global golicenses      LICENSE
%global godocs          README.md
%global gosupfiles glide.lock glide.yaml
Name:           %{goname}
Release:        1%{?dist}
Summary:        Partial port of python difflib package to Go
License:        BSD
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/go-difflib-%{version}.tar.gz
Source1:        glide.yaml
Source2:        glide.lock
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
cp %{S:1} %{S:2} .

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
