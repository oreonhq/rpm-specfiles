%global source0_hash 22abd8126261ef47d92e3faa4100b7a309eb9be6c2a709b4268d81b85cc48768
%bcond check 1
%bcond bootstrap 0
%global debug_package %{nil}
%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif
%global goipath         k8s.io/klog/v2
%global forgeurl        https://github.com/kubernetes/klog
Version:                2.130.1
%gometa -L -f
%global common_description %{expand:
Leveled execution logs for Go.}
%global golicenses      LICENSE
%global godocs          examples CONTRIBUTING.md README.md RELEASE.md\\\
                        SECURITY.md code-of-conduct.md klogr-README.md\\\
                        example
Name:           golang-k8s-klog2
Release:        1%{?dist}
Summary:        Leveled execution logs for Go
License:        Apache-2.0
URL:            %{gourl}
Source0:        %{forgeurl}/archive/v%{version}/klog-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%autopatch -p1

# Remove to avoid extra deps
rm -rvf examples

mv klogr/README.md klogr-README.md

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
