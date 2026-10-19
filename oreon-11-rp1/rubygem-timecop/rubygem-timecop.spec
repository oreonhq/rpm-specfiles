%global source1_hash 64e44496f1e5b2c217250f08bf98c0468cb5363382bfe9e0a4598e5731cd8dc7
%global source0_hash 12ba45ce57cdcf6b1043cb6cdffa6381fd89ce10d369c28a7f6f04dc1b0cd8eb
%global gem_name timecop
Name: rubygem-%{gem_name}
Version: 0.9.10
Release:        1%{?dist}
Summary:        Provides a unified method to mock Time.now, Date.today in a single call
License: MIT
URL: https://github.com/travisjeffery/timecop
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/travisjeffery/timecop/archive/refs/tags/v0.9.10.tar.gz
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby(release)
BuildRequires:  rubygem(activesupport)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygem(mocha)
BuildRequires:  rubygems-devel
# /oreon:deps
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
find %{_builddir} -mindepth 2 -type d \( -name test -o -name tests -o -name spec -o -name specs \) -exec cp -a {} %{_builddir}/ \;

%build

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}/
ln -s %{builddir}/test test
sed -i \
  -e '/require..bundler\/setup./ s/^/#/' \
  -e '/require .pry./ s/^/#/g' \
  test/test_helper.rb test/timecop_with_active_support_test.rb
for i in test/*_test.rb; do
  ruby -I.:lib ${i}
done
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-timecop-doc -f %{oreon_filedir}/rubygem-timecop-doc.list

%changelog

%autochangelog
