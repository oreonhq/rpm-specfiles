%global source0_hash de17f58b6761392bd2cbfa97a01bb8b9deae19d395ab7434505d4e45dded4b64

%global gem_name bundler_ext

Summary: Load system gems via Bundler DSL
Name: rubygem-%{gem_name}
Version: 0.4.2
Release: 11%{?dist}
License: MIT
URL: https://github.com/bundlerext/bundler_ext
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(rspec) < 4
BuildRequires: rubygem(bundler)
BuildRequires: rubygem(rails)
BuildArch: noarch

%description
Simple library leveraging the Bundler Gemfile DSL to load gems already on the
system and managed by the systems package manager (like yum/apt)

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}

# https://github.com/ruby/rubygems/pull/9016
# source :rubygems is no longer accepted
sed -i spec/fixtures/Gemfile.in -e 's|source :rubygems|source "https://rubygems.org"|'

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

%check
pushd .%{gem_instdir}
rspec spec
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/MIT-LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/spec

%changelog
%autochangelog
