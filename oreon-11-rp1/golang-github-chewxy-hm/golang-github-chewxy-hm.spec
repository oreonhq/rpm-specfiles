%global source0_hash a204f8d582e3374104a32f104b6002fbc6ea01b2208feb6a965153a76516f80f
%bcond check 1
%bcond bootstrap 0
%global debug_package %{nil}
%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif
%global goipath         github.com/chewxy/hm
Version:                1.0.0
%gometa -L -f
%global common_description %{expand:
A simple Hindley-Milner type system in Go.}
%global golicenses      LICENCE
%global godocs          README.md
Name:           golang-github-chewxy-hm
Release:        1%{?dist}
Summary:        A simple Hindley-Milner type system in Go
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/hm-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A

# example_greenspun_test.go:95:60: non-constant format string in call to fmt.Fprintf
rm example_greenspun_test.go
# hm_test.go:105:10: undefined: lit
rm hm_test.go

%if %{without bootstrap}
%install
%gopkginstall
%oreon_autofiles main
%if %{without bootstrap}
%if %{with check}
%check

%gocheck
%endif
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
%endif
