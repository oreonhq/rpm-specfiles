%global source0_hash 9628b164369071019368618bdefa446f0aab8acaac47b75d5dfb209e93b8903b
Name:           tree-sitter-c-sharp
Version:        0.23.5
Release:        1%{?dist}
License:        MIT
URL:            https://github.com/tree-sitter/%{name}
Source0:        https://github.com/tree-sitter/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    tree_sitter
%{tree_sitter -l C#}
# oreon:deps

# /oreon:deps
%files -f %{oreon_filedir}/main.list
%files -n libtree-sitter-c-sharp -f %{oreon_filedir}/libtree-sitter-c-sharp.list
%files -n libtree-sitter-c-sharp-devel -f %{oreon_filedir}/libtree-sitter-c-sharp-devel.list
%files -n python3-tree-sitter-c-sharp -f %{oreon_filedir}/python3-tree-sitter-c-sharp.list

%changelog

%autochangelog
