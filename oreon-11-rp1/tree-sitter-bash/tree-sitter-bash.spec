%global source0_hash 2e785a761225b6c433410ef9c7b63cfb0a4e83a35a19e0f2aec140b42c06b52d

Name:           tree-sitter-bash
Version:        0.25.1
Release:        %{autorelease}
License:        MIT
URL:            https://github.com/tree-sitter/%{name}
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    tree_sitter

%{tree_sitter -l Bash}

%changelog
%autochangelog
