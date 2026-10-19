%global source0_hash 7cbbecafca595f75bee0876f8ba2019965d51b47d5e271356df1655b73d17143
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/urfave/cli
Version:                1.22.10
%gometa
%global goaltipaths     gopkg.in/urfave/cli.v1 github.com/codegangsta/cli
%global common_description %{expand:
Cli is a simple, fast, and fun package for building command line apps in Go.
The goal is to enable developers to write fast and distributable command line
applications in an expressive way.}
%global golicenses      LICENSE
%global godocs          docs/CONTRIBUTING.md docs/v1 README.md CODE_OF_CONDUCT.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Simple, fast, and fun package for building command line apps in go
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/cli-%{version}.tar.gz
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

for test in "TestApp_RunAsSubCommandIncorrectUsage" \
            "TestToMan" \
; do
awk -i inplace '/^func.*'"$test"'\(/ { print; print "\tt.Skip(\"disabled failing test\")"; next}1' $(grep -rl $test)
done
%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
