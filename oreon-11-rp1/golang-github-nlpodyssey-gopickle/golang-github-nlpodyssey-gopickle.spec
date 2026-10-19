%global source0_hash 98f425e60f0a11edd8dc3f9151b79b920d9235602d6f7f44413de698f6cd2225
%bcond check 1
%global debug_package %{nil}
%global goipath         github.com/nlpodyssey/gopickle
Version:                0.3.0
%gometa -L -f
%global common_description %{expand:
Go library for loading Python's data serialized with pickle and PyTorch module
files.}
%global golicenses      LICENSE
%global godocs          CHANGELOG.md README.md
Name:           golang-github-nlpodyssey-gopickle
Release:        1%{?dist}
Summary:        Go library for loading Python's data serialized with pickle
License:        BSD-2-Clause
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/gopickle-%{version}.tar.gz
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
