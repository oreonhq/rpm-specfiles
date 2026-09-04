%global source0_hash ca2ae7def8cfcdc2bfb6a186d36d5d59c8b403245dc0256c3802b767fa278aaa

%global gem_name ruby_engine

Name:           rubygem-%{gem_name}
Version:        2.0.3
Release:        1%{?dist}
Summary:        Adds the RubyEngine pseudo-constant

License:        MIT
URL:            https://github.com/janlelis/ruby_engine
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildArch:      noarch
BuildRequires:  rubygems-devel
BuildRequires:  rubygem(rspec)
%if 0%{?rhel} && 0%{?rhel} <= 7
Requires:       ruby(rubygems)
Provides:       rubygem(%{gem_name}) = %{version}
%endif

%description
Gives you an RubyEngine class that simplifies checking for your Ruby
implementation.

%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
gem build %{gem_name}.gemspec

%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
rspec -Ilib
popd

%files
%license %{gem_instdir}/MIT-LICENSE.txt
%dir %{gem_instdir}/
%{gem_libdir}/
%{gem_spec}
%exclude %{gem_instdir}/pkg/
%exclude %{gem_instdir}/spec/
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.rspec
%exclude %{gem_instdir}/.travis.yml
%exclude %{gem_instdir}/Gemfile
%exclude %{gem_instdir}/Gemfile.lock
%exclude %{gem_instdir}/Rakefile
%exclude %{gem_instdir}/ruby_engine.gemspec
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}/
%doc %{gem_instdir}/ChangeLog.md
%doc %{gem_instdir}/README.rdoc

%changelog
%autochangelog
