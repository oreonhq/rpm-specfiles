%global source0_hash 95ef6e8c4d877d1bcb4d4cd8e917c56faba847bba86b3c91e869636ad008bf41
%bcond check 0
%global debug_package %{nil}
%global goipath         dario.cat/mergo
%global forgeurl        https://github.com/imdario/mergo
Version:                1.0.0
%gometa
%global goaltipaths     github.com/imdario/mergo
%global common_description %{expand:
A helper to merge structs and maps in Golang. Useful for configuration default
values, avoiding messy if-statements.}
%global golicenses      LICENSE
%global godocs          CODE_OF_CONDUCT.md CONTRIBUTING.md README.md\\\
                        SECURITY.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Tool to merge Go structs and maps
License:        BSD-3-Clause
URL:            %{gourl}
Source0:        %{forgeurl}/archive/v%{version}/mergo-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
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
