%global source0_hash e2f85daf57af47d740db2a32191d1bdfb0f6503a0dfbc8327d0c9154d5ddfc38

%{!?_pkgdocdir:%global _pkgdocdir %{_docdir}/%{name}-%{version}}
%global gem_name colorator

Name:		rubygem-%{gem_name}
Version:	1.1.0
Release:	21%{?dist}
Summary:	Colorize your text in the terminal

License:	MIT
URL:		https://github.com/octopress/%{gem_name}
Source0:	https://rubygems.org/downloads/%{gem_name}-%{version}.gem

BuildArch:	noarch
BuildRequires:	rubygems-devel

%description
Colorize your text in the terminal.  There are a bunch of gems that
provide functionality like this, but none have as simple an API as
this.  Just call "string".color and your text will be colorized.

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
%{__rm} -f %{buildroot}%{gem_instdir}/{*.gemspec,*.markdown,LICENSE,Rakefile}

%files
%exclude %{gem_cache}
%license LICENSE
%doc History.markdown README.markdown
%{gem_instdir}
%{gem_spec}

%files doc
%doc %{_pkgdocdir}
%doc %{gem_docdir}

%changelog
%autochangelog
