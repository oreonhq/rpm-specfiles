%global source0_hash a56522a7aa15eb8b9d4be1e3d879536cba4d8a0a8b1ee7e622976023f4bfe3b5

%global gem_name prawn-icon

Name: rubygem-%{gem_name}
Version: 4.1.0
Release: 1%{?dist}
Summary: Provides icon fonts for PrawnPDF
# Automatically converted from old format: Ruby or GPLv2 or GPLv3 - review is highly recommended.
License: Ruby OR GPL-2.0-only OR GPL-3.0-only
URL: https://github.com/jessedoyle/prawn-icon/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(prawn)
BuildRequires: rubygem(pdf-inspector)
BuildArch: noarch

%description
Prawn::Icon provides various icon fonts including
FontAwesome, Foundation Icons and GitHub Octicons
for use with the Prawn PDF toolkit.

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

%check
pushd .%{gem_instdir}
# Don't use Bundler.
sed -i "/require \"bundler\"/ s/^/#/" spec/spec_helper.rb
sed -i "/Bundler.setup/ s/^/#/" spec/spec_helper.rb
sed -i "/require 'simplecov'/ s/^/#/" spec/spec_helper.rb
sed -i "/SimpleCov.start/ s/^/#/" spec/spec_helper.rb
rspec -rprawn spec
popd

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/README.md
%license %{gem_instdir}/COPYING
%license %{gem_instdir}/GPLv2
%license %{gem_instdir}/GPLv3
%license %{gem_instdir}/LICENSE
%{gem_instdir}/data
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/examples
%{gem_instdir}/prawn-icon.gemspec
%{gem_instdir}/spec

%changelog
%autochangelog
