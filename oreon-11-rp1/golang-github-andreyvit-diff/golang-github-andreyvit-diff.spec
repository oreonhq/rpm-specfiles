%global source0_hash 9128e34ca1a5446d76ecc6aa409a7b4d47f21e9ddf544810921687db143b78ad
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/andreyvit/diff
%global commit          c7f18ee00883bfd3b00e0a2bf7607827e0148ad4
%gometa
%global common_description %{expand:
Diff provides quick and easy string diffing functions based on
github.com/sergi/go-diff, mainly for diffing strings in tests.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Quick'n'easy string diffs for Go, mainly for diffing strings in tests
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/diff-%{commit}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/sergi/go-diff/diffmatchpatch)
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
