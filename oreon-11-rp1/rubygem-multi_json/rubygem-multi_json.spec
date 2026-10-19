%global source1_hash 07592431d0926f6b2716171d81a33120574b1ade346b8616b2b5dcb67635be6b
%global source0_hash 1fd04138b6e4a90017e8d1b804c039031399866ff3fbabb7822aea367c78615d
%global gem_name multi_json
Name: rubygem-%{gem_name}
Version: 1.15.0
Release:        1%{?dist}
Summary:        A common interface to multiple JSON libraries
License: MIT
URL: https://github.com/intridea/multi_json
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/intridea/multi_json/archive/refs/tags/v1.15.0.tar.gz
Patch0: rubygem-mulit_json-1.15.0-RSpec-3.11.0-distinguishes-between-hashed-and-Ruby-3.patch
BuildArch: noarch
Provides: bundled(okjson) = 45
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygems-devel
# /oreon:deps
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
find %{_builddir} -mindepth 2 -type d \( -name test -o -name tests -o -name spec -o -name specs \) -exec cp -a {} %{_builddir}/ \;

pushd %{_builddir}
%patch 0 -p1
popd

%build

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
ln -s %{_builddir}/spec spec
sed -i "/require.*json\/pure/ s/^/#/" spec/multi_json_spec.rb
sed -i "s/JsonPure/OkJson/" spec/multi_json_spec.rb
sed -i "s/json_pure/ok_json/" spec/multi_json_spec.rb
sed -i "/expect(MultiJson.adapter.to_s).to eq('MultiJson::Adapters::Oj')/ s/Oj/JsonGem/" spec/multi_json_spec.rb
SKIP_ADAPTERS=jr_jackson rspec spec/{multi_json,options_cache}_spec.rb
mv spec/json_pure_adapter_spec.rb{,.disable}
for adapter in spec/*_adapter_spec.rb; do
  SKIP_ADAPTERS=json_pure,gson,jr_jackson,nsjsonserialization,oj,yajl rspec $adapter
done
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-multi_json-doc -f %{oreon_filedir}/rubygem-multi_json-doc.list

%changelog

%autochangelog
