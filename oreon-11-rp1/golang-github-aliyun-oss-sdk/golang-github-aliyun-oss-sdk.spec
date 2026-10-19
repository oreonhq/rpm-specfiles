%global source0_hash 5a17697d860320995fc948d96695b56c837c5d0b8e576a607f3361038eba72d3
%bcond check 1
%global debug_package %{nil}
%global goipath         github.com/aliyun/aliyun-oss-go-sdk
Version:                3.0.2
%gometa
%global common_description %{expand:
Alibaba Cloud OSS SDK for Go.}
%global golicenses      LICENSE
%global godocs          CHANGELOG.md README-CN.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Alibaba Cloud OSS SDK for Go
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/aliyun-oss-go-sdk-%{version}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/aliyun/alibaba-cloud-sdk-go/services/kms)
BuildRequires:  golang(github.com/baiyubin/aliyun-sts-go-sdk/sts)
BuildRequires:  golang(golang.org/x/time/rate)
BuildRequires:  golang(gopkg.in/check.v1)
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
