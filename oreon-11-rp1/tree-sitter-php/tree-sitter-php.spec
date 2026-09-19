%global source0_hash 0e73ad63dda67ac12c0e012726a4e1a9811c26b020a0a2dea3e889f8246d9cf4

Name:           tree-sitter-php
Version:        0.24.2
Release:        %{autorelease}
License:        MIT
URL:            https://github.com/tree-sitter/%{name}
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    tree_sitter
BuildRequires:  tree-sitter-srpm-macros >= 0.1.1

%{tree_sitter -l PHP}

%changelog
%autochangelog
