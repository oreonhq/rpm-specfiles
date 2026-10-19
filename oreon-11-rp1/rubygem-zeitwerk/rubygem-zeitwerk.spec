%global source2_hash ed70e99287355d5c6f4332f5dc5a4194458ecb34f515086a1425507cc1bd255e
%global source0_hash bb397b50c31127f8dab372fa9b21da1e7c453c5b57da172ed858136c6283f826
%global gem_name zeitwerk
Name: rubygem-%{gem_name}
Version: 2.6.6
Release:        1%{?dist}
Summary:        Efficient and thread-safe constant autoloader
License: MIT
URL: https://github.com/fxn/zeitwerk
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source2: https://github.com/fxn/zeitwerk/archive/refs/tags/v2.6.6.tar.gz
Patch0:  zeitwerk-2.6.6-minitest6.patch
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygem(minitest-mock)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Zeitwerk implements constant autoloading with Ruby semantics. Each gem
and application may have their own independent autoloader, with its own
configuration, inflector, and logger. Supports autoloading, preloading,
reloading, and eager loading.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b2
find %{_builddir} -mindepth 2 -type d \( -name test -o -name tests -o -name spec -o -name specs \) -exec cp -a {} %{_builddir}/ \;
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
ln -s %{_builddir}/test .
sed -i '/require..minitest.focus./ s/^/#/' test/test_helper.rb
sed -i '/require..minitest.reporters./ s/^/#/' test/test_helper.rb
sed -i '/Minitest::Reporters/ s/^/#/' test/test_helper.rb
sed -i '/returns true for a file in a descendant of an ignored directory/ a \
  skip' test/lib/zeitwerk/test_ignore.rb
ruby -Itest:lib -e 'Dir.glob "./test/**/test_*.rb", &method(:require)'
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-zeitwerk-doc -f %{oreon_filedir}/rubygem-zeitwerk-doc.list

%changelog

%autochangelog
