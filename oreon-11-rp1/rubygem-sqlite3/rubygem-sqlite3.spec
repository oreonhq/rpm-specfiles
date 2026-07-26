%global source0_hash 5c61aed445ac44d0c298247adc01ea7a2af932cf0f4590883a600de04a5e5f7c

%global gem_name sqlite3

Name: rubygem-%{gem_name}
Version: 2.5.0
Release: 5%{?dist}
Summary: Allows Ruby scripts to interface with a SQLite3 database
License: BSD-3-Clause
URL: https://github.com/sparklemotion/sqlite3-ruby
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/sparklemotion/sqlite3-ruby.git && cd sqlite3-ruby
# git archive -v -o sqlite3-2.5.0-test.tar.gz v2.5.0 test/
Source1: %{gem_name}-%{version}-test.tar.gz
# Fix (s390x) big endian tees failure.
# https://github.com/sparklemotion/sqlite3-ruby/pull/616
Patch0: rubygem-sqlite3-2.5.0-fix-tests-pass-on-bigendian-architecture.patch
# Remove benchmark dependency for ruby3_5
# https://github.com/sparklemotion/sqlite3-ruby/pull/606
# https://github.com/sparklemotion/sqlite3-ruby/commit/e2bb2a9bc6b4729a2fef135f7eb4f7b3b41e03d4
Patch1: rubygem-sqlite3-pr606-remove-benchmark-dep.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby-devel
BuildRequires: sqlite-devel
BuildRequires: rubygem(minitest) >= 5.0.0
BuildRequires: gcc

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
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# Build against system SQLite3.
CONFIGURE_ARGS="--enable-system-libraries"

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/{gem.build_complete,sqlite3} %{buildroot}%{gem_extdir_mri}/

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/ext/

%check
pushd .%{gem_instdir}
ln -s %{_builddir}/test test

# Fedora SQLite does not support URI.
# https://github.com/sparklemotion/sqlite3-ruby/issues/611
mv test/test_database_uri.rb{,.disable}

ruby -I$(dirs +1)%{gem_extdir_mri}:lib:test -e 'Dir.glob "./test/test_*.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%{gem_extdir_mri}
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/FAQ.md
%doc %{gem_instdir}/INSTALLATION.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/dependencies.yml

%changelog
%autochangelog
