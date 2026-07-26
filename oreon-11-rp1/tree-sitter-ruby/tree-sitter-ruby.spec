%global source0_hash e7e49577ddc1f2de8e42d42353b477e338c15bbb95b2558e123ddc13d88789f0

Name:           tree-sitter-ruby
Version:        0.23.1
Release:        %{autorelease}
License:        MIT
URL:            https://github.com/tree-sitter/%{name}
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    tree_sitter

%{tree_sitter -l Ruby}

%changelog
%autochangelog
