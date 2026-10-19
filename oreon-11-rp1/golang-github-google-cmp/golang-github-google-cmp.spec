%global source0_hash c98f4f998ad8134b26816500b5c4c5cd6329905c0610b0c1f031efe7fbb469af
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/google/go-cmp
Version:                0.7.0
%gometa -L
%global common_description %{expand:
This package is intended to be a more powerful and safer alternative
to reflect.DeepEqual for comparing whether two values are semantically
equal.}
%global golicenses      LICENSE
%global godocs          CONTRIBUTING.md README.md
Name:           golang-github-google-cmp
Release:        1%{?dist}
Summary:        Package for comparing Go values in tests
License:        BSD-3-Clause
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/go-cmp-%{version}.tar.gz
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
