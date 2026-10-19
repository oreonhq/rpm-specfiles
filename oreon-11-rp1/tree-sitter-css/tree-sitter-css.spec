%global source0_hash 03965344d8c0435dc54fb45b281578420bb7db8b99df4d34e7e74105a274cb79
Name:           tree-sitter-css
Version:        0.25.0
Release:        1%{?dist}
License:        MIT
URL:            https://github.com/tree-sitter/%{name}
Source0:        https://github.com/tree-sitter/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    tree_sitter
%{tree_sitter -l CSS}
# oreon:deps

# /oreon:deps
%files -f %{oreon_filedir}/main.list
%files -n libtree-sitter-css -f %{oreon_filedir}/libtree-sitter-css.list
%files -n libtree-sitter-css-devel -f %{oreon_filedir}/libtree-sitter-css-devel.list
%files -n python3-tree-sitter-css -f %{oreon_filedir}/python3-tree-sitter-css.list

%changelog

%autochangelog
