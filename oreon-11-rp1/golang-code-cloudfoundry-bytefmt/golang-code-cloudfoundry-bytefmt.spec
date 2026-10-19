%global source0_hash 07ef9a41af33b74f2855ce00255248ff681347b0df588c6b92d546795bdf5eab
%bcond check 0
%global debug_package %{nil}
%global goipath         code.cloudfoundry.org/bytefmt
%global forgeurl        https://github.com/cloudfoundry/bytefmt
%global commit          41ef4d1f67a4f3fe3ba58a44a3230ea6228ab10c
%gometa
%global common_description %{expand:
Human readable byte formatter.}
%global golicenses      LICENSE NOTICE
%global godocs          README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Human readable byte formatter
License:        Apache-2.0
URL:            %{gourl}
Source0:        %{forgeurl}/archive/%{commit}/bytefmt-%{commit}.tar.gz
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
