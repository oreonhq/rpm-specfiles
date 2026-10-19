%global source0_hash 1388d0563e13d2758c1089e35e973a3249e955c659592d10e5b77c468f628a99
%global source1_hash b8018cb91daca6396d7de17d33645d00c7f3d7fe0ad8b9fa248bb24f2ec7efe8
%global gem_name pg
Name: rubygem-%{gem_name}
Version: 1.6.3
Release:        1%{?dist}
Summary:        Pg is the Ruby interface to the PostgreSQL RDBMS
License: (BSD-2-Clause OR Ruby) AND PostgreSQL
URL: https://github.com/ged/ruby-pg
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/ged/ruby-pg/archive/refs/tags/v%{version}.tar.gz#/%{gem_name}-%{version}-spec.tar.gz
Patch0: rubygem-pg-1.3.0-remove-rpath.patch
Requires: rubygem(json)
Suggests: rubygem(bigdecimal)
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libpq-devel
BuildRequires:  postgresql-server
BuildRequires:  ruby(release)
BuildRequires:  ruby-devel
BuildRequires:  rubygem(bigdecimal)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygems-devel
# /oreon:deps
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
find %{_builddir} -mindepth 2 -type d \( -name test -o -name tests -o -name spec -o -name specs \) -exec cp -a {} %{_builddir}/ \;

%patch 0 -p1

%build

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/{gem.build_complete,*.so} %{buildroot}%{gem_extdir_mri}/
rm -rf %{buildroot}%{gem_instdir}/ext/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
ln -s %{_builddir}/spec .
export PGPORT="$((54321 + ${RANDOM} % 1000))"
export RUBY_PG_TEST_DIR=%{_builddir}/tmp
if ! ruby -S --verbose rspec -I$(dirs +1)%{gem_extdir_mri} -f d spec; then
  echo "==== [setup.log start ] ===="
  cat ${RUBY_PG_TEST_DIR}/tmp_test_specs/setup.log
  echo "==== [setup.log end ] ===="
  false
fi
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-pg-doc -f %{oreon_filedir}/rubygem-pg-doc.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.6.3-2
- Import
