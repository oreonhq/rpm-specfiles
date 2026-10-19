%global source0_hash e7e49577ddc1f2de8e42d42353b477e338c15bbb95b2558e123ddc13d88789f0
Name:           tree-sitter-ruby
Version:        0.23.1
Release:        1%{?dist}
License:        MIT
URL:            https://github.com/tree-sitter/%{name}
Source0:        https://github.com/tree-sitter/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    tree_sitter
%{tree_sitter -l Ruby}
# oreon:deps

# /oreon:deps
%files -f %{oreon_filedir}/main.list
%files -n libtree-sitter-ruby -f %{oreon_filedir}/libtree-sitter-ruby.list
%files -n libtree-sitter-ruby-devel -f %{oreon_filedir}/libtree-sitter-ruby-devel.list
%files -n python3-tree-sitter-ruby -f %{oreon_filedir}/python3-tree-sitter-ruby.list

%changelog

%autochangelog
