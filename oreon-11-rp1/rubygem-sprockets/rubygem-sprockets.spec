%global source0_hash 5c273487255c47523f30c0b673310fce70a09ca060a6bbcd3e5d0d489e19024c

# Generated from sprockets-2.4.5.gem by gem2rpm -*- rpm-spec -*-
%global gem_name sprockets

Name: rubygem-%{gem_name}
Version: 4.2.0
Release: 10%{?dist}
Summary: Rack-based asset packaging system
License: MIT
URL: https://github.com/rails/sprockets
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/rails/sprockets.git && cd sprockets/
# git archive -v -o sprockets-4.2.0-tests.tar.gz v4.2.0 test/
Source1: sprockets-%{version}-tests.tar.gz
# Fix Minitest 5.19+ test failures.
# https://github.com/rails/sprockets/pull/791
Patch0: rubygem-sprockets-4.2.0-Fix-Minitest-constant-name-in-tests.patch
# Fix compatibility with minitest 6
Patch1: rubygem-sprockets-4.2.0-minitest6.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.5.0
BuildRequires: rubygem(base64)
BuildRequires: rubygem(concurrent-ruby)
BuildRequires: rubygem(execjs)
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(minitest-mock)
BuildRequires: rubygem(nokogiri)
BuildRequires: rubygem(rack-test)
BuildRequires: rubygem(rake)
BuildRequires: rubygem(sass)
BuildRequires: rubygem(sassc)
BuildRequires: rubygem(timecop)
BuildRequires: %{_bindir}/help2man
BuildRequires: %{_bindir}/node
BuildArch: noarch

%description
Sprockets is a Rack-based asset packaging system that concatenates and serves
JavaScript, CoffeeScript, CSS, Sass, and SCSS.

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
%patch 1 -p1
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

mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

# Turn `sprockets --help` into man page
export GEM_PATH="%{buildroot}/%{gem_dir}:%{gem_dir}"
mkdir -p %{buildroot}%{_mandir}/man1
help2man --no-discard-stderr -N -s1 -o %{buildroot}%{_mandir}/man1/%{gem_name}.1 \
    %{buildroot}/usr/share/gems/gems/%{gem_name}-%{version}/bin/%{gem_name}

# Run the test suite
%check
pushd .%{gem_instdir}
ln -s %{_builddir}/test .

# We don't have rubygem(babel-transpiler) yet.
mv test/test_babel_processor.rb{,.disabled}
mv lib/sprockets/autoload/babel.rb{,.disabled}
sed -i '/:Babel/ s/^/#/' lib/sprockets/autoload.rb
sed -i '/es6/ s/^/#/' test/test_asset.rb
sed -i '/test "es6 asset" do/,/^  end$/ s/^/#/' test/test_environment.rb
sed -i '/test "compile babel source map" do/,/^  end$/ s/^/#/' test/test_source_maps.rb

# We don't habe rubygem(closure-compiler) anymore.
# https://src.fedoraproject.org/rpms/rubygem-closure-compiler/c/c0d447db3557cba0d0134e9ab21b9e222066df41
mv test/test_closure_compressor.rb{,.disabled}
mv lib/sprockets/autoload/closure.rb{,.disabled}
sed -i '/:Closure/ s/^/#/' lib/sprockets/autoload.rb

# While we have rubygem(coffee-script) in Fedora ATM, it is not used by RoR
# anymore and the old version prevents update to CoffeeScript 2.x+. Therefore
# rather disable the CoffeeScript test cases.
mv test/test_coffee_script_processor.rb{,.disabled}
mv lib/sprockets/autoload/coffee_script.rb{,.disabled}
sed -i '/:CoffeeScript/ s/^/#/' lib/sprockets/autoload.rb
sed -i \
  -e '/test "asset is stale if a file is added to its require tree" do/a\    skip' \
  -e '/test "processing a source file with different content type extensions 1" do/a\    skip' \
  -e '/test "require_tree requires all descendant files in alphabetical order" do/a\    skip' \
  -e '/test "asset falls back to files default mime type" do/a\    skip' \
  -e '/test "logical path" do/,/end/{ /coffee/ s/^/#/ }' \
  -e '/test "content type" do/,/end/{ /coffee/ s/^/#/ }' \
  test/test_asset.rb
sed -i \
  -e '/test "find bundled asset with implicit format" do/a\    skip' \
  -e '/test "CoffeeScript files are compiled in a closure" do/a\    skip' \
  -e '/test "find source for concatenated asset" do/a\    skip' \
  -e '/test "processor returning a non-string data" do/a\    skip' \
  -e '/test "processor returning a subclassed string data" do/a\    skip' \
  -e '/test "processor returning a complex metadata type" do/a\    skip' \
  -e '/test "bundled asset cached if theres an error building it" do/a\    skip' \
  -e '/test "asset logical path for absolute path" do/,/end/{ /application\./ s/^/#/ }' \
  -e '/test "find asset with accept type" do/,/end/{ /coffee\/foo/ s/^/#/ }' \
  -e '/test "find bower main by format extension" do/,/end/{ /rails/ s/^/#/ }' \
  -e '/test "find bower main by content type" do/,/end/{ /rails/ s/^/#/ }' \
  test/test_environment.rb
sed -i '/test .load uri with index alias. do/a\    skip' test/test_loader.rb
sed -i '/def test_compose_coffee_and_uglifier/a\    skip' test/test_processor_utils.rb
sed -i \
  -e '/test "correct offsets" do/a\    skip' \
  -e '/test "builds a source map with js dependency" do/a\    skip' \
  -e '/test "builds a concatenated source map" do/a\    skip' \
  -e '/test "compile coffeescript source map" do/a\    skip' \
  -e '/test "source maps work with index alias" do/a\    skip' \
  -e '/test "rebuilds a source map when related dependency has changed" do/a\    skip' \
  test/test_source_maps.rb
# The following has more failures then passing tests without CoffeeScript.
mv test/test_exporting.rb{,.disabled}
mv test/test_manifest.rb{,.disabled}
mv test/test_rake_task.rb{,.disabled}

# We don't have rubygem(eco) yet.
mv test/test_eco_processor.rb{,.disabled}
mv lib/sprockets/autoload/eco.rb{,.disabled}
sed -i '/:Eco/ s/^/#/' lib/sprockets/autoload.rb
sed -i '/test "eco templates" do/,/^  end/ s/^/#/' test/test_environment.rb

# While we have rubygem(ejs) in Fedora ATM, the library is not maintained
# upsteram, therefore it will be better to drop the dependency.
mv test/test_ejs_processor.rb{,.disabled}
mv lib/sprockets/autoload/ejs.rb{,.disabled}
sed -i '/:EJS/ s/^/#/' lib/sprockets/autoload.rb
sed -i \
  -e '/test "logical path" do/,/end/{ /\.ejs/ s/^/#/ }' \
  -e '/test "content type" do/,/end/{ /\.ejs/ s/^/#/ }' \
  test/test_asset.rb
sed -i \
  -e '/test "ejs templates" do/a\    skip' \
  -e '/test "find_asset! does not raise an exception when asset is found" do/,/end/ s/hello.js/gallery.css/' \
  -e '/test "change jst template namespace" do/a\    skip' \
  test/test_environment.rb

# We don't have rubygem(jsminc) yet.
mv test/test_jsminc_compressor.rb{,.disabled}
mv lib/sprockets/autoload/jsminc.rb{,.disabled}
sed -i '/:JSMinC/ s/^/#/' lib/sprockets/autoload.rb

# While we have rubygem(uglifier), it bundles uglify-js, it is not well
# maintained, while RoR does not depend on it anymore. It will be better
# to avoid this dependency.
mv test/test_uglifier_compressor.rb{,.disabled}
mv lib/sprockets/autoload/uglifier.rb{,.disabled}
sed -i '/:Uglifier/ s/^/#/' lib/sprockets/autoload.rb
sed -i '/test "builds a minified source map" do/a\    skip' test/test_source_maps.rb
sed -i '/test "minify js with uglify" do/a\    skip' test/test_sprocketize.rb

# We don't have rubygem(yui-compressor) yet.
# https://bugzilla.redhat.com/show_bug.cgi?id=725768
mv test/test_yui_compressor.rb{,.disabled}
mv lib/sprockets/autoload/yui.rb{,.disabled}
sed -i '/:YUI/ s/^/#/' lib/sprockets/autoload.rb

# This test tries to ensure, that all files are loadable. Nevertheless
# 1) we don't have all dependencies, 2) this is more interesting for upstream
# 3) there is logical bug in the test case, therefore it might fail without
# Bundler: https://github.com/rails/sprockets/issues/780
mv test/test_require.rb{,.disabled}

# Required by TestPathUtils#test_find_upwards test.
touch Gemfile

ruby -Ilib:test -e 'Dir.glob "./test/**/test_*.rb", &method(:require)'

# Check content of man page created by help2man.
gunzip -c %{buildroot}%{_mandir}/man1/%{gem_name}.1.gz | \
  grep -q '^Adds the directory to the Sprockets load path'
popd

%files
%dir %{gem_instdir}
%{_bindir}/sprockets
%license %{gem_instdir}/MIT-LICENSE
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%{_mandir}/man1/%{gem_name}.1*

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md

%changelog
%autochangelog
