%global source0_hash b1c664921d06a6609f2b4fdfbd6685baea35066873ae5b75e11be55317d281f9
Name:           tree-sitter-cmake
Version:        0.7.5
Release:        1%{?dist}
License:        MIT
URL:            https://github.com/uyha/%{name}
Source0:        https://github.com/uyha/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    tree_sitter
%{tree_sitter -l CMake}
# oreon:deps
BuildRequires:  tree-sitter-srpm-macros
# /oreon:deps
%files -f %{oreon_filedir}/main.list
%files -n libtree-sitter-cmake -f %{oreon_filedir}/libtree-sitter-cmake.list
%files -n libtree-sitter-cmake-devel -f %{oreon_filedir}/libtree-sitter-cmake-devel.list
%files -n python3-tree-sitter-cmake -f %{oreon_filedir}/python3-tree-sitter-cmake.list

%changelog

%autochangelog
