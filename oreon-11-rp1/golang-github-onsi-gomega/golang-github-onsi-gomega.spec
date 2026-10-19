%global source0_hash e46be4011571df2615dfc618007eebde5f4f9c9a14b817285de1ed795292cea2
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/onsi/gomega
Version:                1.44.0
%gometa -L
%global common_description %{expand:
Ginkgo's Preferred Matcher Library.}
%global golicenses      LICENSE
%global godocs          CHANGELOG.md CONTRIBUTING.md README.md RELEASING.md
Name:           golang-github-onsi-gomega
Release:        1%{?dist}
Summary:        Ginkgo's Preferred Matcher Library
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/gomega-%{version}.tar.gz
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

rm -rfv gexec/build_test.go
%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
