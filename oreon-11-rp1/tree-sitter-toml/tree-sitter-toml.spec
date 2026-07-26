%global source0_hash 7d52a7d4884f307aabc872867c69084d94456d8afcdc63b0a73031a8b29036dc

Name:           tree-sitter-toml
Version:        0.7.0
Release:        %{autorelease}
License:        MIT
URL:            https://github.com/tree-sitter-grammars/%{name}
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    tree_sitter

%{tree_sitter -l TOML}

%changelog
%autochangelog
