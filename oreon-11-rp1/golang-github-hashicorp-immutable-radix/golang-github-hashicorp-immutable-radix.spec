%global source0_hash b1bb5298511459b33d5c8013ac6cb93f3249d809f0a178d8b80496cd80987600
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/hashicorp/go-immutable-radix
Version:                2.1.0
%gometa
%global common_description %{expand:
Provides the iradix package that implements an immutable radix tree. The package
only provides a single Tree implementation, optimized for sparse nodes.
As a radix tree, it provides the following:
 - O(k) operations. In many cases, this can be faster than a hash table since
   the hash function is an O(k) operation, and hash tables have very poor cache
   locality.
 - Minimum / Maximum value lookups
 - Ordered iteration
A tree supports using a transaction to batch multiple updates (insert, delete)
in a more efficient manner than performing each operation one at a time.}
%global golicenses      LICENSE
%global godocs          CHANGELOG.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        An immutable radix tree implementation in Golang
License:        MPL-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/go-immutable-radix-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
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
