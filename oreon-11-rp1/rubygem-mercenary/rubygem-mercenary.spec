%global source0_hash b25a1e4a59adca88665e08e24acf0af30da5b5d859f7d8f38fba52c28f405138

%{!?_pkgdocdir:%global _pkgdocdir %{_docdir}/%{name}-%{version}}
%global git_url https://raw.githubusercontent.com/jekyll/%{gem_name}/master
%global gem_name mercenary

Name:		rubygem-%{gem_name}
Version:	0.4.0
Release:	%autorelease
Summary:	An easier way to build your command-line scripts in Ruby

License:	MIT
URL:		https://github.com/jekyll/%{gem_name}
Source0:	https://rubygems.org/downloads/%{gem_name}-%{version}.gem

BuildArch:	noarch
BuildRequires:	rubygems-devel

%description
Lightweight and flexible library for writing command-line apps in Ruby.

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
/bin/ln LICENSE.txt LICENSE
/bin/ln README.md README.markdown
for f in examples/*.rb
do
	%{__sed} -e '1s:^#![ \t]*%{_bindir}/env ruby:#!%{_bindir}/ruby:'	\
		< ${f} > ${f}.new &&						\
	/bin/touch -r ${f} ${f}.new && %{__mv} -f ${f}.new ${f} &&		\
	%{__chmod} -c 0755 ${f}
done

%build
%{_bindir}/gem build %{gem_name}.gemspec
%gem_install

%install
%{__mkdir} -p %{buildroot}%{gem_dir}
%{__cp} -a ./%{gem_dir}/* %{buildroot}%{gem_dir}
%{__rm} -f %{buildroot}%{gem_instdir}/{*.gemspec,*.md,*.markdown,.travis.yml}
%{__rm} -f %{buildroot}%{gem_instdir}/{.gitignore,.rspec,LICENSE.txt,Rakefile}
%{__rm} -rf %{buildroot}%{gem_instdir}/script

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
