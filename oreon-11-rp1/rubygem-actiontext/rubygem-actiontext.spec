%global source0_hash fae6adfa799bb05cc138ba23339f29ff7f29dc3db133a013030f484e91a8194e

# Generated from actiontext-6.0.3.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name actiontext

# TODO: Re-enable recompilation if possible. Currently, we don't have rollup.js
# in Fedora and therefore it requires network access. Still good for checking
# the results
%bcond_with js_recompilation

Name: rubygem-%{gem_name}
Version: 8.0.3
Release: 2%{?dist}
Summary: Rich text framework
License: MIT
URL: https://rubyonrails.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}%{?prerelease}.gem
# git clone https://github.com/rails/rails.git --no-checkout && cd rails/actiontext
# git archive -v -o actiontext-8.0.3-tests.tar.gz v8.0.3 test/
Source1: %{gem_name}-%{version}%{?prerelease}-tests.tar.gz
# Source code of pregenerated JS files.
# git clone https://github.com/rails/rails.git && cd rails/actiontext
# git archive -v -o actiontext-8.0.3-js.tar.gz v8.0.3 app/javascript rollup.config.js
Source2: %{gem_name}-%{version}%{?prerelease}-js.tar.gz

BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 3.2.0
BuildRequires: rubygem(actionmailer) = %{version}
BuildRequires: rubygem(activestorage) = %{version}
BuildRequires: rubygem(bundler)
BuildRequires: rubygem(image_processing)
BuildRequires: rubygem(importmap-rails)
BuildRequires: rubygem(railties) = %{version}
BuildRequires: rubygem(sprockets-rails)
BuildRequires: rubygem(sqlite3)
BuildRequires: rubygem(capybara) >= 3.26
BuildRequires: rubygem(puma)
BuildRequires: rubygem(selenium-webdriver)
BuildRequires: chromedriver chromium chromium-headless
# Chromium availability is limited:
# https://src.fedoraproject.org/rpms/chromium/blob/0d9761748509bb12051ab149d28c1052cd834f87/f/chromium.spec#_800
# and chrome-headless even more:
# https://src.fedoraproject.org/rpms/chromium/blob/0d9761748509bb12051ab149d28c1052cd834f87/f/chromium.spec#_46-48
ExclusiveArch: x86_64 aarch64 noarch
%{?with_js_recompilation:BuildRequires: %{_bindir}/npm}
BuildArch: noarch

# Bundles Trix editor.
# https://trix-editor.org/
# https://github.com/basecamp/trix
# app/assets/javascripts/trix.js
# TODO: would be nice to check the version. Althoug the bundled Trix is going
# to be extracted into independent gem: https://github.com/rails/rails/pull/55058
Provides: bundled(js-trix) = 2.1.12

%description
Edit and display rich text in Rails applications.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}%{?prerelease} -b1 -b2

%build
%if %{with js_recompilation}
# Recompile the embedded JS files from sources.
#
# This is practice suggested by packaging guidelines:
# https://fedoraproject.org/wiki/Packaging:Guidelines#Use_of_pregenerated_code

find app/assets/ -type f -exec sha512sum {} \;

rm -rf app/assets/javacripts/actiontext.*

ln -s %{builddir}/app/javascript ./app/javascript
cp -a %{builddir}/rollup.config.js .

# TODO: This requires network access. Use Fedora rollup.js if it becomes
# available eventually
# `rollup-plugin-terser` is missing from package.json, otherwise `npm install`
# would be enough.
# https://github.com/rails/rails/issues/54795
npm install rollup-plugin-terser
npx rollup --config rollup.config.js

# For comparison with the orginal checksum above.
find app/assets/ -type f -exec sha512sum {} \;
%endif

gem build ../%{gem_name}-%{version}%{?prerelease}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
( cd .%{gem_instdir}
cp -a %{builddir}/test .

mkdir ../tools
# Fake test_common.rb. It does not provide any functionality besides
# `force_skip` alias.
touch ../tools/test_common.rb
# Netiher strict_warnings.rb appears to be useful.
touch ../tools/strict_warnings.rb

export BUNDLE_GEMFILE=${PWD}/../Gemfile

# The `Gemfiles` is unavoidable, otherwise `importmap-rails` are not properly
# loaded.
cat > $BUNDLE_GEMFILE <<EOF
gem "actionmailer"
gem "activestorage"
gem "capybara"
gem "image_processing"
gem "importmap-rails"
gem "puma"
gem "railties"
gem "selenium-webdriver"
gem "sprockets-rails"
gem "sqlite3"
EOF

# test/javascript_package_test.rb requires rollup.js, which we don't have.
# OTOH, if we had it, we would recomplie the sources and the test would have
# less value.
mv test/javascript_package_test.rb{,.disable}

ruby -Itest -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
)

%files
%dir %{gem_instdir}
%license %{gem_instdir}/MIT-LICENSE
%{gem_instdir}/app
%{gem_instdir}/db
%{gem_libdir}
%{gem_instdir}/package.json
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md

%changelog
%autochangelog
