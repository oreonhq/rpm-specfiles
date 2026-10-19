%global source1_hash 6a18d608e1524b761c541f152520323950620bae37808a1167b6859725835978
%global source0_hash 87fa0036e6369c3f3cfeca749865c2b2b63649d3b17b223d1939a8eed4841a6b
%global gem_name sqlite3
Name: rubygem-%{gem_name}
Version: 2.5.0
Release:        1%{?dist}
Summary:        Allows Ruby scripts to interface with a SQLite3 database
License: BSD-3-Clause
URL: https://github.com/sparklemotion/sqlite3-ruby
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/sparklemotion/sqlite3-ruby/archive/refs/tags/v2.5.0.tar.gz
Patch0: rubygem-sqlite3-2.5.0-fix-tests-pass-on-bigendian-architecture.patch
Patch1: rubygem-sqlite3-pr606-remove-benchmark-dep.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  ruby(release)
BuildRequires:  ruby-devel
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygems-devel
BuildRequires:  sqlite-devel
# /oreon:deps
%description
SQLite3/Ruby is a module to allow Ruby scripts to interface with a SQLite3
database.

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

# Remove bundled SQLite right away.
rm -rf ports
%gemspec_remove_file "ports/archives/sqlite-autoconf-3470200.tar.gz"

( cd %{builddir}
%patch 0 -p1
%patch 1 -p1
)

# This is not really runtime dependency, neither it is needed by official
# prebuild platform specific packages.
%gemspec_remove_dep -g mini_portile2 "~> 2.8.0"

%build

gem build ../%{gem_name}-%{version}.gemspec
CONFIGURE_ARGS="--enable-system-libraries"
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/{gem.build_complete,sqlite3} %{buildroot}%{gem_extdir_mri}/
rm -rf %{buildroot}%{gem_instdir}/ext/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
ln -s %{_builddir}/test test
mv test/test_database_uri.rb{,.disable}
ruby -I$(dirs +1)%{gem_extdir_mri}:lib:test -e 'Dir.glob "./test/test_*.rb", &method(:require)'
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-sqlite3-doc -f %{oreon_filedir}/rubygem-sqlite3-doc.list

%changelog

%autochangelog
