%global source0_hash 51b8aba24230240cb6d78e01b9e9efee280d329f535f30f7f488b6467c7775d3

%global gem_name pdf-core

Name: rubygem-%{gem_name}
Version: 0.9.0
Release: 13%{?dist}
Summary: PDF::Core is used by Prawn to render PDF documents
# Automatically converted from old format: GPLv2 or GPLv3 or Ruby - review is highly recommended.
License: GPL-2.0-only OR GPL-3.0-only OR Ruby 
URL: https://github.com/prawnpdf/pdf-core
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/prawnpdf/pdf-core && cd pdf-core
# git checkout 0.9.0 && tar czvf pdf-core-0.9.0-specs.tgz spec/
Source1: %{gem_name}-%{version}-specs.tgz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel >= 1.3.6
BuildRequires: ruby >= 1.9.3
BuildRequires: rubygem(pdf-reader) => 1.2
BuildRequires: rubygem(pdf-inspector) => 1.1.0
BuildRequires: rubygem(rspec)

BuildArch: noarch

%description
PDF::Core is used by Prawn to render PDF documents.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b1

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
# Symlinking does not work for this test suite
cp -r %{_builddir}/spec .

# get rid of bundler
sed -i -e "s/require 'bundler'//" spec/spec_helper.rb
sed -i -e 's/Bundler.setup//' spec/spec_helper.rb
rspec spec
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%license %{gem_instdir}/LICENSE
%doc %{gem_instdir}/COPYING
%doc %{gem_instdir}/GPLv2
%doc %{gem_instdir}/GPLv3

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/%{gem_name}.gemspec

%changelog
%autochangelog
