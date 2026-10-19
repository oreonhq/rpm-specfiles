%global source0_hash 40ca501c67cebe005bb168fac292b63e631ae09344963b5030d92872e6612306
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/alexflint/go-filemutex
Version:                1.3.0
%gometa -L
%global common_description %{expand:
FileMutex is similar to sync.RWMutex, but also synchronizes across processes. On
Linux, OSX, and other POSIX systems it uses the flock system call. On windows it
uses the LockFileEx and UnlockFileEx system calls.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           golang-github-alexflint-filemutex
Release:        1%{?dist}
Summary:        Sync.Mutex working across processes
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/go-filemutex-%{version}.tar.gz
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
