%global source0_hash 30249727f488012118ba30f5f65a45e51ac0c8e17e4fcef136d58996c49150a8

# Generated from rdoc-3.4.gem by gem2rpm -*- rpm-spec -*-
%global gem_name rdoc

Name: rubygem-%{gem_name}
Version: 7.0.3
Release: 201%{?dist}
Summary: RDoc produces HTML and command-line documentation for Ruby projects
# BSD-3-Clause: lib/rdoc/generator/darkfish.rb
# CC-BY-2.5: lib/rdoc/generator/template/darkfish/images/loadingAnimation.gif
# MIT: lib/rdoc/generator/aliki.rb
# MIT: lib/rdoc/generator/template/aliki/*
# OFL-1.1-RFN: lib/rdoc/generator/template/darkfish/css/fonts.css
# Note that RDoc now embeds Racc parser:
# https://github.com/ruby/rdoc/pull/1019
# Luckily, this should have no license impact:
# https://github.com/ruby/racc/blob/5eb07b28bfb3e193a1cac07798fe7be7e1e246c4/lib/racc/parser.rb#L8-L10
# Please also note that there are uncertainties about the license:
# https://github.com/ruby/rdoc/issues/401
# https://github.com/ruby/rdoc/issues/924
License: %{shrink:
    GPL-2.0-only AND
    Ruby AND
    BSD-3-Clause AND
    CC-BY-2.5 AND
    MIT AND
    OFL-1.1-RFN
}
URL: https://ruby.github.io/rdoc
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/ruby/rdoc.git --no-checkout && cd rdoc
# git archive -v -o rdoc-%%{version}-tests.tar.gz v%%{version} test/
Source1: %{gem_name}-%{version}-tests.tar.gz
# Fix ruby_version abuse. Keep this in sinc with ruby-2.3.0-ruby_version.patch
# applied in ruby package.
# https://bugs.ruby-lang.org/issues/11002
Patch0: rubygem-rdoc-5.1.0-ruby_version.patch
# https://github.com/ruby/rdoc/pull/1531
# Fix error with `gem install --document=rdoc,ri`
Patch1: rdoc-pr1531-fix-mutilple-document-installation.patch
Requires: rubygem(irb)
Requires: rubygem(io-console)
Requires: rubygem(json)
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(test-unit-ruby-core)
# test/rdoc/test_rdoc_i18n_locale.rb
BuildRequires: rubygem(gettext)
# Execute Rake integration test cases.
BuildRequires: rubygem(rake)
# test/rdoc/test_rdoc_servlet.rb
BuildRequires: rubygem(webrick)
Provides: rdoc = %{version}-%{release}
Provides: ri = %{version}-%{release}
BuildArch: noarch

%description
RDoc produces HTML and command-line documentation for Ruby projects.
RDoc includes the +rdoc+ and +ri+ tools for generating and displaying
documentation from the command-line.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -a 1

%patch 0 -p1
%patch 1 -p1

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/exe -type f | xargs chmod a+x

for n in 1; do
  mkdir -p %{buildroot}%{_mandir}/man${n}
  for file in %{buildroot}%{gem_instdir}/man/*.${n}; do
    base_name=$(basename "${file}")
    cp -a "${file}" "%{buildroot}%{_mandir}/man${n}/${base_name}"
  done
done

%check
( cp -a test .%{gem_instdir}
cd .%{gem_instdir}
sed -i '/^\s*require..bundler/ s/^/#/g' test/rdoc/support/test_case.rb

# Give `lib` precedence over system location, otherwise strange timestamp
# failures might happen.
RUBYOPT=-Ilib \
  ruby -e 'Dir.glob "./test/**/*_test.rb", &method(:require)' -- -v
)

%files
%dir %{gem_instdir}
%{_bindir}/rdoc
%{_bindir}/ri
%license %{gem_instdir}/LICENSE.rdoc
%license %{gem_instdir}/LEGAL.rdoc
%{gem_instdir}/exe
%{gem_libdir}
%exclude %{gem_instdir}/man
%exclude %{gem_cache}
%{gem_plugin}
%{gem_spec}
%doc %{_mandir}/man1/*

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/CVE-2013-0256.rdoc
%doc %{gem_instdir}/Example*
%doc %{gem_instdir}/History.rdoc
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/RI.md
%doc %{gem_instdir}/TODO.rdoc
%{gem_instdir}/rdoc.gemspec

%changelog
%autochangelog
