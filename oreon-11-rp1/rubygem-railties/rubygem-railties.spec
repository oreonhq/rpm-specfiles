%global source1_hash 0419bf47f7357e6d3da85ff4ad797a3609dcf36ff44be496162ffbc901ff4232
%global source0_hash ace31dcad7134299a64d6d96310d76d32868756e58e2983e25b121acd457f1d2
%global gem_name railties
%bcond_with bootstrap
Name: rubygem-%{gem_name}
Version: 8.0.3
Release:        4%{?dist}
Summary:        Tools for creating, working with, and running Rails applications
License: MIT
URL: https://rubyonrails.org
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/rails/rails/archive/refs/tags/v8.0.3.tar.gz
Patch0: rubygem-railties-8.0.3-Fix-tests-now-that-Propshaft-Server-is-a-middleware.patch
Patch1: rubygem-railties-pr56202-linefiltering-minitest6.patch
Suggests: %{_bindir}/sqlite3
Recommends: %{_bindir}/git
%if %{without bootstrap}
ExclusiveArch: x86_64 aarch64 noarch
%endif
BuildArch: noarch
# oreon:deps
BuildRequires:  /usr/bin/git
BuildRequires:  /usr/bin/postgres
BuildRequires:  /usr/bin/sqlite3
BuildRequires:  chromedriver
BuildRequires:  chromium
BuildRequires:  chromium-headless
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(actioncable)
BuildRequires:  rubygem(actionmailbox)
BuildRequires:  rubygem(actionmailer)
BuildRequires:  rubygem(actionpack)
BuildRequires:  rubygem(actiontext)
BuildRequires:  rubygem(activejob)
BuildRequires:  rubygem(activerecord)
BuildRequires:  rubygem(activestorage)
BuildRequires:  rubygem(activesupport)
BuildRequires:  rubygem(bootsnap)
BuildRequires:  rubygem(bundler)
BuildRequires:  rubygem(capybara)
BuildRequires:  rubygem(dalli)
BuildRequires:  rubygem(importmap-rails)
BuildRequires:  rubygem(listen)
BuildRequires:  rubygem(minitest-mock)
BuildRequires:  rubygem(mysql2)
BuildRequires:  rubygem(pg)
BuildRequires:  rubygem(propshaft)
BuildRequires:  rubygem(puma)
BuildRequires:  rubygem(rack-cache)
BuildRequires:  rubygem(rails)
BuildRequires:  rubygem(rake)
BuildRequires:  rubygem(selenium-webdriver)
BuildRequires:  rubygem(sprockets-rails)
BuildRequires:  rubygem(sqlite3)
BuildRequires:  rubygem(thor)
BuildRequires:  rubygem(webrick)
BuildRequires:  rubygem(zeitwerk)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Rails internals: application bootup, plugins, generators, and rake tasks.
Railties is responsible to glue all frameworks together. Overall, it:
* handles all the bootstrapping process for a Rails application;
* manages rails command line interface;
* provides Rails generators core;

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
%patch 1 -p2

( cd %{builddir}
%patch 0 -p2
)

%build

gem build ../%{gem_name}-%{version}%{?prerelease}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/
find %{buildroot}%{gem_instdir}/exe -type f | xargs chmod a+x
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{without bootstrap}
%check

ln -s %{gem_dir}/specifications/rails-%{version}%{?prerelease}.gemspec .%{gem_dir}/gems/rails.gemspec
ln -s ${PWD}%{gem_instdir} .%{gem_dir}/gems/railties
( cd .%{gem_dir}/gems/railties
cp -a %{builddir}/test .
mkdir ../tools
touch ../tools/test_common.rb
touch ../tools/strict_warnings.rb
echo '%{version}%{?prerelease}' > ../RAILS_VERSION
touch ../Gemfile
echo 'gem "actioncable"' >> ../Gemfile
echo 'gem "actionmailbox"' >> ../Gemfile
echo 'gem "actionmailer"' >> ../Gemfile
echo 'gem "actionpack"' >> ../Gemfile
echo 'gem "actiontext"' >> ../Gemfile
echo 'gem "activejob"' >> ../Gemfile
echo 'gem "activerecord"' >> ../Gemfile
echo 'gem "activestorage"' >> ../Gemfile
echo 'gem "activesupport"' >> ../Gemfile
echo 'gem "bootsnap"' >> ../Gemfile
echo 'gem "capybara"' >> ../Gemfile
echo 'gem "dalli"' >> ../Gemfile
echo 'gem "importmap-rails"' >> ../Gemfile
echo 'gem "listen"' >> ../Gemfile
echo 'gem "minitest-mock"' >> ../Gemfile
echo 'gem "mysql2"' >> ../Gemfile
echo 'gem "pg"' >> ../Gemfile
echo 'gem "propshaft"' >> ../Gemfile
echo 'gem "puma"' >> ../Gemfile
echo 'gem "rack-cache"' >> ../Gemfile
echo 'gem "rails"' >> ../Gemfile
echo 'gem "rake"' >> ../Gemfile
echo 'gem "selenium-webdriver"' >> ../Gemfile
echo 'gem "sprockets-rails", require: false' >> ../Gemfile
echo 'gem "sqlite3"' >> ../Gemfile
echo 'gem "thor"' >> ../Gemfile
echo 'gem "webrick"' >> ../Gemfile
echo 'gem "zeitwerk"' >> ../Gemfile
export RUBYOPT="-I${PWD}/../railties/lib"
export PATH="${PWD}/../railties/exe:$PATH"
PG_DIR=$(mktemp -d)
PG_DATA_DIR=${PG_DIR}/data
export PGHOST=localhost
initdb -E UTF8 --no-locale -D ${PG_DATA_DIR}
pg_ctl -o "-p 5432 -k ${PG_DIR}" -D ${PG_DATA_DIR} -l ${PG_DIR}/logfile start
sed -i -e '/require..minitest.retry./ s/^/#/' \
  test/isolation/abstract_unit.rb
sed -i '/test "db:drop failure because bad permissions" do$/a\          skip' \
  test/application/rake/dbs_test.rb
sed -i '/def use_mysql2/a\      skip "Fedora TODO: Configure MySQL server"' test/isolation/abstract_unit.rb
sed -i '/def test_prompt_env_colorization/a\    skip' test/commands/console_test.rb
sed -i -r '/require\s.solid_(cable|queue)./i\    skip' test/commands/devcontainer_test.rb
sed -i -r 's/\[bundle install\]/[bundle install --local]/' test/plugin_helpers.rb
sed -i -r 's/"--mountable"/"--mountable", "--skip-rubocop"/' test/engine/commands_test.rb
sed -i -r 's/"--mountable"/"--mountable", "--skip-rubocop"/' test/engine/test_test.rb
sed -i '/test "i18n files have lower priority than application ones" do$/,/^    end$/ s/^/#/' \
  test/railties/engine_test.rb
sed -i '/test "displays statement invalid template correctly" do/a\
    skip' test/application/middleware/exceptions_test.rb
sed -i '/^\s*def test_create_migrations/ a \  skip' \
  test/generators/action_mailbox_install_generator_test.rb
sed -i '/test_app_update_does_not_generate_public_files/a\
    skip' test/generators/api_app_generator_test.rb
sed -r -i '/test_(hotwire|css_option_with_(asset_pipeline_tailwind|cssbundling_gem)|app_update|application_name_is_detected_if_it_exists_and_app_folder_renamed)/a\
    skip' test/generators/app_generator_test.rb
sed -r -i '/def test_generated_files_have_no_rubocop_warnings$/a\
    skip' test/generators/shared_generator_tests.rb
sed -i '/def test_authentication_generator_without_bcrypt_in_gemfile$/a\    skip' \
  test/generators/authentication_generator_test.rb
sed -i -r \
  -e '/def test_ensure_that_migration_tasks_work_with_mountable_option$/,/^  end/ s/"--mountable"/"--mountable", "--skip-rubocop"/' \
  -e '/def test_plugin_passes_generated_test$/,/^  end/ s/(run_generator)/\1 [destination_root, "--skip-rubocop"]/' \
  test/generators/plugin_generator_test.rb
sed -i -r '/generate_plugin\(/ s/\)$/, "--skip-rubocop")/' \
  test/generators/plugin_test_runner_test.rb
sed -i -r '/with_new_plugin\(/ s/\)/, "--skip-rubocop")/' \
  test/generators/scaffold_controller_generator_test.rb
sed -i -r '/with_new_plugin\(/ s/\)/, "--skip-rubocop")/' \
  test/generators/scaffold_generator_test.rb
sed -i -r '/generate_plugin\(/ s/\)$/, "--skip-rubocop")/' \
  test/generators/test_runner_in_engine_test.rb
mv test/commands/routes_test.rb{,.disable}
mv test/application/active_storage/uploads_integration_test.rb{,.disable}
find test -type f -name '*_test.rb' -print0 | \
  sort -z | \
  xargs -0 -n1 -i sh -c "echo '* Test file: {}'; env -u NOTIFY_SOCKET bundle exec ruby -Itest -- '{}' || exit 255"
pg_ctl -D ${PG_DATA_DIR} stop
rm -rf ${PG_DIR}
)
%endif
%files -f %{oreon_filedir}/main.list
%files -n rubygem-railties-doc -f %{oreon_filedir}/rubygem-railties-doc.list

%changelog

%autochangelog
