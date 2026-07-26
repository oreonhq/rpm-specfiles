%global source0_hash c9498a31d6462b3eda82ff0988e95109b3853d88cc7c393a5008736e7da527e0

Name:           tree-sitter-cmake
Version:        0.7.2
Release:        %{autorelease}
License:        MIT
URL:            https://github.com/uyha/%{name}
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    tree_sitter
BuildRequires:  tree-sitter-srpm-macros >= 0.2.4

%{tree_sitter -l CMake}

%changelog
%autochangelog
