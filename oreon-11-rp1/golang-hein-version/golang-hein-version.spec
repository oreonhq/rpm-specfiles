%global source0_hash 155ec485711bc4df3a61e9934d3700da516211f26d0ca9603ebb2cd5ee4f2037
%bcond check 0
%global debug_package %{nil}
%global goipath         go.hein.dev/go-version
%global forgeurl        https://github.com/christopherhein/go-version
Version:                0.1.0
%gometa
%global common_description %{expand:
This package gives allows you to use https://github.com/spf13/cobra and
https://github.com/goreleaser/goreleaser together to output your version in a
simple way. Supporting multiple flags for mutating the output.}
%global golicenses      LICENSE.txt
%global godocs          example CHANGELOG.md readme.adoc
Name:           %{goname}
Release:        1%{?dist}
Summary:        Golang Cobra & Goreleaser Versioning library
License:        Apache-2.0
URL:            %{gourl}
Source0:        %{forgeurl}/archive/v%{version}/go-version-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/mitchellh/go-homedir)
BuildRequires:  golang(github.com/spf13/cobra)
BuildRequires:  golang(github.com/spf13/viper)
BuildRequires:  golang(sigs.k8s.io/yaml)
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
