%global source0_hash 89045d1f52e12a4ca6b3297c769e17bdde0c1000a6f8c8290fa3bda9f99d0851
%bcond check 1
%global debug_package %{nil}
%global goipath         github.com/denverdino/aliyungo
%global commit          a47aa053adf73343a00aab48f200128eaf5540e6
%gometa
%global common_description %{expand:
This is an unofficial Go SDK for Aliyun services.}
%global golicenses      LICENSE.txt
%global godocs          README.md
%global gosupfiles      glide.lock glide.yaml
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Go SDK for Aliyun (Alibaba Cloud)
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/aliyungo-%{commit}.tar.gz
Source1:        glide.yaml
Source2:        glide.lock
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/golang/protobuf/proto)
BuildRequires:  golang(github.com/magiconair/properties/assert)
BuildRequires:  golang(golang.org/x/text/encoding/simplifiedchinese)
BuildRequires:  golang(golang.org/x/text/transform)
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
