%global source0_hash e1d28e0a658603681dcb43f9a8dc77691a639db51f66b1ed345aa261872faf4c
%bcond check 1
%bcond bootstrap 1
%global debug_package %{nil}
%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif
%global goipath         github.com/aws/aws-sdk-go-v2
Version:                20250103
%global tag             release-2025-01-03
%global distprefix      %{nil}
%gometa -f
%global common_description %{expand:
AWS SDK for the Go programming language.}
%global golicenses      LICENSE.txt NOTICE.txt
%global godocs          example CHANGELOG.md CODE_OF_CONDUCT.md\\\
                        CONTRIBUTING.md DESIGN.md README.md
Name:           golang-github-aws-sdk-2
Release:        1%{?dist}
Summary:        AWS SDK for the Go programming language
License:        BSD-3-Clause AND Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{tag}/aws-sdk-go-v2-%{tag}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

%goprep -A
%autopatch -p1

%if %{without bootstrap}
%install
%gopkginstall
%oreon_autofiles main
%if %{without bootstrap}
%if %{with check}
%check

%gocheck
%endif
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
%endif
