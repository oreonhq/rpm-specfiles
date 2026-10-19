%global source0_hash d01f2349b605a37db615d0a9454970bda9575d8ebe12bdd0c164f4d2717ab2bc
%bcond check 1
%bcond bootstrap 0
%global debug_package %{nil}
%global goipath         github.com/googleapis/enterprise-certificate-proxy
%global forgeurl        https://github.com/googleapis/enterprise-certificate-proxy
Version:                0.3.2
%gometa -L
%global common_description %{expand:
Repository for the Enterprise Certificate Proxy project.}
%global golicenses      LICENSE
%global godocs          CODE_OF_CONDUCT.md CONTRIBUTING.md README.md\\\
                        SECURITY.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Repository for the Enterprise Certificate Proxy project
License:        Apache-2.0
URL:            %{gourl}
Source0:        %{forgeurl}/archive/v%{version}/enterprise-certificate-proxy-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
rm -rfv internal linux windows client/client_test.go

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
