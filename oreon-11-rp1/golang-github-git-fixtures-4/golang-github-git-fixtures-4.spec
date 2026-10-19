%global source0_hash de669304b6aaf46dd0f06dbc376f80e3303a858588113a06c3a64b7514500846
%ifnarch %{ix86} %{arm}
%bcond check 0
%endif
%global debug_package %{nil}
%global goipath         github.com/go-git/go-git-fixtures/v4
Version:                4.3.1
%gometa
%global common_description %{expand:
Several git fixtures to run go-git tests.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Several git fixtures to run go-git tests
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://github.com/go-git/go-git-fixtures/archive/v%{version}/go-git-fixtures-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description
%{common_description}

%prep

%goprep

%install
%gopkginstall
%oreon_autofiles main
%if %{with check}
%check

rm -rvf internal/tgz/tgz_test.go
%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
