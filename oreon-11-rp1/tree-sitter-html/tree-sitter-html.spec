%global source0_hash 21fa4f2d4dcb890ef12d09f4979a0007814f67f1c7294a9b17b0108a09e45ef7

Name:           tree-sitter-html
Version:        0.23.2
Release:        %{autorelease}
License:        MIT
URL:            https://github.com/tree-sitter/%{name}
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    tree_sitter

%{tree_sitter -l HTML}

%changelog
%autochangelog
