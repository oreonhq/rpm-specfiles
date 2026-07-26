%global source0_hash 2dc241b97872c53195e01b86542b411a3c1a6201d9c946c78d5c60c063bba1ef

Name:           tree-sitter-go
Version:        0.25.0
Release:        %{autorelease}
License:        MIT
URL:            https://github.com/tree-sitter/%{name}
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    tree_sitter

%{tree_sitter -l Go}

%changelog
%autochangelog
