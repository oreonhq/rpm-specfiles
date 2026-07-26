%global source0_hash 9712fc283d3dc01d996d20b6392143445d05867a7aad76fdd723824468428b86

Name:           tree-sitter-javascript
Version:        0.25.0
Release:        %{autorelease}
License:        MIT
URL:            https://github.com/tree-sitter/%{name}
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    tree_sitter

%{tree_sitter -l JavaScript}

%changelog
%autochangelog
