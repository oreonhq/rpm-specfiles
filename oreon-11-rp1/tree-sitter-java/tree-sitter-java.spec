%global source0_hash cb199e0faae4b2c08425f88cbb51c1a9319612e7b96315a174a624db9bf3d9f0
Name:           tree-sitter-java
Version:        0.23.5
Release:        1%{?dist}
License:        MIT
URL:            https://github.com/tree-sitter/%{name}
Source0:        https://github.com/tree-sitter/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    tree_sitter
%{tree_sitter -l Java}
# oreon:deps

# /oreon:deps
%files -f %{oreon_filedir}/main.list
%files -n libtree-sitter-java -f %{oreon_filedir}/libtree-sitter-java.list
%files -n libtree-sitter-java-devel -f %{oreon_filedir}/libtree-sitter-java-devel.list
%files -n python3-tree-sitter-java -f %{oreon_filedir}/python3-tree-sitter-java.list

%changelog

%autochangelog
