%global source0_hash 7d8bf37949e2bea75a19d38491d7680ed1c9f0f5a41a5235832d718ec174c7c4
Name:           tree-sitter-elixir
Version:        0.3.5
Release:        1%{?dist}
License:        Apache-2.0
URL:            https://github.com/elixir-lang/%{name}
Source0:        https://github.com/elixir-lang/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    tree_sitter
BuildOption(build): PARSER_NAME=elixir
BuildOption(install): PARSER_NAME=elixir
%{tree_sitter -l Elixir}
# oreon:deps
BuildRequires:  tree-sitter-srpm-macros
# /oreon:deps
%install
%{buildsystem_tree_sitter_install PARSER_NAME=elixir}
mv $RPM_BUILD_ROOT/%{_includedir}/tree_sitter/elixir.h \
   $RPM_BUILD_ROOT/%{_includedir}/tree_sitter/%{name}.h \
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n libtree-sitter-elixir -f %{oreon_filedir}/libtree-sitter-elixir.list
%files -n libtree-sitter-elixir-devel -f %{oreon_filedir}/libtree-sitter-elixir-devel.list
%files -n python3-tree-sitter-elixir -f %{oreon_filedir}/python3-tree-sitter-elixir.list

%changelog

%autochangelog
