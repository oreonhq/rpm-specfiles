%global source0_hash 6e759246556145642ef832d670fc06f9bd8539159a0e600847a00291dd7aae0c

# Generated from haml-2.2.14.gem by gem2rpm -*- rpm-spec -*-
%global gem_name haml

Name: rubygem-%{gem_name}
Version: 5.2.2
Release: 14%{?dist}
Summary: An elegant, structured (X)HTML/XML templating engine
License: MIT and WTFPL
URL: http://haml.info/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone --no-checkout https://github.com/haml/haml.git
# git -C haml archive -v -o haml-5.2.2-tests.txz v5.2.2 test/
Source1: %{gem_name}-%{version}-tests.txz
# Explicitly include ostruct due to json 2.7.2 change
Patch0:  rubygem-haml-5.2.2-explicit-ostruct-dep.patch
# Support ruby3.4 Hash#inspect format change
# Note that haml 6.0 changes codebase a lot and
# the file modified in the patch no longer exists:
# https://github.com/haml/haml/commit/11bb81149f4b048fe9282ed9be0dd10bfbc710b2
Patch1:  rubygem-haml-5.2.2-ruby34-hash-inspect-formatting-change.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(activemodel)
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(railties)
BuildRequires: rubygem(temple)
BuildRequires: rubygem(tilt)
BuildArch: noarch

%description
Haml (HTML Abstraction Markup Language) is a layer on top of HTML or XML
that's designed to express the structure documents in a non-repetitive,
elegant, easy way by using indentation rather than closing
tags and allowing Ruby to be embedded with ease.
It was originally envisioned as a plugin for Ruby on Rails, but it can
function as a stand-alone templating engine.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b 1
(
cd %{_builddir}
%patch 0 -p1
%patch 1 -p1
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

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%check
pushd .%{gem_instdir}
# Link test suite into the place.
ln -s %{_builddir}/test .

# Get rid of Bundler.
sed -i '/[bB]undler/ s/^/#/' test/test_helper.rb

# We don't care about code coverage
sed -i '/[Ss]imple[Cc]ov/ s/^/#/g' test/test_helper.rb

# Disable test_annotated_template_names that's not working (removed in next release)
mv test/template_test.rb{,.disable}

# Avoid `ActionView::Template::Error: unknown keyword: :has_strict_locals`
# error in Rails 8, which intoduced this kwarg:
# https://github.com/rails/rails/commit/bbe7d19e11d1cd6374c667c38428c0c783bed3b5
# Just FTR, this file was dropped in more recent HAML:
# https://github.com/haml/haml/commit/11bb81149f4b048fe9282ed9be0dd10bfbc710b2#diff-2acf37380293c4739141a2f05134fa30a6d8f2716e5574a9598265fbf86a0854
sed -i '/def _run/ s/add_to_stack: true, &block/add_to_stack: true, has_strict_locals: false, \&block/' \
  test/helpers_for_rails_test.rb

# options_test.rb must be executed in isolation in order to prevent load
# order issues.
# https://github.com/haml/haml/issues/943
ruby -Ilib:test -e '(Dir.glob("./test/*_test.rb") - %w[./test/options_test.rb]).each {|f| require f }'
ruby -Ilib:test -e 'require "./test/options_test.rb"'
popd

%files
%dir %{gem_instdir}
%{_bindir}/haml
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/MIT-LICENSE
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_libdir}/haml/.gitattributes
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/FAQ.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/REFERENCE.md
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/TODO
%{gem_instdir}/benchmark.rb
%{gem_instdir}/haml.gemspec
%{gem_instdir}/yard
%exclude %{gem_instdir}/yard/default/.gitignore

%changelog
%autochangelog
