%global source0_hash cf01b93f4b61b96a6d27942cf28eeda4cbce7d503c3bef773a8930b3d778a2d9
Name:           tree-sitter-lua
Version:        0.5.0
Release:        1%{?dist}
License:        MIT
URL:            https://github.com/tree-sitter-grammars/%{name}
Source0:        https://github.com/tree-sitter-grammars/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    tree_sitter
%{tree_sitter -l Lua}
# oreon:deps

# /oreon:deps
%files -f %{oreon_filedir}/main.list
%files -n libtree-sitter-lua -f %{oreon_filedir}/libtree-sitter-lua.list
%files -n libtree-sitter-lua-devel -f %{oreon_filedir}/libtree-sitter-lua-devel.list
%files -n python3-tree-sitter-lua -f %{oreon_filedir}/python3-tree-sitter-lua.list

%changelog

%autochangelog
