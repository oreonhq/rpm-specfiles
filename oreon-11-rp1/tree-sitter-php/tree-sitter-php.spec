%global source0_hash 0e73ad63dda67ac12c0e012726a4e1a9811c26b020a0a2dea3e889f8246d9cf4
Name:           tree-sitter-php
Version:        0.24.2
Release:        1%{?dist}
License:        MIT
URL:            https://github.com/tree-sitter/%{name}
Source0:        https://github.com/tree-sitter/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    tree_sitter
%{tree_sitter -l PHP}
# oreon:deps
BuildRequires:  tree-sitter-srpm-macros
# /oreon:deps
%files -f %{oreon_filedir}/main.list
%files -n libtree-sitter-php -f %{oreon_filedir}/libtree-sitter-php.list
%files -n libtree-sitter-php-devel -f %{oreon_filedir}/libtree-sitter-php-devel.list
%files -n python3-tree-sitter-php -f %{oreon_filedir}/python3-tree-sitter-php.list

%changelog

%autochangelog
