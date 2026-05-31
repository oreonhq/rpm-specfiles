%global source0_hash 1388d0563e13d2758c1089e35e973a3249e955c659592d10e5b77c468f628a99
%global source1_hash 5bf95b0350adae30fd5f4984170e4ce0206c2c6bea14ba81dfb0c86f1dea417c

# Generated from pg-0.11.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name pg

Name: rubygem-%{gem_name}
Version: 1.6.3
Release: 2%{?dist}
Summary: Pg is the Ruby interface to the PostgreSQL RDBMS
License: (BSD-2-Clause OR Ruby) AND PostgreSQL
URL: https://github.com/ged/ruby-pg
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone --no-checkout https://github.com/ged/ruby-pg.git
# git archive -v -o pg-1.6.3-spec.tar.gz v1.6.3 spec/
Source1: %{gem_name}-%{version}-spec.tar.gz
# Disable RPATH.
# https://github.com/ged/ruby-pg/issues/183
Patch0: rubygem-pg-1.3.0-remove-rpath.patch
# lib/pg/text_{de,en}coder.rb
Requires: rubygem(json)
# This is optional dependency now.
# https://github.com/ged/ruby-pg/pull/556
Suggests: rubygem(bigdecimal)
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby-devel
# Compiler is required for build of gem binary extension.
# 
BuildRequires: gcc

BuildRequires: postgresql-server libpq-devel
# This is optional dependency now.
# https://github.com/ged/ruby-pg/pull/556
BuildRequires: rubygem(bigdecimal)
BuildRequires: rubygem(rspec)

%description
Pg is the Ruby interface to the PostgreSQL RDBMS. It works with PostgreSQL 10
and later.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{gem_name}-%{version} -b 1

%patch 0 -p1

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/{gem.build_complete,*.so} %{buildroot}%{gem_extdir_mri}/

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/ext/


%check
pushd .%{gem_instdir}
ln -s %{_builddir}/spec .

# Assign a random port to consider a case of multi builds in parallel in a host.
# https://github.com/ged/ruby-pg/pull/39
export PGPORT="$((54321 + ${RANDOM} % 1000))"
# Since RPM 4.20, the build path becomes too long and therefore the
# "Unix-domain socket path" hits the limit. Use some shorter path to prevent
# the issue (/tmp could be also possibility).
export RUBY_PG_TEST_DIR=%{_builddir}/tmp
# Set --verbose to show detail log by $VERBOSE.
# See https://github.com/ged/ruby-pg/blob/master/spec/helpers.rb $VERBOSE
if ! ruby -S --verbose rspec -I$(dirs +1)%{gem_extdir_mri} -f d spec; then
  echo "==== [setup.log start ] ===="
  cat ${RUBY_PG_TEST_DIR}/tmp_test_specs/setup.log
  echo "==== [setup.log end ] ===="
  false
fi
popd

%files
%dir %{gem_instdir}
%{gem_extdir_mri}
%license %{gem_instdir}/BSDL
%license %{gem_instdir}/LICENSE
%license %{gem_instdir}/POSTGRES
%{gem_libdir}
%exclude %{gem_instdir}/ports
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/Contributors.rdoc
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README-OS_X.rdoc
%doc %{gem_instdir}/README-Windows.rdoc
%lang(ja) %doc %{gem_instdir}/README.ja.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/certs
%{gem_instdir}/misc
%{gem_instdir}/pg.gemspec
%{gem_instdir}/rakelib
%{gem_instdir}/sample

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.6.3-2
- Import
