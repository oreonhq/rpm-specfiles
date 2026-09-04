%global source0_hash 52b9fea10701461dd3eaf9d9839702169b418dbbf50426786b9b74fade373bd6

# Generated from fog-xml-0.1.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name fog-xml

Name: rubygem-%{gem_name}
Version: 0.1.5
Release: 1%{?dist}
Summary: XML parsing for fog providers
License: MIT
URL: https://github.com/fog/fog-xml
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(fog-core)
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(nokogiri)
BuildArch: noarch

%description
Extraction of the XML parsing tools shared between a
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
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
# We don't have Turn in Fedora (neither we really need it).
sed -i '/require.*turn/ s/^/#/' spec/minitest_helper.rb
sed -i '/Turn/,/end/ s/^/#/' spec/minitest_helper.rb

ruby -Ispec -e 'Dir.glob "./spec/**/*_spec.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/LICENSE.md
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/CONTRIBUTORS.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/fog-xml.gemspec
%{gem_instdir}/gemfiles
%{gem_instdir}/spec

%changelog
%autochangelog
