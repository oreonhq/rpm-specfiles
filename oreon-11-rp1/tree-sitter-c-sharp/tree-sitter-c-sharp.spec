%global source0_hash c0b008dca3c6820604bf0853b9668ba034f9750d89d170ba834261e94e2cd917

Name:           tree-sitter-c-sharp
Version:        0.23.1
Release:        %{autorelease}
License:        MIT
URL:            https://github.com/tree-sitter/%{name}
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    tree_sitter

%{tree_sitter -l C#}

%changelog
%autochangelog
