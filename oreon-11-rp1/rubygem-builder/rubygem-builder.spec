%global source0_hash 497918d2f9dca528fdca4b88d84e4ef4387256d984b8154e9d5d3fe5a9c8835f

%global gem_name builder

Name: rubygem-%{gem_name}
Version: 3.3.0
Release: 4%{?dist}
Summary: Builders for MarkUp
License: MIT
URL: https://github.com/rails/builder
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(minitest)
BuildArch: noarch

%description
Builder provides a number of builder objects that make creating structured
data simple to do. Currently the following builder objects are supported:
* XML Markup
* XML Events

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

# Remove shebangs from test files.
# https://github.com/rails/builder/pull/25
pushd %{buildroot}%{gem_instdir}
  find -type f -name '*.rb' -print | xargs sed -i '/#!\/usr\/bin\/env/d'
popd

# Remove shebang from rake file.
sed -i '/#!\/usr\/bin\/env/d' %{buildroot}%{gem_instdir}/rakelib/tags.rake
chmod a-x %{buildroot}%{gem_instdir}/rakelib/tags.rake

%check
pushd .%{gem_instdir}
ruby -Ilib:test -e 'Dir.glob "./test/test_*.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/MIT-LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGES
%{gem_instdir}/Gemfile*
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/builder.blurb
%{gem_instdir}/builder.gemspec
%doc %{gem_instdir}/doc
%{gem_instdir}/rakelib
%{gem_instdir}/test

%changelog
%autochangelog
