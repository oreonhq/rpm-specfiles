%global source0_hash b25ea9dceea6de921331ae7ca74158e9878ef5acce05ff3bc3ae1d293f02ccc0

%global	gem_name minitest
# Use full EVR for provides
%global	__provides_exclude_from	%{gem_spec}

Summary:	Small and fast replacement for ruby's huge and slow test/unit

Name:		rubygem-%{gem_name}4
# With 4.7.5, some test fails, so for now use 4.7.0
Version:	4.7.0
Release:	28%{?dist}

License:	MIT
URL:		https://github.com/seattlerb/minitest
Source0:	https://rubygems.org/gems/%{gem_name}-%{version}.gem
# support ruby3.4 formatting change
Patch0:	minitest-4.7.0-ruby34-format.patch
BuildRequires:	rubygems-devel
BuildRequires:	ruby(release)
BuildArch:			noarch
Provides:			rubygem(%{gem_name}) = %{version}-%{release}
# Also provide this
Provides:			rubygem(%{gem_name}4) = %{version}-%{release}
Conflicts:			rubygem-minitest < 4.7.0-3

%description
minitest/unit is a small and fast replacement for ruby's huge and slow
test/unit. This is meant to be clean and easy to use both as a regular
test writer and for language implementors that need a minimal set of
methods to bootstrap a working unit test suite.

miniunit/spec is a functionally complete spec engine.

miniunit/mock, by Steven Baker, is a beautifully tiny mock object framework.

This is a compatibitity package for minitest version 4.x.y.

%package	doc
Summary:	Documentation for %{name}

Requires: %{name} = %{version}-%{release}

%description doc
This package contains documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}
mv ../%{gem_name}-%{version}.gemspec .

# Fix for F-37
sed -i test/minitest/test_minitest_mock.rb \
	-e 's|assert_equal expected, e.message|assert_equal expected, e.message.lines(chomp: true)[0]|'
# Ruby 3.2 removes already deprecated Fixnum
sed -i test/minitest/test_minitest_mock.rb \
	-e 's|Fixnum|Integer|'
# Ruby 3.2 removes Object#=~
sed -i test/minitest/test_minitest_unit.rb -e 's|\(test_refute_match_matcher_object\)|\1; skip|'
# Ruby 3.4 formatting change
%patch -P0 -p1

%build
gem build %{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

find %{buildroot}%{gem_instdir}/lib -type f | \
	xargs -n 1 sed -i  -e '/^#!\/usr\/bin\/ruby.*/d'
# Ships with extremely tight permissions, bring them inline with other gems
find %{buildroot}%{gem_instdir} -type f | \
	xargs chmod 0644

# Cleanup
rm -f %{buildroot}%{gem_instdir}/{.autotest,.gemtest}
rm -f %{buildroot}%{gem_cache}
rm -rf %{buildroot}%{gem_instdir}/{Rakefile,test/}

%check
pushd .%{gem_instdir}

# spec test suite is unstable.
# https://github.com/seattlerb/minitest/issues/257
mv test/minitest/test_minitest_spec.rb{,.ignore}

for f in test/minitest/test_*.rb
do
	ruby -Ilib:.:./test $f
done

%files
%doc	%{gem_instdir}/History.txt
%doc	%{gem_instdir}/Manifest.txt
%license	%{gem_instdir}/README.txt
%dir	%{gem_instdir}
%{gem_libdir}/
%{gem_spec}

%files doc
%{gem_instdir}/design_rationale.rb
%doc	%{gem_docdir}/

%changelog
%autochangelog
