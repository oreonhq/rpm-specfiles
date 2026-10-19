%global source1_hash 694f845c0c86e0ff15f9d5764d4d2fd0fc13ee41bae45f30cb136676018392be
%global source0_hash 1bec948c469bbddfadeb3bd90eb8c85f6e627a412a3e852acfd7eaedbac3ec97
%{!?_pkgdocdir:%global _pkgdocdir %{_docdir}/%{name}-%{version}}
%global gem_name forwardable-extended
Name:		rubygem-%{gem_name}
Version:	2.6.0
Release:        21%{?dist}
Summary:        Forwardable with hash, and instance variable extensions
License:	MIT
URL:		https://github.com/envygeeks/%{gem_name}
Source0:        https://rubygems.org/downloads/%{gem_name}-%{version}.gem
Source1:	https://raw.githubusercontent.com/envygeeks/forwardable-extended/master/README.md#/%{gem_name}-README.md
BuildArch:	noarch
# oreon:deps
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Extends forwardable with delegation to hashes and instance variables.

%package doc
Summary:	Documentation files for %{name}
%description doc
This package contains the documentation files for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{__rm} -rf %{gem_name}-%{version}
%{_bindir}/gem unpack %{SOURCE0}
%setup -DTqn %{gem_name}-%{version}
%{_bindir}/gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build

%{_bindir}/gem build %{gem_name}.gemspec
%gem_install
%install
%{__mkdir} -p %{buildroot}%{gem_dir}
%{__cp} -a ./%{gem_dir}/* %{buildroot}%{gem_dir}
%{__rm} -f %{buildroot}%{gem_instdir}/{LICENSE,Rakefile}
%{__install} -pm0644 %{SOURCE1} ./README.markdown
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n rubygem-forwardable-extended-doc -f %{oreon_filedir}/rubygem-forwardable-extended-doc.list

%changelog

%autochangelog
