%global source0_hash 5817812a95d147f6afa825e43a5917e41622b69f4039c2deeda003f4c48d8611

Name:           tree-sitter-rust
Version:        0.24.1
Release:        %{autorelease}
License:        MIT
URL:            https://github.com/tree-sitter/%{name}
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    tree_sitter
BuildRequires:  tree-sitter-cli >= 0.25.0

%{tree_sitter -l Rust}

%changelog
%autochangelog
