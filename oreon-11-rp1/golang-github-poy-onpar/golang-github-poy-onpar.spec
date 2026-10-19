%global source0_hash 197f5f9824e1a65bdc0b6c4707c5d32c401021b92b7e49c68e7330a3c96dbcd2
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
%bcond check 1
%global debug_package %{nil}
%global goipath         github.com/poy/onpar
Version:                3.0.0
%gometa -f
%global common_description %{expand:
Parallel testing framework for Go.}
%global golicenses      LICENSE
%global godocs          README.md expect/README.md matchers/README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Parallel testing framework for Go
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/onpar-%{version}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(git.sr.ht/~nelsam/hel/pkg/pers)
BuildRequires:  golang(git.sr.ht/~nelsam/hel/vegr)
BuildRequires:  golang(github.com/fatih/color)
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
