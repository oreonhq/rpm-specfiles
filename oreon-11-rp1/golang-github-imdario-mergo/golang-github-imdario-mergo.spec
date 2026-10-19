%global source0_hash ea63e957639684b877cecc85570c4e6bfda76315027bf86b61f0084a43482a8e
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/imdario/mergo
Version:                1.0.2
%gometa
%global common_description %{expand:
A helper to merge structs and maps in Golang. Useful for configuration default
values, avoiding messy if-statements.}
%global golicenses      LICENSE
%global godocs          CODE_OF_CONDUCT.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Tool to merge Go structs and maps
License:        BSD-3-Clause
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/mergo-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(gopkg.in/yaml.v3)
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

%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
