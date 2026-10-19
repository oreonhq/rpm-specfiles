%global source1_hash 0419bf47f7357e6d3da85ff4ad797a3609dcf36ff44be496162ffbc901ff4232
%global source0_hash 9b95c63b2ae9ccb57bb15db730300fdd02af387e12474eb9002a668acab3cea8
%global gem_name activerecord
Name: rubygem-%{gem_name}
Epoch: 1
Version: 8.0.3
Release:        2%{?dist}
Summary:        Object-relational mapper framework (part of Rails)
License: MIT
URL: https://rubyonrails.org
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/rails/rails/archive/refs/tags/v8.0.3.tar.gz
Patch0: rubygem-activerecord-8.0.1-Fix-sqlite3-dbconsole-not-working-outside-Rails.patch
Suggests: %{_bindir}/sqlite3
BuildArch: noarch
# oreon:deps
BuildRequires:  /usr/bin/sqlite3
BuildRequires:  ruby
BuildRequires:  rubygem(actionpack)
BuildRequires:  rubygem(activemodel)
BuildRequires:  rubygem(activesupport)
BuildRequires:  rubygem(bcrypt)
BuildRequires:  rubygem(msgpack)
BuildRequires:  rubygem(pg)
BuildRequires:  rubygem(rack)
BuildRequires:  rubygem(sqlite3)
BuildRequires:  rubygem(zeitwerk)
BuildRequires:  rubygems-devel
BuildRequires:  tzdata
# /oreon:deps
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
find %{_builddir} -mindepth 2 -type d \( -name test -o -name tests -o -name spec -o -name specs \) -exec cp -a {} %{_builddir}/ \;

%patch 0 -p2

%build

gem build ../%{gem_name}-%{version}%{?prerelease}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

( cd .%{gem_instdir}
cp -a %{builddir}/test .
mkdir ../tools
touch ../tools/strict_warnings.rb
ARCONN=sqlite3 ruby -Itest:lib -e '
  Dir.glob("./test/cases/**/*_test.rb")
    .reject { |f| f =~ %r"/adapters/" }
    .each { |f| require f }
'
for adapter in sqlite3; do
ARCONN=sqlite3 ruby -Itest:lib -e "
  module Rails; end
  Dir.glob %|./test/cases/adapters/${adapter}/**/*_test.rb|, &method(:require)
"
done
)
%files -f %{oreon_filedir}/main.list
%files -n rubygem-activerecord-doc -f %{oreon_filedir}/rubygem-activerecord-doc.list

%changelog

%autochangelog
