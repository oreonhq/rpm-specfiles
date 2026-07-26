%global source0_hash 1bec948c469bbddfadeb3bd90eb8c85f6e627a412a3e852acfd7eaedbac3ec97

%{!?_pkgdocdir:%global _pkgdocdir %{_docdir}/%{name}-%{version}}
%global gem_name forwardable-extended

Name:		rubygem-%{gem_name}
Version:	2.6.0
Release:	21%{?dist}
Summary:	Forwardable with hash, and instance variable extensions

License:	MIT
URL:		https://github.com/envygeeks/%{gem_name}
Source0:	https://rubygems.org/downloads/%{gem_name}-%{version}.gem
Source1:	https://raw.githubusercontent.com/envygeeks/forwardable-extended/master/README.md#/%{gem_name}-README.md

BuildArch:	noarch
BuildRequires:	rubygems-devel

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

%files
%exclude %{gem_cache}
%license LICENSE
%doc README.markdown
%{gem_instdir}
%{gem_spec}

%files doc
%doc %{_pkgdocdir}
%doc %{gem_docdir}

%changelog
%autochangelog
