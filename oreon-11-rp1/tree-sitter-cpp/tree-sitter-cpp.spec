%global source0_hash 7a2c55afe3028f4105f25762ea58cc16537d1f5a1dcd9cca90410b3cd5d46051

Name:           tree-sitter-cpp
Version:        0.23.4
Release:        %{autorelease}
License:        MIT
URL:            https://github.com/tree-sitter/%{name}
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    tree_sitter
BuildRequires:  tree-sitter-srpm-macros >= 0.3.0

%{tree_sitter -l C++}

%changelog
%autochangelog
