%global source0_hash 7eba1906f39a764281c7dab8ebc3383240430b6330563998e3ce4fb6eb13e54c
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/docopt/docopt.go
Version:                0.6.2
%global commit          ee0de3bc6815ee19d4a46c7eb90f829db0e014b1
%gometa
%global goaltipaths         github.com/docopt/docopt-go
%global common_description %{expand:
An implementation of Docopt in the Go programming language.
Docopt helps you create beautiful command-line interfaces easily}
%global golicenses      LICENSE
%global godocs          examples README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Command-line arguments parser in Go
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/docopt.go-%{commit}.tar.gz
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
