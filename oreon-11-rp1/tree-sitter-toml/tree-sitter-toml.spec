%global source0_hash 7d52a7d4884f307aabc872867c69084d94456d8afcdc63b0a73031a8b29036dc
Name:           tree-sitter-toml
Version:        0.7.0
Release:        1%{?dist}
License:        MIT
URL:            https://github.com/tree-sitter-grammars/%{name}
Source0:        https://github.com/tree-sitter-grammars/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    tree_sitter
%{tree_sitter -l TOML}
# oreon:deps

# /oreon:deps
%files -f %{oreon_filedir}/main.list
%files -n libtree-sitter-toml -f %{oreon_filedir}/libtree-sitter-toml.list
%files -n libtree-sitter-toml-devel -f %{oreon_filedir}/libtree-sitter-toml-devel.list
%files -n python3-tree-sitter-toml -f %{oreon_filedir}/python3-tree-sitter-toml.list

%changelog

%autochangelog
