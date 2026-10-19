%global source0_hash 7a2c55afe3028f4105f25762ea58cc16537d1f5a1dcd9cca90410b3cd5d46051
Name:           tree-sitter-cpp
Version:        0.23.4
Release:        1%{?dist}
License:        MIT
URL:            https://github.com/tree-sitter/%{name}
Source0:        https://github.com/tree-sitter/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    tree_sitter
%{tree_sitter -l C++}
# oreon:deps
BuildRequires:  tree-sitter-srpm-macros
# /oreon:deps
%files -f %{oreon_filedir}/main.list
%files -n libtree-sitter-cpp -f %{oreon_filedir}/libtree-sitter-cpp.list
%files -n libtree-sitter-cpp-devel -f %{oreon_filedir}/libtree-sitter-cpp-devel.list
%files -n python3-tree-sitter-cpp -f %{oreon_filedir}/python3-tree-sitter-cpp.list

%changelog

%autochangelog
