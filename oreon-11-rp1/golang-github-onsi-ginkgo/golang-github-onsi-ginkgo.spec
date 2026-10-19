%global source0_hash 0380c81321b764b75e76a7aa8fc8ab1ab361232a88d5b6124ef8b9a9e75d5287
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/onsi/ginkgo
Version:                1.16.5
%gometa
%global common_description %{expand:
BDD Testing Framework for Go.}
%global golicenses      LICENSE
%global godocs          CHANGELOG.md CONTRIBUTING.md README.md RELEASING.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        BDD Testing Framework for Go
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/ginkgo-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

%install
%gopkginstall
%oreon_autofiles main
%if %{with check}
%check

export ACK_GINKGO_DEPRECATIONS=1.16.5
export ACK_GINKGO_RC=true
%gocheck -d integration
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
