%global source0_hash dd4f5ab362dbc72b687240bba9d2dd841d5dfe888a285797533f85c03ea548fe
%global gem_name fog-json
Name: rubygem-%{gem_name}
Version: 1.2.0
Release:        1%{?dist}
Summary:        JSON parsing for fog providers
License: MIT
URL: http://github.com/fog/fog-json
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(fog-core)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygem(multi_json)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Extraction of the JSON parsing tools shared between a
number of providers in the 'fog' gem.

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

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
ruby -Ilib -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-fog-json-doc -f %{oreon_filedir}/rubygem-fog-json-doc.list

%changelog

%autochangelog
