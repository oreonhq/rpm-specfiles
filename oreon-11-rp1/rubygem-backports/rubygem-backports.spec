%global source0_hash b55be1ebf02d64488be71b3f82c30fbd51a3d461e8f7c39dc2d466a049adbd1d

# Generated from backports-2.5.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name backports

Name: rubygem-%{gem_name}
Version: 3.23.0
Release: 10%{?dist}
Summary: Backports of Ruby features for older Ruby
License: MIT
URL: http://github.com/marcandre/backports
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/marcandre/backports.git && cd backports
# git archive -v -o backports-3.23.0-tests.tar.gz v3.23.0 test/
Source1: %{gem_name}-%{version}-tests.tar.gz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(test-unit)
BuildArch: noarch

%description
Essential backports that enable many of the nice features of Ruby for earlier
versions.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b 1

%build
gem build ../%{gem_name}-%{version}.gemspec

%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
# Move the tests into place
ln -s %{_builddir}/test test

# TODO: More test could be enabled, if MSpec and RubySpec are available
# in Fedora.

# ref: https://github.com/marcandre/backports/issues/198
# Upstream simply disabled Ractor related tests
mv test/ractor_extra_test.rb{,.skip}
ruby -Ilib -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
mv test/ractor_extra_test.rb{.skip,}
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/SECURITY.md
%{gem_instdir}/backports.gemspec

%changelog
%autochangelog
