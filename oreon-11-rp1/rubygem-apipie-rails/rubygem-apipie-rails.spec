%global source0_hash 727c2a74d913cd0cb601d3675800672b7b5a6b0c61349805c0582431a12f2f45

# Generated from apipie-rails-0.0.13.gem by gem2rpm -*- rpm-spec -*-
%global gem_name apipie-rails

Name: rubygem-%{gem_name}
Version: 1.5.1
Release: 1%{?dist}
Summary: Rails REST API documentation tool
# The project itself is MIT
# For ASL 2.0, see https://github.com/Apipie/apipie-rails/issues/66
# (bundled JS files under app/public)
License: MIT AND Apache-2.0
URL: http://github.com/Apipie/apipie-rails
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Fix Rails 7.2+ compatibility
# https://github.com/Apipie/apipie-rails/pull/948
Patch0: rubygem-apipie-rails-1.4.2-Fix-ActiveSupport-Deprecation-warn-deprecation.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: %{_bindir}/rspec
BuildRequires: rubygem(railties)
BuildRequires: rubygem(rails-controller-testing)
BuildRequires: rubygem(rspec-rails)
# app/public/apipie/javascripts/bundled/jquery.js
Provides: bundled(js-jquery1) = 1.12.4
# app/public/apipie/javascripts/bundled/bootstrap*.js
Provides: bundled(js-bootstrap) = 2.3.2
BuildArch: noarch

%description
Apipie-rails is a DSL and Rails engine for documenting your RESTful API.
Instead of traditional use of #comments, Apipie lets you describe the code,
through the code. This brings advantages like:

* No need to learn yet another syntax, you already know Ruby, right?
* Possibility of reusing the docs for other purposes (such as validation)
* Easier to extend and maintain (no string parsing involved)
* Possibility of reusing other sources for documentation purposes (such as
  routes etc.)

The documentation is available from within your app (by default under the
/apipie path.) In development mode, you can see the changes as you go. It's
markup language agnostic, and even provides an API for reusing the
documentation data in JSON.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}

%patch 0 -p1

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

# Remove empty .gitkeep files, that rpmlint complains about, we don't need
# them in RPMs.
find %{buildroot}%{gem_instdir}/spec -type f -name '.gitkeep' -exec rm {} \;

%check
pushd .%{gem_instdir}
# Don't use Bundler.
sed -i "/require 'bundler\/setup'/ s/^/#/" spec/spec_helper.rb
sed -i "/Bundler.require/ s/^/#/" spec/dummy/config/application.rb
rm Gemfile

# We don't care about code coverage.
sed -i '/[sS]imple[cC]ov/ s/^/#/' spec/spec_helper.rb

# We don't have json-schema in Fedora ATM :/
# https://bugzilla.redhat.com/show_bug.cgi?id=1675932
for f in \
  spec/lib/apipie/apipies_controller_spec.rb \
  spec/lib/swagger/rake_swagger_spec.rb
do
  sed -i "/json-schema/ s/^/#/" $f
  sed -i "/JSON::Validator/ s/^/#/" $f
done
mv spec/controllers/pets_controller_spec.rb{,.disable}

rspec -Ispec/dummy/components/test_engine/lib -rrails-controller-testing spec
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/APACHE-LICENSE-2.0
%license %{gem_instdir}/MIT-LICENSE
%license %{gem_instdir}/NOTICE
%{gem_instdir}/app
%{gem_instdir}/config
%{gem_libdir}
# exclude useless rel-eng directory
%exclude %{gem_instdir}/rel-eng
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/PROPOSAL_FOR_RESPONSE_DESCRIPTIONS.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/apipie-rails.gemspec
%{gem_instdir}/gemfiles
%{gem_instdir}/images
%{gem_instdir}/spec

%changelog
%autochangelog
