%global source1_hash 0419bf47f7357e6d3da85ff4ad797a3609dcf36ff44be496162ffbc901ff4232
%global source0_hash 2a0444f8937c641db100128a1826554c5298ade65c62b623a1fcb34a1dc6bd2f
%global gem_name actionmailbox
Name: rubygem-%{gem_name}
Version: 8.0.3
Release:        1%{?dist}
Summary:        Inbound email handling framework
License: MIT
URL: https://rubyonrails.org
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/rails/rails/archive/refs/tags/v8.0.3.tar.gz
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(actionmailer)
BuildRequires:  rubygem(activerecord)
BuildRequires:  rubygem(activestorage)
BuildRequires:  rubygem(bundler)
BuildRequires:  rubygem(railties)
BuildRequires:  rubygem(sqlite3)
BuildRequires:  rubygem(webmock)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Receive and process incoming emails in Rails applications.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}%{?prerelease} -b1
find %{_builddir} -mindepth 2 -type d \( -name test -o -name tests -o -name spec -o -name specs \) -exec cp -a {} %{_builddir}/ \;

%build

gem build ../%{gem_name}-%{version}%{?prerelease}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

( cd .%{gem_instdir}/
cp -a %{_builddir}/test .
mkdir ../tools
touch ../tools/test_common.rb
touch ../tools/strict_warnings.rb
export BUNDLE_GEMFILE=${PWD}/../Gemfile
cat > $BUNDLE_GEMFILE <<EOF
gem "railties"
gem "actionmailer"
gem "activerecord"
gem "activestorage"
gem "sqlite3"
gem "webmock"
EOF
echo > test/dummy/config/initializers/assets.rb
ruby -Itest -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
)
%files -f %{oreon_filedir}/main.list
%files -n rubygem-actionmailbox-doc -f %{oreon_filedir}/rubygem-actionmailbox-doc.list

%changelog

%autochangelog
