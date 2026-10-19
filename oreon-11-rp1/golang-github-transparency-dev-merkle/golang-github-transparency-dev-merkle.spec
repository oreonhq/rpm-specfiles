%global source0_hash db6c26b0069fb41400a801e81a3e5ccc2d3b0157a9ed2bf6a4a9aa6d66befd9c
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/transparency-dev/merkle
Version:                0.0.1
%gometa
%global common_description %{expand:
Go code to help create and manipulate Merkle trees, as well as constructing and
verifying various types of proof.}
%global golicenses      LICENSE
%global godocs          docs CONTRIBUTING.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Go code to help create and manipulate Merkle trees
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/merkle-%{version}.tar.gz
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
