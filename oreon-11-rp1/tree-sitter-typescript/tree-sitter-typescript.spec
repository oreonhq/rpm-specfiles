%global source0_hash 2c4ce711ae8d1218a3b2f899189298159d672870b5b34dff5d937bed2f3e8983
Name:           tree-sitter-typescript
Version:        0.23.2
Release:        1%{?dist}
License:        MIT
URL:            https://github.com/tree-sitter/%{name}
Source0:        https://github.com/tree-sitter/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    tree_sitter
%{tree_sitter -l %{quote:TypeScript and TSX}}
# oreon:deps

# /oreon:deps
%files -f %{oreon_filedir}/main.list
%files -n libtree-sitter-typescript -f %{oreon_filedir}/libtree-sitter-typescript.list
%files -n libtree-sitter-typescript-devel -f %{oreon_filedir}/libtree-sitter-typescript-devel.list
%files -n python3-tree-sitter-typescript -f %{oreon_filedir}/python3-tree-sitter-typescript.list

%changelog

%autochangelog
