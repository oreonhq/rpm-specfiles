%global source0_hash b8fdcd67288f9a9b502c572d14af696dc634229162184f551cd368c77de7b321
%bcond check 0
%global debug_package %{nil}
%global goipath         k8s.io/gengo
%global forgeurl        https://github.com/kubernetes/gengo
%global commit          c02415ce41852193a7b49b79639ec83b8f517515
%gometa
%global common_description %{expand:
A package for generating things based on Go files. This mechanism was first used
in Kubernetes and is split out here for ease of reuse and maintainability.}
%global golicenses      LICENSE
%global godocs          examples CONTRIBUTING.md README.md code-of-conduct.md
%global gosupfiles      ${examples[@]}
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Gengo library for code generation
License:        Apache-2.0
URL:            %{gourl}
Source0:        %{forgeurl}/archive/%{commit}/gengo-%{commit}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/davecgh/go-spew/spew)
BuildRequires:  golang(github.com/google/gofuzz)
BuildRequires:  golang(github.com/spf13/pflag)
BuildRequires:  golang(golang.org/x/tools/imports)
BuildRequires:  golang(k8s.io/klog/v2)
BuildRequires:  golang(sigs.k8s.io/yaml)
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

%install
mapfile -t examples <<< $(find examples -type f)
%gopkginstall
%oreon_autofiles main
%if %{with check}
%check

%gocheck -d parser
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
