%global source0_hash 5a62c397ced0a191e7a0cda0f8added46ef9a688e2b1a9c1420d4716f91960c5
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/termie/go-shutil
%global commit          bcacb06fecaeec8dc42af03c87c6949f4a05c74c
%gometa
%global common_description %{expand:
High-level Filesystem Operations (for Go)
A direct port of a few of the functions from Python's shutil package
for high-level filesystem operations.
Functions so far: we support Copy, CopyFile, CopyMode and CopyTree.}
%global golicenses      LICENSE
%global godocs          README.rst
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Golang port of python's shutil
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/go-shutil-%{commit}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
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
