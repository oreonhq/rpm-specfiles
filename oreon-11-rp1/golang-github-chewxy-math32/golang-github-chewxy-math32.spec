%global source0_hash 52b9c4aa2d5bcd85a916271dee9ab5851ebeac29dfcd8a1199b81a9aeab04653
%ifarch x86_64
%bcond check 1
%else
%bcond check 0
%endif
%global debug_package %{nil}
%global goipath         github.com/chewxy/math32
Version:                1.11.1
%gometa -L -f
%global common_description %{expand:
A float32 version of Go's math package. The majority \
of code in this library is a thin float32 wrapper over \
the results of the math package that comes in the \
standard lib.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           golang-github-chewxy-math32
Release:        1%{?dist}
Summary:        A float32 version of Go's math package
License:        BSD-2-Clause
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/math32-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A

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
