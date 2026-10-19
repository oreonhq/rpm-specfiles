%global source0_hash 1f2251133c840381220c050196d716ff3a117173a076249ec4ae0763c48bd63d
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/emirpasic/gods/v2
Version:                2.0.0
%global tag             v2.0.0-alpha
%global date            20240106
%gometa
%global common_description %{expand:
GoDS (Go Data Structures)
Implementation of various data structures and algorithms in Go.
Containers (Sets, Lists, Stacks, Maps, Trees), Sets (HashSet, TreeSet), Lists
(ArrayList, SinglyLinkedList, DoublyLinkedList), Stacks (LinkedListStack,
ArrayStack), Maps (HashMap, TreeMap, HashBidiMap, TreeBidiMap), Trees
(RedBlackTree, AVLTree, BTree, BinaryHeap), Comparators, Iterators, Enumerables,
Sort, JSON}
%global golicenses      LICENSE
%global godocs          examples README.md
Name:           golang-github-emirpasic-gods2
Release:        1%{?dist}
Summary:        Implementation of various data structures and algorithms in Go
License:        BSD-2-Clause AND ISC
URL:            %{gourl}
Source0:        https://github.com/emirpasic/gods/archive/%{tag}/gods-%{version}-alpha.tar.gz
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
