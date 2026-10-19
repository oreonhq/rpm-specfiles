%global source0_hash 8064cef025207d5c051398eba5936d31d716b28b0ed2638cea34cd4449153cf6
Name:           tree-sitter-heex
Version:        0.9.0
Release:        1%{?dist}
License:        MIT
URL:            https://github.com/phoenixframework/%{name}
Source0:        https://github.com/phoenixframework/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    tree_sitter
%{tree_sitter -l HEEx}
# oreon:deps
BuildRequires:  tree-sitter-srpm-macros
# /oreon:deps
%files -f %{oreon_filedir}/main.list
%files -n libtree-sitter-heex -f %{oreon_filedir}/libtree-sitter-heex.list
%files -n libtree-sitter-heex-devel -f %{oreon_filedir}/libtree-sitter-heex-devel.list
%files -n python3-tree-sitter-heex -f %{oreon_filedir}/python3-tree-sitter-heex.list

%changelog

%autochangelog
