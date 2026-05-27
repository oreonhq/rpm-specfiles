%global source0_hash none

Name:           tree-sitter-srpm-macros
Version:        0.4.2
Release:        %autorelease
Summary:        RPM macros for Tree-sitter parsers
License:        MIT
URL:            https://github.com/tree-sitter/tree-sitter

Source0:        MIT.txt
Source1:        README.md
Source2:        macros.tree_sitter
Source3:        tree_sitter.attr

BuildArch:      noarch
Requires:       rpm

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

%files
%license %{_defaultlicensedir}/%{name}/
%doc %{_pkgdocdir}/
%{_rpmmacrodir}/%{basename:%{SOURCE2}}
%{_fileattrsdir}/%{basename:%{SOURCE3}}

%changelog
* Fri May 08 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.4.2-1
- Import from Fedora 44 dist-git, debrand docs and changelog
