%global source0_hash 21fa4f2d4dcb890ef12d09f4979a0007814f67f1c7294a9b17b0108a09e45ef7
Name:           tree-sitter-html
Version:        0.23.2
Release:        1%{?dist}
License:        MIT
URL:            https://github.com/tree-sitter/%{name}
Source0:        https://github.com/tree-sitter/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    tree_sitter
%{tree_sitter -l HTML}
# oreon:deps

# /oreon:deps
%files -f %{oreon_filedir}/main.list
%files -n libtree-sitter-html -f %{oreon_filedir}/libtree-sitter-html.list
%files -n libtree-sitter-html-devel -f %{oreon_filedir}/libtree-sitter-html-devel.list
%files -n python3-tree-sitter-html -f %{oreon_filedir}/python3-tree-sitter-html.list

%changelog

%autochangelog
