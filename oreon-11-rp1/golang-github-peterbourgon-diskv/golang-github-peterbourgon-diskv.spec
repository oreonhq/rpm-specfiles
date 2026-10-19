%global source0_hash a5b476653f88ab82593bd3d342cb53915f6c7a0cdd4db25bc9d6c5dde71b2c65
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/peterbourgon/diskv
Version:                3.0.1
%gometa
%global goaltipaths     github.com/peterbourgon/diskv/v3
%global common_description %{expand:
Diskv (disk-vee) is a simple, persistent key-value store written in the Go
language. It starts with an incredibly simple API for storing arbitrary data
on a filesystem by key, and builds several layers of performance-enhancing
abstraction on top. The end result is a conceptually simple, but highly
performant, disk-backed storage system.}
%global golicenses      LICENSE
%global godocs          examples README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Disk-backed key-value store
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/diskv-%{version}.tar.gz
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
