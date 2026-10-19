%global source0_hash 15dc899ecc225e9b5514db2a44c620e652c8ad083df3167a7a722654596bcc5b
%bcond check 0
%global debug_package %{nil}
%global goipath         k8s.io/utils
%global forgeurl        https://github.com/kubernetes/utils
%global commit          bdf08cb9a70a05bd10b6fe605643a9cbab6effd5
%gometa
%global common_description %{expand:
A set of Go libraries that provide low-level, kubernetes-independent packages
supplementing the Go standard libs.}
%global golicenses      LICENSE
%global godocs          CONTRIBUTING.md HOWTOMOVE.md README.md code-of-\\\
                        conduct.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Non-Kubernetes-specific utility libraries consumed by multiple projects
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{forgeurl}/archive/%{commit}/utils-%{commit}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/davecgh/go-spew/spew)
BuildRequires:  golang(github.com/spf13/afero)
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(k8s.io/klog/v2)
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

%gocheck -d internal/third_party/forked/golang/net
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
