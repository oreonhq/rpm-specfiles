%global source0_hash b862bc662d38bcb1cff65d47c65e82ddb6294debf7272a3f9107aee2c5134ce1
%bcond check 1
%bcond bootstrap 1
%global debug_package %{nil}
%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif
%global goipath         github.com/aws/aws-sdk-go
Version:                1.55.8
%gometa
%global common_description %{expand:
Aws-sdk-go is the official AWS SDK for the Go programming language.}
%global golicenses      LICENSE.txt NOTICE.txt
%global godocs          example CHANGELOG_PENDING.md CODE_OF_CONDUCT.md CONTRIBUTING.md README.md CHANGELOG.MIGRATION_GUIDE
Name:           %{goname}
Release:        1%{?dist}
Summary:        AWS SDK for the Go programming language
License:        BSD-3-Clause AND Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/aws-sdk-go-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description
%{common_description}

%prep

%goprep

%if %{without bootstrap}
%install
%gopkginstall
%oreon_autofiles main
%if %{without bootstrap}
%if %{with check}
%check

%gocheck -d aws/session
%endif
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
%endif
