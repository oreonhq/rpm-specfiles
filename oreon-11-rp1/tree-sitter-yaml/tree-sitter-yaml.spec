%global source0_hash aeaff5731bb8b66c7054c8aed33cd5edea5f4cd2ac71654f3f6c2ba2073d8fac

Name:           tree-sitter-yaml
Version:        0.7.2
Release:        %{autorelease}
License:        MIT
URL:            https://github.com/tree-sitter-grammars/%{name}
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  tree-sitter-srpm-macros >= 0.2.1
BuildSystem:    tree_sitter

%{tree_sitter -l YAML}

%changelog
%autochangelog
