%global source0_hash 9712fc283d3dc01d996d20b6392143445d05867a7aad76fdd723824468428b86
Name:           tree-sitter-javascript
Version:        0.25.0
Release:        1%{?dist}
License:        MIT
URL:            https://github.com/tree-sitter/%{name}
Source0:        https://github.com/tree-sitter/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    tree_sitter
%{tree_sitter -l JavaScript}
# oreon:deps

# /oreon:deps
%files -f %{oreon_filedir}/main.list
%files -n libtree-sitter-javascript -f %{oreon_filedir}/libtree-sitter-javascript.list
%files -n libtree-sitter-javascript-devel -f %{oreon_filedir}/libtree-sitter-javascript-devel.list
%files -n python3-tree-sitter-javascript -f %{oreon_filedir}/python3-tree-sitter-javascript.list

%changelog

%autochangelog
