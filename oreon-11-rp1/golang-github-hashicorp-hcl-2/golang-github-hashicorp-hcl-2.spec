%global source0_hash a2cc385ada570cea4e623c4e7eae862e1a920482e91fb08d24590fc1c546e8d1
%bcond check 1
%bcond bootstrap 0
%global debug_package %{nil}
%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif
%global goipath         github.com/hashicorp/hcl/v2
Version:                2.25.0
%gometa -f
%global common_description %{expand:
HCL (HashiCorp Configuration Language) is a configuration language built by
HashiCorp. The goal of HCL is to build a structured configuration language that
is both human and machine friendly for use with command-line tools, but
specifically targeted towards DevOps tools, servers, etc..}
%global golicenses      LICENSE
%global godocs          CHANGELOG.md README.md spec.md
Name:           golang-github-hashicorp-hcl-2
Release:        1%{?dist}
Summary:        HCL is the HashiCorp configuration language
License:        MPL-2.0
URL:            %{gourl}
Source0:        https://github.com/hashicorp/hcl/archive/v%{version}/hcl-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%autopatch -p1

rm -rf cmd hcldec/spec_test.go

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
