%global source0_hash 2eeb4db31f8fa0865e45488503d13403923bcb485a1bdb637abff8c42dd97364
Name:           tree-sitter-c
Version:        0.24.2
Release:        1%{?dist}
License:        MIT
URL:            https://github.com/tree-sitter/%{name}
Source0:        https://github.com/tree-sitter/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    tree_sitter
%{tree_sitter -l C}
# oreon:deps
BuildRequires:  tree-sitter-srpm-macros
# /oreon:deps
%install
%buildsystem_tree_sitter_install
install -m644 queries/*.scm $RPM_BUILD_ROOT%{_datadir}/tree-sitter/queries/c
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n libtree-sitter-c -f %{oreon_filedir}/libtree-sitter-c.list
%files -n libtree-sitter-c-devel -f %{oreon_filedir}/libtree-sitter-c-devel.list
%files -n python3-tree-sitter-c -f %{oreon_filedir}/python3-tree-sitter-c.list

%changelog

%autochangelog
