%global source0_hash b513db6e7cbebe001a24cddc2e063d21409f15b55d28915f7c626c708f9f792e
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/gofrs/flock
Version:                0.13.1
%gometa
%global common_description %{expand:
Flock implements a thread-safe sync.Locker interface for file locking. It also
includes a non-blocking TryLock() function to allow locking without blocking
execution.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Thread-safe file locking library in Go
License:        BSD-3-Clause
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/flock-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(gopkg.in/check.v1)
# /oreon:deps
%description %{common_description}

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
