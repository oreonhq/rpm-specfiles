%global source0_hash ca870c983c51bfb6b25c4cf316e28c685d0f6e9847e359c7da8d16eedd60d623

Name:           tree-sitter-jsdoc
Version:        0.25.0
Release:        %{autorelease}
License:        MIT
URL:            https://github.com/tree-sitter/%{name}
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    tree_sitter

%{tree_sitter -l JSDoc}

%changelog
%autochangelog
