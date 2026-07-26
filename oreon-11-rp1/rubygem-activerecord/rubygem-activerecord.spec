%global source0_hash 9b95c63b2ae9ccb57bb15db730300fdd02af387e12474eb9002a668acab3cea8

# Generated from activerecord-1.15.5.gem by gem2rpm -*- rpm-spec -*-
%global gem_name activerecord

Name: rubygem-%{gem_name}
Epoch: 1
Version: 8.0.3
Release: 2%{?dist}
Summary: Object-relational mapper framework (part of Rails)
License: MIT
URL: https://rubyonrails.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}%{?prerelease}.gem
# git clone http://github.com/rails/rails.git && cd rails/activerecord
# git archive -v -o activerecord-8.0.3-tests.tar.gz v8.0.3 test/
Source1: activerecord-%{version}%{?prerelease}-tests.tar.gz
# Fix undefined `Rails` constant in sqlite3 dbconsole.
# https://github.com/rails/rails/pull/54498
Patch0: rubygem-activerecord-8.0.1-Fix-sqlite3-dbconsole-not-working-outside-Rails.patch

# Database dump/load reuires the executable.
Suggests: %{_bindir}/sqlite3
BuildRequires: rubygems-devel
BuildRequires: ruby >= 3.2.0
BuildRequires: rubygem(bcrypt)
BuildRequires: rubygem(activesupport) = %{version}
BuildRequires: rubygem(activemodel)   = %{version}
BuildRequires: rubygem(actionpack)   = %{version}
BuildRequires: rubygem(sqlite3)
BuildRequires: rubygem(msgpack)
BuildRequires: rubygem(rack)
BuildRequires: rubygem(pg)
BuildRequires: rubygem(zeitwerk)
BuildRequires: %{_bindir}/sqlite3
BuildRequires: tzdata
BuildArch: noarch

%description
Implements the ActiveRecord pattern (Fowler, PoEAA) for ORM. It ties database
tables and classes together for business objects, like Customer or
Subscription, that can find, save, and destroy themselves without resorting to
manual SQL.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}%{?prerelease} -b 1

%patch 0 -p2

%build
gem build ../%{gem_name}-%{version}%{?prerelease}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
( cd .%{gem_instdir}
cp -a %{builddir}/test .

mkdir ../tools
# Fake strict_warnings.rb. It does not appear to be useful.
touch ../tools/strict_warnings.rb

# Run without adapters, but the default adapter is not picked up anymore
# without the `ARCONN` env variable. Not sure why :(
ARCONN=sqlite3 ruby -Itest:lib -e '
  Dir.glob("./test/cases/**/*_test.rb")
    .reject { |f| f =~ %r"/adapters/" }
    .each { |f| require f }
'

# Run tests for adapters only, but for the moment ignore those which needs
# more configuration: mysql2 trilogy postgresql
# and sqlite3_mem does not have specific test cases.
for adapter in sqlite3; do
ARCONN=sqlite3 ruby -Itest:lib -e "
  # Rails is not defined for some reason :(
  # https://github.com/rails/rails/issues/54579
  module Rails; end

  Dir.glob %|./test/cases/adapters/${adapter}/**/*_test.rb|, &method(:require)
"
done
)

%files
%dir %{gem_instdir}
%license %{gem_instdir}/MIT-LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.rdoc
%{gem_instdir}/examples

%changelog
%autochangelog
