%global source0_hash 3fcfc288f7f94c1ed1cea1f003fa40cb6caab4164c5a0fb74db137080934a520
%bcond check 0
%global debug_package %{nil}
%global goipath         sigs.k8s.io/structured-merge-diff
%global forgeurl        https://github.com/kubernetes-sigs/structured-merge-diff
Version:                4.2.1
%gometa
%global goaltipaths     sigs.k8s.io/structured-merge-diff/v4
%global common_description %{expand:
This package contains code which implements the Kubernetes "apply" operation.}
%global golicenses      LICENSE
%global godocs          CONTRIBUTING.md README.md RELEASE.md code-of-\\\
                        conduct.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Test cases and implementation for "server-side apply"
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{forgeurl}/archive/v%{version}/structured-merge-diff-%{version}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/google/gofuzz)
BuildRequires:  golang(github.com/json-iterator/go)
BuildRequires:  golang(gopkg.in/yaml.v2)
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
