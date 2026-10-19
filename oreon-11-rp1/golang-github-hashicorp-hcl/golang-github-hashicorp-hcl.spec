%global source0_hash 50632428210503070fd2fde748c88b7414bf84a6a0eadebf9d8e596a033bead2
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/hashicorp/hcl
Version:                1.0.0
%gometa -L
%global common_description %{expand:
HCL (HashiCorp Configuration Language) is a configuration language built by
HashiCorp. The goal of HCL is to build a structured configuration language that
is both human and machine friendly for use with command-line tools, but
specifically targeted towards DevOps tools, servers, etc.
HCL is also fully JSON compatible. That is, JSON can be used as completely valid
input to a system expecting HCL. This helps makes systems interoperable with
other systems.
HCL is heavily inspired by libucl, nginx configuration, and others similar.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           golang-github-hashicorp-hcl
Release:        1%{?dist}
Summary:        Hashicorp configuration language
License:        MPL-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/hcl-%{version}.tar.gz
Patch:          https://patch-diff.githubusercontent.com/raw/hashicorp/hcl/pull/267.patch#/0001-Fixes-some-tests-descriptions.patch
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
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
