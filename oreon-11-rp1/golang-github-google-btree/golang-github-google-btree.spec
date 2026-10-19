%global source0_hash ecb1f97cff16ce5b18a12ed31728a82a8e0df0c0181febf2b9c39dd3ed362ffd
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/google/btree
Version:                1.1.3
%gometa
%global common_description %{expand:
This package provides an in-memory B-Tree implementation for Go, useful as an
ordered, mutable data structure.
The API is based off of the wonderful
http://godoc.org/github.com/petar/GoLLRB/llrb, and is meant to allow btree to
act as a drop-in replacement for gollrb trees.}
%global golicenses      LICENSE
%global godocs          README.md
%global gosupfiles glide.lock glide.yaml
Name:           %{goname}
Release:        1%{?dist}
Summary:        BTree implementation for Go
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/btree-%{version}.tar.gz
Source1:        glide.yaml
Source2:        glide.lock
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
cp %{S:1} %{S:2} .

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
