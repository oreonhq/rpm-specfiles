%global source0_hash none
Name:           tree-sitter-srpm-macros
Version:        0.4.2
Release:        1%{?dist}
Summary:        RPM macros for Tree-sitter parsers
License:        MIT
URL:            https://github.com/tree-sitter/tree-sitter
Source0:        MIT.txt
Source1:        README.md
Source2:        macros.tree_sitter
Source3:        tree_sitter.attr
BuildArch:      noarch
Requires:       rpm
# oreon:deps

# /oreon:deps
%description
Macros for building packages that ship Tree-sitter parsers on RPM-based
distributions.

%install
install -Dp -m u=rw,go=r \
        %{SOURCE0} %{buildroot}%{_defaultlicensedir}/%{name}/%{basename:%{SOURCE0}}
install -Dp -m u=rw,go=r \
        %{SOURCE1} %{buildroot}%{_pkgdocdir}/%{basename:%{SOURCE1}}
install -Dp -m u=rw,go=r \
        %{SOURCE2} %{buildroot}%{_rpmmacrodir}/%{basename:%{SOURCE2}}
install -Dp -m u=rw,go=r \
        %{SOURCE3} %{buildroot}%{_fileattrsdir}/%{basename:%{SOURCE3}}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
