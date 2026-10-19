%global source0_hash 061e90a539a55a6aa65dceb0ad6425c50ab1a6e3e6d4ba430e2795ed4550f10e
Name:           tree-sitter-rust
Version:        0.24.2
Release:        1%{?dist}
License:        MIT
URL:            https://github.com/tree-sitter/%{name}
Source0:        https://github.com/tree-sitter/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    tree_sitter
%{tree_sitter -l Rust}
# oreon:deps
BuildRequires:  tree-sitter-cli
# /oreon:deps
%files -f %{oreon_filedir}/main.list
%files -n libtree-sitter-rust -f %{oreon_filedir}/libtree-sitter-rust.list
%files -n libtree-sitter-rust-devel -f %{oreon_filedir}/libtree-sitter-rust-devel.list
%files -n python3-tree-sitter-rust -f %{oreon_filedir}/python3-tree-sitter-rust.list

%changelog

%autochangelog
