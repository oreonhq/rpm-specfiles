%global source0_hash 63a1af5432b99ed6a908b7f32de7524a660e58db1ab765e58881207f0e1d5db1

# Generated from multi_xml-0.4.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name multi_xml

Name: rubygem-%{gem_name}
Version: 0.7.1
Release: 6%{?dist}
Summary: A generic swappable back-end for XML parsing
License: MIT
URL: https://github.com/sferik/multi_xml
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/sferik/multi_xml.git && cd multi_xml/
# git archive -v -o multi_xml-0.7.1-specs.tar.gz v0.7.1 spec/
Source1: multi_xml-%{version}-specs.tar.gz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(bigdecimal)
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(nokogiri)
BuildRequires: rubygem(ox)
BuildRequires: rubygem(rexml)
BuildArch: noarch

%description
Provides swappable XML backends utilizing LibXML, Nokogiri, Ox, or REXML.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b 1

# ref: https://github.com/sferik/multi_xml/issues/72
# ruby4.0 bumps bigdecimal to 4.0
sed -i ../%{gem_name}-%{version}.gemspec \
        -e '\@add_runtime_dependency.*bigdecimal@s|~> 3\.1|>= 3.1|'

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
ln -s %{_builddir}/spec spec

# We don't care about code coverage.
sed -i '/simplecov/,/^end$/ s/^/#/' spec/helper.rb

rspec spec
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
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CONTRIBUTING.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile

%changelog
%autochangelog
