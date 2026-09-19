%global source0_hash 2a0444f8937c641db100128a1826554c5298ade65c62b623a1fcb34a1dc6bd2f

%global gem_name actionmailbox

Name: rubygem-%{gem_name}
Version: 8.0.3
Release: 2%{?dist}
Summary: Inbound email handling framework
License: MIT
URL: https://rubyonrails.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}%{?prerelease}.gem
# git clone http://github.com/rails/rails.git && cd rails/actionmailbox
# git archive -v -o actionmailbox-8.0.3-tests.tar.gz v8.0.3 test/
Source1: actionmailbox-%{version}%{?prerelease}-tests.tar.gz

BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 3.2.0
BuildRequires: rubygem(actionmailer) = %{version}
BuildRequires: rubygem(activerecord) = %{version}
BuildRequires: rubygem(activestorage) = %{version}
BuildRequires: rubygem(bundler)
BuildRequires: rubygem(railties) = %{version}
BuildRequires: rubygem(sqlite3)
BuildRequires: rubygem(webmock)
BuildArch: noarch

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

%build
gem build ../%{gem_name}-%{version}%{?prerelease}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
( cd .%{gem_instdir}/
cp -a %{_builddir}/test .

mkdir ../tools
# Fake test_common.rb. It does not provide any functionality besides
# `force_skip` alias.
touch ../tools/test_common.rb
# Netiher strict_warnings.rb appears to be useful.
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

# Remove asset pipeline initializer
echo > test/dummy/config/initializers/assets.rb

ruby -Itest -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
)

%files
%dir %{gem_instdir}
%license %{gem_instdir}/MIT-LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/app
%{gem_instdir}/config
%{gem_instdir}/db
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md

%changelog
%autochangelog
