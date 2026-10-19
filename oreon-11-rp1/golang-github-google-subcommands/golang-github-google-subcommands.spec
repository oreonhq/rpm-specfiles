%global source0_hash 99602409506274003f52f6eb901f3a4d6aa2fc041971939dfa753ffcf0549bae
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/google/subcommands
Version:                1.2.0
%gometa
%global common_description %{expand:
Subcommands is a Go package that implements a simple way for a single command to
have many subcommands, each of which takes arguments and so forth.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Go subcommand library
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/subcommands-%{version}.tar.gz
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
