%global source0_hash a25675ffbd055ae1186766cc1e120b4cf62588e88abb59b99c57e22b1c55c9eb
%global source1_hash 708f4651e46ae744eb8bb7b2866068db6cf05d0ed6e0e843526c7aa3f684296a
%global gem_name bundler
%bcond_with tests
%global connection_pool_version 2.5.0
%global fileutils_version 1.7.3
%global net_http_persistent_version 4.0.4
%global pub_grub_version 0.5.0
%global securerandom_version 0.4.1
%global thor_version 1.3.2
%global tsort_version 0.2.0
%global uri_version 1.0.3
Name: rubygem-%{gem_name}
Version: 2.6.9
Release:        4%{?dist}
Summary:        Library and utilities to manage a Ruby application's gem dependencies
License: MIT AND (Ruby OR BSD-2-Clause)
URL: https://bundler.io
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://codeload.github.com/rubygems/rubygems/tar.gz/bundler-v%{version}#/rubygems-bundler-v%{version}.tar.gz
Patch0:        rubygem-bundler-2.6.9-Revert-changes-in-spec-sectup.patch
Requires: rubygem(io-console)
%if %{with tests}
%endif
Provides: bundled(rubygem-connection_pool) = %{connection_pool_version}
Provides: bundled(rubygem-fileutils) = %{fileutils_version}
Provides: bundled(rubygem-net-http-persistent) = %{net_http_persistent_version}
Provides: bundled(rubygem-pub_grub) = %{pub_grub_version}
Provides: bundled(rubygem-securerandom) = %{securerandom_version}
Provides: bundled(rubygem-thor) = %{thor_version}
Provides: bundled(rubygem-tsort) = %{tsort_version}
Provides: bundled(rubygem-uri) = %{uri_version}
BuildArch: noarch
# oreon:deps
BuildRequires:  /usr/bin/git
BuildRequires:  /usr/bin/man
BuildRequires:  /usr/bin/ps
BuildRequires:  gcc
BuildRequires:  libyaml-devel
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  ruby-devel
BuildRequires:  rubygem(rake)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Bundler manages an application's dependencies through its entire life, across
many machines, systematically and repeatably.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

_specs="%{gem_name}-%{version}-specs.tar.gz"
if test ! -f "$_specs"; then
  rm -rf _bdir && mkdir _bdir
  tar xzf ../rubygems-bundler-v%{version}.tar.gz -C _bdir --strip-components=1
  tar czf "$_specs" -C _bdir bundler/spec tool/bundler/rubocop_gems.rb tool/bundler/standard_gems.rb tool/bundler/test_gems.rb
  rm -rf _bdir
fi

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -c -T
gem unpack ../%{gem_name}-%{version}.gem
tar xf ../%{gem_name}-%{version}-specs.tar.gz -C %{gem_name}-%{version}
cd %{gem_name}-%{version}

( cd %{builddir}
%patch 0 -p1
)

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
for n in 5 1; do
  mkdir -p %{buildroot}%{_mandir}/man${n}
  for file in %{buildroot}%{gem_libdir}/bundler/man/*.${n}; do
    base_name=$(basename "${file}")
    cp -a "${file}" "%{buildroot}%{_mandir}/man${n}/${base_name}"
  done
done
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

( cd .%{gem_instdir}
[ `ls lib/bundler/vendor | wc -l` == 8 ]
[ "`ruby -e " \
  module Bundler; end; \
  require './lib/bundler/vendor/connection_pool/lib/connection_pool/version'; \
  puts Bundler::ConnectionPool::VERSION"`" \
  == '%{connection_pool_version}' ]
[ "`ruby -e " \
  module Bundler; end; \
  require './lib/bundler/vendor/fileutils/lib/fileutils'; \
  puts Bundler::FileUtils::VERSION"`" \
  == '%{fileutils_version}' ]
[ `ruby -Ilib -e '
  module Bundler; end;
  require "bundler/vendor/pub_grub/lib/pub_grub/version";
  puts Bundler::PubGrub::VERSION'` == '%{pub_grub_version}' ]
[ `ruby -Ilib -e '
  module Bundler; module Persistent; module Net; module HTTP; end; end; end; end
  require "bundler/vendor/net-http-persistent/lib/net/http/persistent"
  puts Gem::Net::HTTP::Persistent::VERSION'` == '%{net_http_persistent_version}' ]
[ `ruby -Ilib -e '
  module Bundler; module Random; end; end;
  require "bundler/vendor/securerandom/lib/securerandom";
  puts Bundler::SecureRandom::VERSION'` == '%{securerandom_version}' ]
[ `ruby -e '
  module Bundler; end;
  require "./lib/bundler/vendor/thor/lib/thor/version"
  puts Bundler::Thor::VERSION'` == '%{thor_version}' ]
[ `ruby -Ilib -e '
  module Bundler; end;
  require "bundler/vendor/tsort/lib/tsort";
  puts Bundler::TSort::VERSION'` == '%{tsort_version}' ]
[ "`ruby -e "
  module Bundler; end; \
  require './lib/bundler/vendor/uri/lib/uri/version'; \
  puts Bundler::URI::VERSION"`" \
  == '%{uri_version}' ]
%if %{with tests}
cp -a %{builddir}/bundler/spec .
cp -a %{builddir}/tool ..
sed -i '/"fiddle"/ s/^/#/' ../tool/bundler/test_gems.rb
sed -i '/^    context "when disable_exec_load is set" do$/,/^    end$/ {
  /it "runs" do/a\        skip
}' spec/commands/exec_spec.rb
mkdir -p %{_builddir}/rubygems/rubygems/defaults/
touch %{_builddir}/rubygems/rubygems/defaults/operating_system.rb
sed -i '/def ruby_core_tarball\?/,/^    end$/ {
  /^    end$/i\      # Hardcode standar Bundler layout\n      return false
}' spec/support/path.rb
sed -i '/def git_commit_sha\?/a\      return "unknown"' spec/support/build_metadata.rb
mv spec/quality_spec.rb{,.disable}
mv spec/quality_es_spec.rb{,.disable}
sed -i '/\sruby_repo:\s/ s/ruby_repo: .*/ruby_repo: true/' spec/support/filters.rb
sed -i '/if Spec::Path.ruby_core?/ s/$/ || true/' spec/commands/version_spec.rb
sed -i '/release.*be_falsey/I s/be_falsey/be_truthy/' spec/bundler/build_metadata_spec.rb
sed -i '/it "stays in sync with the rubygems implementation" do/a\    skip' spec/bundler/ci_detector_spec.rb
sed -i 's/VALUE foo()/VALUE foo(VALUE _)/' spec/install/gemfile/git_spec.rb
RUBYOPT=-I%{_builddir}/rubygems GEM_PATH=%{gem_dir} BUNDLER_GEM_DEFAULT_DIR=%{gem_dir} rspec -rspec_helper spec -f d
%endif
)
%files -f %{oreon_filedir}/main.list
%files -n rubygem-bundler-doc -f %{oreon_filedir}/rubygem-bundler-doc.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.6.9-4
- Import
