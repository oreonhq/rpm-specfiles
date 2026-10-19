%global source0_hash 00056fa164b1bf217eb249f5733c76fd6e18f3f55ae269286695705243f48fe2
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/pborman/getopt
Version:                2.1.0
%gometa
%global common_description %{expand:
Package Getopt provides traditional getopt processing for implementing commands
that use traditional command lines. The standard Go flag package cannot be used
to write a program that parses flags the way ls or ssh does, for example.}
%global golicenses      LICENSE
%global godocs          AUTHORS CONTRIBUTING.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Getopt style option parsing for Go
License:        BSD
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/getopt-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
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
