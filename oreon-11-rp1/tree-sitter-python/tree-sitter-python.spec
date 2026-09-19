%global source0_hash 4609a3665a620e117acf795ff01b9e965880f81745f287a16336f4ca86cf270c

Name:           tree-sitter-python
Version:        0.25.0
Release:        %{autorelease}
License:        MIT
URL:            https://github.com/tree-sitter/%{name}
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    tree_sitter

%{tree_sitter -l Python}

%changelog
%autochangelog
