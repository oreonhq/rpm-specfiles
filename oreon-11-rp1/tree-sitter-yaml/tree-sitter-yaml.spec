%global source0_hash aeaff5731bb8b66c7054c8aed33cd5edea5f4cd2ac71654f3f6c2ba2073d8fac
Name:           tree-sitter-yaml
Version:        0.7.2
Release:        1%{?dist}
License:        MIT
URL:            https://github.com/tree-sitter-grammars/%{name}
Source0:        https://github.com/tree-sitter-grammars/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    tree_sitter
%{tree_sitter -l YAML}
# oreon:deps
BuildRequires:  tree-sitter-srpm-macros
# /oreon:deps
%files -f %{oreon_filedir}/main.list
%files -n libtree-sitter-yaml -f %{oreon_filedir}/libtree-sitter-yaml.list
%files -n libtree-sitter-yaml-devel -f %{oreon_filedir}/libtree-sitter-yaml-devel.list
%files -n python3-tree-sitter-yaml -f %{oreon_filedir}/python3-tree-sitter-yaml.list

%changelog

%autochangelog
