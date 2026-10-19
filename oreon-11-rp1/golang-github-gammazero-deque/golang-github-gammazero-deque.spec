%global source0_hash c34b530b86a8956ac598168dda1b64b3b665ee398288223cb32a12f943a488fa
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/gammazero/deque
Version:                1.2.1
%gometa -L -f
%global common_description %{expand:
Fast ring-buffer deque (double-ended queue).}
%global golicenses      LICENSE
%global godocs          README.md
Name:           golang-github-gammazero-deque
Release:        1%{?dist}
Summary:        Fast ring-buffer deque (double-ended queue)
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/deque-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
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
