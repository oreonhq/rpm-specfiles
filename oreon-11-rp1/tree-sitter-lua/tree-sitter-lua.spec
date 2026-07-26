%global source0_hash cef44b8773bde69d427b5e50ca95e417c86c0be91caa37a6782c90d6f529da70

Name:           tree-sitter-lua
Version:        0.4.1
Release:        %{autorelease}
License:        MIT
URL:            https://github.com/tree-sitter-grammars/%{name}
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    tree_sitter

%{tree_sitter -l Lua}

%changelog
%autochangelog
