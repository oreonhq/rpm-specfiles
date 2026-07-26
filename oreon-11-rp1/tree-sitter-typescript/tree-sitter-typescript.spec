%global source0_hash 2c4ce711ae8d1218a3b2f899189298159d672870b5b34dff5d937bed2f3e8983

Name:           tree-sitter-typescript
Version:        0.23.2
Release:        %{autorelease}
License:        MIT
URL:            https://github.com/tree-sitter/%{name}
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    tree_sitter

%{tree_sitter -l %{quote:TypeScript and TSX}}

%changelog
%autochangelog
