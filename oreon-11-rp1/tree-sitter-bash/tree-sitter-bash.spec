%global source0_hash 2e785a761225b6c433410ef9c7b63cfb0a4e83a35a19e0f2aec140b42c06b52d
Name:           tree-sitter-bash
Version:        0.25.1
Release:        1%{?dist}
License:        MIT
URL:            https://github.com/tree-sitter/%{name}
Source0:        https://github.com/tree-sitter/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    tree_sitter
%{tree_sitter -l Bash}
# oreon:deps

# /oreon:deps
%files -f %{oreon_filedir}/main.list
%files -n libtree-sitter-bash -f %{oreon_filedir}/libtree-sitter-bash.list
%files -n libtree-sitter-bash-devel -f %{oreon_filedir}/libtree-sitter-bash-devel.list
%files -n python3-tree-sitter-bash -f %{oreon_filedir}/python3-tree-sitter-bash.list

%changelog

%autochangelog
