%global source0_hash c087067d47c370a90ea68b6f13d6801fa3ae9d180fdb14b6ad9b9428fce80c3e
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
%bcond check 1
%global debug_package %{nil}
%global goipath         github.com/google/go-github
Version:                92.0.0
%gometa
%global goname golang-github-google-go-github
%global goaltipaths     github.com/google/go-github/v55
%global common_description %{expand:
Go library for accessing the GitHub v3 API.}
%global golicenses      LICENSE
%global godocs          AUTHORS CONTRIBUTING.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Go library for accessing the GitHub v3 API
License:        BSD-3-Clause
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/go-github-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%autopatch -p1
rm -rf example

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
