%global source0_hash acf6e8362457e819ed8b613f2ad9a0e1b621a77556c296f3abea58f7880a9213

Name:           tree-sitter-json
Version:        0.24.8
Release:        %{autorelease}
License:        MIT
URL:            https://github.com/tree-sitter/%{name}
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    tree_sitter

%{tree_sitter -l JSON}

%changelog
%autochangelog
