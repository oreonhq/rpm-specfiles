%global source0_hash 765ee8c9cb61af9171c368f2023e42214dc1be23e0aff0af6d1a1069be8b3603
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/go-stack/stack
Version:                1.8.1
%gometa
%global common_description %{expand:
Package Stack implements utilities to capture, manipulate, and format call
stacks. It provides a simpler API than package runtime.
The implementation takes care of the minutia and special cases of interpreting
the program counter (pc) values returned by runtime.Callers.}
%global golicenses      LICENSE.md
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Capture, manipulate, and format call stacks
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/stack-%{version}.tar.gz
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
