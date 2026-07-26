%global source0_hash 03965344d8c0435dc54fb45b281578420bb7db8b99df4d34e7e74105a274cb79

Name:           tree-sitter-css
Version:        0.25.0
Release:        %{autorelease}
License:        MIT
URL:            https://github.com/tree-sitter/%{name}
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    tree_sitter

%{tree_sitter -l CSS}

%changelog
%autochangelog
