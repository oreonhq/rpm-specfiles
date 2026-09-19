%global source0_hash b7a750e002b916a50c878c53087175dde5f256eb73d2d479b11b24d6c4b9a885

Name:           tree-sitter-phpdoc
Version:        0.1.8
Release:        %{autorelease}
License:        MIT
URL:            https://github.com/claytonrcarter/%{name}
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    tree_sitter

%{tree_sitter -l PHPDoc}

%changelog
%autochangelog
