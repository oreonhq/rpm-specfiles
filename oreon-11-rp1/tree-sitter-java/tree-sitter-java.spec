%global source0_hash cb199e0faae4b2c08425f88cbb51c1a9319612e7b96315a174a624db9bf3d9f0

Name:           tree-sitter-java
Version:        0.23.5
Release:        %{autorelease}
License:        MIT
URL:            https://github.com/tree-sitter/%{name}
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    tree_sitter

%{tree_sitter -l Java}

%changelog
%autochangelog
