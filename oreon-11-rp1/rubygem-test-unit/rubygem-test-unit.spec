%global source1_hash c05e7356f4173236cc1491cad216ac8945bdcb10b0f274039054c2fed0d59136
%global source0_hash 6133a9754b3aad7a422e23c1d746f6165074df45dd5740a6ededa5902304561b

%global	gem_name	test-unit

# svn repository
# http://test-unit.rubyforge.org/svn/trunk/

Summary:	Improved version of Test::Unit bundled in Ruby 1.8.x
Name:		rubygem-%{gem_name}
# 3.6.0 and above is for F-39+ only as 3.5.8 and above
# changes default progress style
# (For 3.5.8 and 3.5.9, F-38 and below reverted this change)
Version:	3.7.7
Release:	2%{?dist}
# SPDX confirmed
# lib/test/unit/diff.rb is under (BSD-2-Clause OR Ruby) AND Python-2.0.1
# lib/test-unit.rb changed to BSD-2-Clause or Ruby (from 3.3.7)
# Other file: BSD-2-Clause or Ruby
License:	((BSD-2-Clause OR Ruby) AND Python-2.0.1) AND (BSD-2-Clause OR Ruby)
URL:		http://test-unit.github.io/

Source0:	http://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1:	https://github.com/test-unit/test-unit/archive/refs/tags/%{version}.tar.gz
# Source1 is created by bash %%SOURCE2
Source2:	test-unit-create-missing-files.sh

BuildRequires:	ruby(release)
BuildRequires:	rubygems
BuildRequires:	rubygems-devel
BuildRequires:	rubygem(power_assert)
# For %%check
#BuildRequires:	rubygem(rake)
#BuildRequires:	rubygem(hoe)
BuildRequires:	rubygem(bigdecimal)
BuildRequires:	rubygem(csv)
Requires:	ruby(release)
Requires:	rubygems

BuildArch:	noarch
Provides:	rubygem(%{gem_name}) = %{version}-%{release}

%description
Test::Unit 2.x - Improved version of Test::Unit bundled in
Ruby 1.8.x.
Ruby 1.9.x bundles minitest not Test::Unit. Test::Unit
bundled in Ruby 1.8.x had not been improved but unbundled
Test::Unit (Test::Unit 2.x) will be improved actively.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}

%description	doc
This package contains documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}
tar -xzf %{SOURCE1}
rm -rf test
mv %{gem_name}-%{version}/test .
rm -rf %{gem_name}-%{version}

mv ../%{gem_name}-%{version}.gemspec .

%build
gem build %{gem_name}-%{version}.gemspec
%gem_install
cp -a %{gem_name}-%{version}/test ./%{gem_instdir}

#find . -name \*.gem | xargs chmod 0644
find . -type f | xargs chmod ugo+r

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

rm -f %{buildroot}%{gem_cache}
# Keep undeleted the following files (now)??
# Needs investigation
pushd %{buildroot}%{gem_instdir}
rm -rf \
	Rakefile \
	test/ \
	%{nil}
popd

%check
pushd .%{gem_instdir}
#rake test --trace
ruby -Ilib ./test/run.rb
popd

%files
%dir	%{gem_instdir}
%license	%{gem_instdir}/BSDL
%license	%{gem_instdir}/COPYING
%license	%{gem_instdir}/PSFL
%doc	%{gem_instdir}/README.md

%{gem_libdir}
%{gem_instdir}/bin/
%{gem_spec}

%files	doc
%{gem_instdir}/doc/
%{gem_instdir}/sample/

%{gem_docdir}/

%changelog
%autochangelog
