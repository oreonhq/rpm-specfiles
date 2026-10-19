%global source0_hash 9085ccd724f6bc6b01975341501eb8e4951c3e8e4d48ef94ffdf38193f11dbab
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/brunoscheufler/aws-ecs-metadata-go
%global forgeurl        https://github.com/brunoscheufler/aws-ecs-metadata-go
%global commit          67e37ae746cd12f6ddd5dbebd31ff4a1ecd062cf
%gometa
%global common_description %{expand:
A minimal wrapper library to fetch Elastic Container Service (ECS) Task metadata
from any Go service running in container provisioned by AWS Fargate.
Based on the Fargate platform version, you'll have access to different versions
of the Task Metadata Endpoint. If you're running on 1.4.0, you'll be able to
access Version 4, Fargate 1.3.0 and later support Version 3 of the endpoint.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Retrieve AWS ECS Task metadata
License:        MIT
URL:            %{gourl}
Source0:        %{forgeurl}/archive/%{commit}/aws-ecs-metadata-go-%{commit}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%autopatch -p1

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
