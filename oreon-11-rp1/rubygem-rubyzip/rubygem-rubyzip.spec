%global source0_hash c0ed99385f0625415c8f05bcae33fe649ed2952894a95ff8b08f26ca57ea5b3c

# Generated from rubyzip-1.1.7.gem by gem2rpm -*- rpm-spec -*-
%global gem_name rubyzip

Name: rubygem-%{gem_name}
Version: 3.2.2
Release: 3%{?dist}
Summary: A ruby module for reading and writing zip files
License: Ruby OR BSD-2-Clause
URL: http://github.com/rubyzip/rubyzip
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/rubyzip/rubyzip.git --no-checkout
# cd rubyzip && git archive -v -o rubyzip-3.2.2-test.tar.gz v3.2.2 test/
Source1: %{gem_name}-%{version}-test.tar.gz
# Fix compatibility with minitest 6
Patch0:  rubyzip-3.2.2-minitest6.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(minitest-mock)
BuildArch: noarch

%description
A ruby module for reading and writing zip files.

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
%patch -P0 -p1
)

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
cp -a %{_builddir}/test .

# `FULL_ZIP64_TEST` enables additional two slow test cases.
FULL_ZIP64_TEST=1 ruby -Ilib:test -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE.md
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/Changelog.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/rubyzip.gemspec
%{gem_instdir}/samples

%changelog
%autochangelog
