%global source0_hash 52d108d08e1a5d95c00343cb3a4936fb1deecff2be612ec39c9cb66be5a8b859

%global gem_name semantic_puppet

%global with_test 1

Name:          rubygem-%{gem_name}
Version:       1.1.0
Release:       6%{?dist}
Summary:       Useful tools for working with Semantic Versions
License:       Apache-2.0
URL:           https://github.com/puppetlabs/semantic_puppet
Source0:       https://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildRequires: rubygems-devel
%if 0%{?with_test}
BuildRequires: rubygem(rspec)
%endif
Requires:      ruby(rubygems)

BuildArch:     noarch

%description
Tools used by Puppet to parse, validate, and compare Semantic Versions and
Version Ranges and to query and resolve module dependencies.

%package doc
Summary:       Documentation for %{name}
Requires:      %{name} = %{version}-%{release}
BuildArch:     noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

gem unpack %{SOURCE0}
%setup -q -D -T -n %{gem_name}-%{version}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
gem build %{gem_name}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
rm -rf %{buildroot}%{gem_instdir}/{.github,.gitignore,.rubocop.yml,.yardopts}

%check
%if 0%{?with_test}
pushd .%{gem_instdir}
rspec spec
popd
%endif

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%exclude %{gem_instdir}/CODEOWNERS
%{gem_instdir}/Rakefile
%{gem_instdir}/semantic_puppet.gemspec
%{gem_instdir}/spec

%changelog
%autochangelog
