%global source1_hash dfbf1dbe06d1646ed36ac740e50f27ebb76c5b7f85205918813dc60246cee655
%global source0_hash 8daf828cc77bcf7d63b0e3bdb6caa47e2272dcfaf4fbfe46f8c3a9df087a829b
%global gem_name tzinfo
Name: rubygem-%{gem_name}
Version: 2.0.6
Release:        1%{?dist}
Summary:        Time Zone Library
License: MIT
URL: https://tzinfo.github.io
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/tzinfo/tzinfo/archive/refs/tags/v2.0.6.tar.gz
Patch0:  %{gem_name}-2.0.6-minitest6.patch
Recommends: tzdata
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(concurrent-ruby)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygem(minitest-mock)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
TZInfo provides access to time zone data and allows times to be converted
using time zone rules.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b1
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
sed -i "/raise 'Tests must be run with bundler/ s/^/#/" \
  test/test_utils.rb
export RUBYOPT="-Ilib"
ruby test/ts_all_ruby_format1.rb
ruby test/ts_all_ruby_format2.rb
ruby test/ts_all_zoneinfo.rb
sed -i '/zoneinfo_path/ s|= .*|= "%{_datadir}/zoneinfo"|' test/ts_all_zoneinfo.rb
ruby test/ts_all_zoneinfo.rb || :
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-tzinfo-doc -f %{oreon_filedir}/rubygem-tzinfo-doc.list

%changelog

%autochangelog
