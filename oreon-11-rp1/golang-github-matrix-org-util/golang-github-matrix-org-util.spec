%global source0_hash e1c85f85dab2119bec5b51d09f92b26695d6248cbe1aa088a26bbfff8c5f5c9e
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/matrix-org/util
%global commit          399730281e66400bbfa38220eeb874609fca6c55
%gometa -L -f
%global common_description %{expand:
A loose collection of Golang functions that we use at matrix.org.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           golang-github-matrix-org-util
Version:        0
Release:        1%{?dist}
Summary:        A loose collection of Golang functions that we use at matrix.org
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/util-%{commit}.tar.gz
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
