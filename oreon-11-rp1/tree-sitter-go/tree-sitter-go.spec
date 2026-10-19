%global source0_hash 2dc241b97872c53195e01b86542b411a3c1a6201d9c946c78d5c60c063bba1ef
Name:           tree-sitter-go
Version:        0.25.0
Release:        1%{?dist}
License:        MIT
URL:            https://github.com/tree-sitter/%{name}
Source0:        https://github.com/tree-sitter/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    tree_sitter
%{tree_sitter -l Go}
# oreon:deps

# /oreon:deps
%files -f %{oreon_filedir}/main.list
%files -n libtree-sitter-go -f %{oreon_filedir}/libtree-sitter-go.list
%files -n libtree-sitter-go-devel -f %{oreon_filedir}/libtree-sitter-go-devel.list
%files -n python3-tree-sitter-go -f %{oreon_filedir}/python3-tree-sitter-go.list

%changelog

%autochangelog
