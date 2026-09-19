%global source0_hash 18fd90b6eb76ed3fed1a415136ee969d3457a64a1ba06b134297ec91ddd7f0f8

# Generated from multi_json-1.0.3.gem by gem2rpm -*- rpm-spec -*-
%global gem_name multi_json

Name: rubygem-%{gem_name}
Version: 1.15.0
Release: 13%{?dist}
Summary: A common interface to multiple JSON libraries
License: MIT
URL: https://github.com/intridea/multi_json
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/intridea/multi_json.git && cd multi_json
# git archive -v -o multi_json-1.15.0-spec.tar.gz v1.15.0 spec/
Source1: %{gem_name}-%{version}-spec.tar.gz
# Fix RSpec 3.11.0+ compatibility due to improved kwargs handling.
# https://github.com/intridea/multi_json/pull/205
Patch0: rubygem-mulit_json-1.15.0-RSpec-3.11.0-distinguishes-between-hashed-and-Ruby-3.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel >= 1.3.5
BuildRequires: ruby
BuildRequires: rubygem(rspec)
BuildArch: noarch
# OkJson is allowed to be bundled:
# https://fedorahosted.org/fpc/ticket/113
Provides: bundled(okjson) = 45

%description
A common interface to multiple JSON libraries, including Oj, Yajl, the JSON
gem (with C-extensions), the pure-Ruby JSON gem, NSJSONSerialization, gson.rb,
JrJackson, and OkJson.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b 1

pushd %{_builddir}
%patch 0 -p1
popd

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
ln -s %{_builddir}/spec spec

# json_pures is not available on Fedora.
sed -i "/require.*json\/pure/ s/^/#/" spec/multi_json_spec.rb
sed -i "s/JsonPure/OkJson/" spec/multi_json_spec.rb
sed -i "s/json_pure/ok_json/" spec/multi_json_spec.rb
# oj is not available on Fedora.
sed -i "/expect(MultiJson.adapter.to_s).to eq('MultiJson::Adapters::Oj')/ s/Oj/JsonGem/" spec/multi_json_spec.rb

# Execute main test suite.
SKIP_ADAPTERS=jr_jackson rspec spec/{multi_json,options_cache}_spec.rb

# json_pure adapter does not support skipping :/
mv spec/json_pure_adapter_spec.rb{,.disable}

# Adapters have to be tested separately, but disable test of engines
# unsupported on Fedora (they may cause test suite to fail).
for adapter in spec/*_adapter_spec.rb; do
  SKIP_ADAPTERS=json_pure,gson,jr_jackson,nsjsonserialization,oj,yajl rspec $adapter
done

popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE.md
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/README.md

%changelog
%autochangelog
