%global source0_hash c44015cf1a4d24aa727fa33b7b35ff6cf3361ffa1a201b108b68d3a01b3234e1
%bcond check 0
%global debug_package %{nil}
%global goipath         gopkg.in/stack.v0
%global forgeurl        https://github.com/go-stack/stack
%global commit          9b43fcefddd0178abdabf4d484ab0d695d0011db
%gometa
%global common_description %{expand:
Package Stack implements utilities to capture, manipulate, and format call
stacks. It provides a simpler API than package runtime.
The implementation takes care of the minutia and special cases of interpreting
the program counter (pc) values returned by runtime.Callers.}
%global golicenses      LICENSE.md
%global godocs          README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Utilities to capture, manipulate, and format call stacks
License:        Apache-2.0
URL:            %{gourl}
Source0:        %{forgeurl}/archive/%{commit}/stack-%{commit}.tar.gz
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

rm stackinternal_test.go
%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
