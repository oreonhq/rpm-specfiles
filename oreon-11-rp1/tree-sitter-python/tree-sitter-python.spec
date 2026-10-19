%global source0_hash 4609a3665a620e117acf795ff01b9e965880f81745f287a16336f4ca86cf270c
Name:           tree-sitter-python
Version:        0.25.0
Release:        1%{?dist}
License:        MIT
URL:            https://github.com/tree-sitter/%{name}
Source0:        https://github.com/tree-sitter/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    tree_sitter
%{tree_sitter -l Python}
# oreon:deps

# /oreon:deps
%files -f %{oreon_filedir}/main.list
%files -n libtree-sitter-python -f %{oreon_filedir}/libtree-sitter-python.list
%files -n libtree-sitter-python-devel -f %{oreon_filedir}/libtree-sitter-python-devel.list
%files -n python3-tree-sitter-python -f %{oreon_filedir}/python3-tree-sitter-python.list

%changelog

%autochangelog
