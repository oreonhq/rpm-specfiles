%global source0_hash 16bc9a793337abd54b5c17d588ba45665b4ff44cffb9aca66704190643608270
%global gem_name apipie-rails
Name: rubygem-%{gem_name}
Version: 1.4.2
Release:        3%{?dist}
Summary:        Rails REST API documentation tool
License: MIT AND Apache-2.0
URL: http://github.com/Apipie/apipie-rails
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch0: rubygem-apipie-rails-1.4.2-Fix-ActiveSupport-Deprecation-warn-deprecation.patch
Provides: bundled(js-jquery1) = 1.12.4
Provides: bundled(js-bootstrap) = 2.3.2
BuildArch: noarch
# oreon:deps
BuildRequires:  /usr/bin/rspec
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(rails-controller-testing)
BuildRequires:  rubygem(railties)
BuildRequires:  rubygem(rspec-rails)
BuildRequires:  rubygems-devel
# /oreon:deps
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

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
find %{buildroot}%{gem_instdir}/spec -type f -name '.gitkeep' -exec rm {} \;
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
sed -i "/require 'bundler\/setup'/ s/^/#/" spec/spec_helper.rb
sed -i "/Bundler.require/ s/^/#/" spec/dummy/config/application.rb
rm Gemfile
sed -i '/[sS]imple[cC]ov/ s/^/#/' spec/spec_helper.rb
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
%files -f %{oreon_filedir}/main.list
%files -n rubygem-apipie-rails-doc -f %{oreon_filedir}/rubygem-apipie-rails-doc.list

%changelog

%autochangelog
