%global source0_hash dc229a74f5d181f09942dd60ab5d6e667f7392c4ee826f35096db36d1fe3614c

%global gem_name i18n

%bcond_without tests

Name: rubygem-%{gem_name}
Version: 1.14.6
Release: 4%{?dist}
Summary: New wave Internationalization support for Ruby
# `BSD or Ruby` due to header of lib/i18n/gettext/po_parser.rb
License: MIT AND (BSD-2-Clause OR Ruby)
URL: https://github.com/ruby-i18n/i18n
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone --no-checkout https://github.com/ruby-i18n/i18n && cd i18n
# git archive -v -o i18n-1.14.6-tests.tar.xz v1.14.6 test
Source1: %{gem_name}-%{version}-tests.tar.xz
# Fix `NameError: uninitialized constant I18nLoadPathTest::Pathname` test
# errors.
# https://github.com/ruby-i18n/i18n/pull/708
Patch0: rubygem-i18n-1.14.6-Explicitly-require-pathname.patch
# Fix Ruby 3.4 `Hash#inspect` compatibility.
# https://github.com/ruby-i18n/i18n/pull/709
Patch1: rubygem-i18n-1.14.6-Ruby-3.4-Hash-inspect-compatibility.patch
Patch2: rubygem-i18n-1.14.6-Ruby-3.4-Hash-inspect-compatibility-test.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
%if %{with tests}
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(mocha)
BuildRequires: rubygem(test_declarative)
BuildRequires: rubygem(concurrent-ruby)
BuildRequires: rubygem(activesupport)
BuildREquires: rubygem(racc)
%endif
BuildArch: noarch

%description
Ruby internationalization and localization solution.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b1

%patch 1 -p1

pushd %{builddir}
%patch 0 -p1
%patch 2 -p1
popd

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%if %{with tests}
%check
pushd .%{gem_instdir}
ln -s %{builddir}/test .

# Bundler just complicates everything in our case, remove it.
sed -i -e "/require 'bundler\/setup'/ s/^/#/" test/test_helper.rb

find ./test/ -type f -name '*_test.rb' | \
  xargs -n 1 ruby -Ilib:test
popd
%endif

%files
%dir %{gem_instdir}
%license %{gem_instdir}/MIT-LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
%autochangelog
