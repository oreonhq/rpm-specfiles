%global source0_hash 6bcf8b0e656b6ae9977bdc1351ef211d0383252d2f759a59ef4bcf254542fc46
%global gem_name mime-types
Summary:        The mime-types library provides a library
Name: rubygem-%{gem_name}
Version: 3.4.1
Release:        1%{?dist}
License: MIT
URL: https://github.com/mime-types/ruby-mime-types/
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(logger)
BuildRequires:  rubygem(mime-types-data)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
The mime-types library provides a library and registry for information about
MIME content type definitions. It can be used to determine defined filename
extensions for MIME types, or to use filename extensions to look up the likely
MIME type definitions.
Version 3.0 is a major release that requires Ruby 2.0 compatibility and
removes deprecated functions. The columnar registry format introduced
in 2.6 has been made the primary format; the registry data has been
extracted from this library and put into {mime-types-data}[https://github.com/mime-types/mime-types-data].
Additionally, mime-types is now licensed exclusively under the MIT licence and
there is a code of conduct in effect. There are a number of other smaller
changes described in the History file.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
%description doc
This package contains documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}
# ref: https://github.com/mime-types/ruby-mime-types/pull/183
%gemspec_add_dep -g logger

mv ../%{gem_name}-%{version}.gemspec .

%build

gem build %{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/
find %{buildroot}%{gem_instdir}/{Rakefile,test} -type f | \
  xargs -n 1 sed -i  -e '/^#! \/usr\/bin\/env .*/d'
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
sed -i -e '/^require..minitest-bonus-assertions.$/ s/^/#/' \
    -e '/^require..minitest\/hooks.$/ s/^/#/' \
    -e '/^require..minitest\/focus.$/ s/^/#/' \
    -e '/^require..minitest\/rg.$/ s/^/#/' \
    -e '/^require..fivemat\/minitest\/autorun.$/ s/^/#/' \
  test/minitest_helper.rb
cat << EOF >> test/minitest_helper.rb
def assert_has_keys obj, keys, msg = nil
  keys = [ keys ] unless keys.kind_of?(Array)
  keys.all? { |key| assert obj.key?(key) }
end
EOF
mv test/test_mime_types_cache.rb{,.disable}
ruby -Ilib:test -rminitest/autorun -e 'Dir.glob "./test/**/test_*.rb", &method(:require)'
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-mime-types-doc -f %{oreon_filedir}/rubygem-mime-types-doc.list

%changelog

%autochangelog
