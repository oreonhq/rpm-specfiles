%global source1_hash c05e7356f4173236cc1491cad216ac8945bdcb10b0f274039054c2fed0d59136
%global source0_hash 3c89d5ff0690a16bef9946156c4624390402b9d54dfcf4ce9cbd5b06bead1e45
%global	gem_name	test-unit
Summary:        Improved version of Test::Unit bundled in Ruby 1.8.x
Name:		rubygem-%{gem_name}
Version:	3.7.7
Release:        1%{?dist}
License:	((BSD-2-Clause OR Ruby) AND Python-2.0.1) AND (BSD-2-Clause OR Ruby)
URL:		http://test-unit.github.io/
Source0:        http://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1:	https://github.com/test-unit/test-unit/archive/refs/tags/%{version}.tar.gz
Source2:	test-unit-create-missing-files.sh
Requires:	ruby(release)
Requires:	rubygems
BuildArch:	noarch
Provides:	rubygem(%{gem_name}) = %{version}-%{release}
# oreon:deps
BuildRequires:  ruby(release)
BuildRequires:  rubygem(bigdecimal)
BuildRequires:  rubygem(csv)
BuildRequires:  rubygem(power_assert)
BuildRequires:  rubygems
BuildRequires:  rubygems-devel
# /oreon:deps
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
find %{_builddir} -mindepth 2 -type d \( -name test -o -name tests -o -name spec -o -name specs \) -exec cp -a {} %{_builddir}/ \;
tar -xzf %{SOURCE1}
rm -rf test
mv %{gem_name}-%{version}/test .
rm -rf %{gem_name}-%{version}

mv ../%{gem_name}-%{version}.gemspec .

%build

gem build %{gem_name}-%{version}.gemspec
%gem_install
cp -a test ./%{gem_instdir}
find . -type f | xargs chmod ugo+r
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/
rm -f %{buildroot}%{gem_cache}
pushd %{buildroot}%{gem_instdir}
rm -rf \
	Rakefile \
	test/ \
	%{nil}
popd
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
ruby -Ilib ./test/run.rb
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-test-unit-doc -f %{oreon_filedir}/rubygem-test-unit-doc.list

%changelog

%autochangelog
