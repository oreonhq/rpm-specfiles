%global source0_hash dc530018a4684512f8f38143cd2a096c9f02a1fc2459edcfe534787a7fc77d4b
%global source1_hash d9349a02080ff7ff48737ec946d2e7e872961af7a14829715ba6432616fbcd42

%global gem_name coderay

%if %{undefined rhel} || (0%{?oreon} >= 11)
%bcond_without shoulda
%endif

Name: rubygem-%{gem_name}
Version: 1.1.3
Release: 12%{?dist}
Summary: Fast syntax highlighting for selected languages
License: MIT
URL: http://coderay.rubychan.de
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/rubychan/coderay --no-checkout
# cd coderay && git archive -v -o coderay-1.1.3-tests.txz v1.1.3 test spec
Source1: %{gem_name}-%{version}-tests.txz
# Fix test suite for ruby 3.0 change for methods on subclass of Array
# https://github.com/rubychan/coderay/pull/255
Patch0: rubygem-coderay-1.1.3-fix-tests-Array-on-ruby-3.0.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 1.8.6
BuildRequires: rubygem(test-unit)
BuildRequires: rubygem(rspec)
%if %{with shoulda}
BuildRequires: rubygem(shoulda-context)
%endif
BuildArch: noarch

%description
Fast and easy syntax highlighting for selected languages, written in Ruby.
Comes with RedCloth integration and LOC counter.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{gem_name}-%{version} -b 1

pushd ..
%patch -P0 -p1
popd

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
cp -r %{_builddir}/spec .
cp -r %{_builddir}/test .

# Comment out simplecov.
for file in \
  spec/spec_helper.rb \
  test/executable/suite.rb \
  test/functional/for_redcloth.rb \
  test/functional/suite.rb \
  test/unit/suite.rb; do
  sed -i "/^require 'simplecov'/ s/^/#/" "${file}"
done

# See https://github.com/rubychan/coderay/blob/master/rake_tasks/test.rake
LANG=C.UTF-8
ruby ./test/functional/suite.rb
ruby ./test/functional/for_redcloth.rb
ruby ./test/unit/suite.rb
# This test depends on rubygem-shoulda-context.
%if %{with shoulda}
ruby ./test/executable/suite.rb
%endif
rspec spec
popd

%files
%dir %{gem_instdir}
%{_bindir}/coderay
%license %{gem_instdir}/MIT-LICENSE
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README_INDEX.rdoc

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1.3-12
- Import
