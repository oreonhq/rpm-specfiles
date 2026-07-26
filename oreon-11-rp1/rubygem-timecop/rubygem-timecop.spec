%global source0_hash fdf7938c0df4cd642382fcc17c46d8045bca185e9bb0629b73ad362abec7e293

%global gem_name timecop

Name: rubygem-%{gem_name}
Version: 0.9.10
Release: 4%{?dist}
Summary: Provides a unified method to mock Time.now, Date.today in a single call
License: MIT
URL: https://github.com/travisjeffery/timecop
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/travisjeffery/timecop.git && cd timecop
# git archive -v -o timecop-0.9.10-test.tar.gz v0.9.10 test/
Source1: %{gem_name}-%{version}-test.tar.gz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: rubygem(activesupport)
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(mocha)
BuildArch: noarch

%description
A gem providing "time travel" and "time freezing" capabilities, making it dead
simple to test time-dependent code.  It provides a unified method to mock
Time.now, Date.today, and DateTime.now in a single call.

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
pushd .%{gem_instdir}/
ln -s %{builddir}/test test

# Drop Bundler and minitest-rg dependency.
sed -i \
  -e '/require..bundler\/setup./ s/^/#/' \
  -e '/require .pry./ s/^/#/g' \
  test/test_helper.rb test/timecop_with_active_support_test.rb

# The test cases must be executed independently.
for i in test/*_test.rb; do
  ruby -I.:lib ${i}
done
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.markdown
%{gem_instdir}/Rakefile

%changelog
%autochangelog
