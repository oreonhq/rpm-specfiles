%global source0_hash acf6e8362457e819ed8b613f2ad9a0e1b621a77556c296f3abea58f7880a9213
Name:           tree-sitter-json
Version:        0.24.8
Release:        1%{?dist}
License:        MIT
URL:            https://github.com/tree-sitter/%{name}
Source0:        https://github.com/tree-sitter/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    tree_sitter
%{tree_sitter -l JSON}
# oreon:deps

# /oreon:deps
%files -f %{oreon_filedir}/main.list
%files -n libtree-sitter-json -f %{oreon_filedir}/libtree-sitter-json.list
%files -n libtree-sitter-json-devel -f %{oreon_filedir}/libtree-sitter-json-devel.list
%files -n python3-tree-sitter-json -f %{oreon_filedir}/python3-tree-sitter-json.list

%changelog

%autochangelog
