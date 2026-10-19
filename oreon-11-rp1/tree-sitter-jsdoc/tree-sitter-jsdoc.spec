%global source0_hash ca870c983c51bfb6b25c4cf316e28c685d0f6e9847e359c7da8d16eedd60d623
Name:           tree-sitter-jsdoc
Version:        0.25.0
Release:        1%{?dist}
License:        MIT
URL:            https://github.com/tree-sitter/%{name}
Source0:        https://github.com/tree-sitter/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    tree_sitter
%{tree_sitter -l JSDoc}
# oreon:deps

# /oreon:deps
%files -f %{oreon_filedir}/main.list
%files -n libtree-sitter-jsdoc -f %{oreon_filedir}/libtree-sitter-jsdoc.list
%files -n libtree-sitter-jsdoc-devel -f %{oreon_filedir}/libtree-sitter-jsdoc-devel.list
%files -n python3-tree-sitter-jsdoc -f %{oreon_filedir}/python3-tree-sitter-jsdoc.list

%changelog

%autochangelog
