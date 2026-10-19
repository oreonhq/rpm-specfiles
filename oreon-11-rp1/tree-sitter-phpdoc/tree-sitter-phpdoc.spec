%global source0_hash b7a750e002b916a50c878c53087175dde5f256eb73d2d479b11b24d6c4b9a885
Name:           tree-sitter-phpdoc
Version:        0.1.8
Release:        1%{?dist}
License:        MIT
URL:            https://github.com/claytonrcarter/%{name}
Source0:        https://github.com/claytonrcarter/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    tree_sitter
%{tree_sitter -l PHPDoc}
# oreon:deps

# /oreon:deps
%files -f %{oreon_filedir}/main.list
%files -n libtree-sitter-phpdoc -f %{oreon_filedir}/libtree-sitter-phpdoc.list
%files -n libtree-sitter-phpdoc-devel -f %{oreon_filedir}/libtree-sitter-phpdoc-devel.list
%files -n python3-tree-sitter-phpdoc -f %{oreon_filedir}/python3-tree-sitter-phpdoc.list

%changelog

%autochangelog
