%global source0_hash ace31dcad7134299a64d6d96310d76d32868756e58e2983e25b121acd457f1d2

# Generated from railties-3.0.3.gem by gem2rpm -*- rpm-spec -*-
%global gem_name railties

# Circular dependency with rubygem-{rails,jquery-rails,uglifier}.
%bcond_with bootstrap

Name: rubygem-%{gem_name}
Version: 8.0.3
Release: 4%{?dist}
Summary: Tools for creating, working with, and running Rails applications
License: MIT
URL: https://rubyonrails.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}%{?prerelease}.gem
# git clone http://github.com/rails/rails.git && cd rails/railties
# git archive -v -o railties-8.0.3-tests.tar.gz v8.0.3 test/
Source1: %{gem_name}-%{version}%{?prerelease}-tests.tar.gz

# Fix test compatibility with Propshaft 1.3+
# https://github.com/rails/rails/pull/55746
Patch0: rubygem-railties-8.0.3-Fix-tests-now-that-Propshaft-Server-is-a-middleware.patch
# MT6: Fix LineFiltering to work with both MT5 & MT6
# https://github.com/rails/rails/pull/56202
# https://github.com/rails/rails/commit/99395e1ea401acbc23d4f6b2a8657cdb82f921bd
Patch1: rubygem-railties-pr56202-linefiltering-minitest6.patch

# dbconsole requires the executable.
Suggests: %{_bindir}/sqlite3
# Required by generators, e.g.:
# https://github.com/rails/rails/blob/7-0-stable/railties/lib/rails/generators/rails/app/app_generator.rb#L75
Recommends: %{_bindir}/git
# Let's keep Requires and BuildRequires sorted alphabeticaly
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 3.2.0
%if %{without bootstrap}
BuildRequires: rubygem(actioncable) = %{version}
BuildRequires: rubygem(actionmailbox) = %{version}
BuildRequires: rubygem(actionmailer) = %{version}
BuildRequires: rubygem(actionpack) = %{version}
BuildRequires: rubygem(actiontext) = %{version}
BuildRequires: rubygem(activejob) = %{version}
BuildRequires: rubygem(activerecord) = %{version}
BuildRequires: rubygem(activestorage) = %{version}
BuildRequires: rubygem(activesupport) = %{version}
BuildRequires: rubygem(bootsnap)
BuildRequires: rubygem(bundler)
BuildRequires: rubygem(capybara)
BuildRequires: rubygem(dalli)
BuildRequires: rubygem(importmap-rails)
BuildRequires: rubygem(listen)
BuildRequires: rubygem(minitest-mock)
BuildRequires: rubygem(mysql2)
BuildRequires: rubygem(pg)
BuildRequires: rubygem(puma)
BuildRequires: rubygem(propshaft)
BuildRequires: rubygem(rack-cache)
BuildRequires: rubygem(rails)
BuildRequires: rubygem(rake)
BuildRequires: rubygem(selenium-webdriver)
BuildRequires: rubygem(sprockets-rails)
BuildRequires: rubygem(sqlite3)
BuildRequires: rubygem(thor)
BuildRequires: rubygem(zeitwerk)
BuildRequires: rubygem(webrick)
BuildRequires: chromedriver chromium chromium-headless
# Chromium availability is limited:
# https://src.fedoraproject.org/rpms/chromium/blob/0d9761748509bb12051ab149d28c1052cd834f87/f/chromium.spec#_800
# and chrome-headless even more:
# https://src.fedoraproject.org/rpms/chromium/blob/0d9761748509bb12051ab149d28c1052cd834f87/f/chromium.spec#_46-48
ExclusiveArch: x86_64 aarch64 noarch
BuildRequires: %{_bindir}/git
BuildRequires: %{_bindir}/postgres
BuildRequires: %{_bindir}/sqlite3
%endif
BuildArch: noarch

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

%if %{without bootstrap}
%check
# fake RAILS_FRAMEWORK_ROOT
ln -s %{gem_dir}/specifications/rails-%{version}%{?prerelease}.gemspec .%{gem_dir}/gems/rails.gemspec
ln -s ${PWD}%{gem_instdir} .%{gem_dir}/gems/railties

( cd .%{gem_dir}/gems/railties
cp -a %{builddir}/test .

mkdir ../tools
# Fake test_common.rb. It does not provide any functionality besides
# `force_skip` alias.
touch ../tools/test_common.rb
# Netiher strict_warnings.rb appears to be useful.
touch ../tools/strict_warnings.rb

# Expected by InfoTest#test_rails_version
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
# Loading Sprockets causes `Expected to find a manifest file in
#   `app/assets/config/manifest.js` (Sprockets::Railtie::ManifestNeededError)`
# error. Follow what Rails does:
# https://github.com/rails/rails/commit/1b3fc3c82e36a1c5f19f174e318166a11bd0b301
echo 'gem "sprockets-rails", require: false' >> ../Gemfile
echo 'gem "sqlite3"' >> ../Gemfile
echo 'gem "thor"' >> ../Gemfile
echo 'gem "webrick"' >> ../Gemfile
echo 'gem "zeitwerk"' >> ../Gemfile

export RUBYOPT="-I${PWD}/../railties/lib"
export PATH="${PWD}/../railties/exe:$PATH"

# Start PostgreSQL server, required by e.g.
# test/application/bin_setup_test
PG_DIR=$(mktemp -d)
PG_DATA_DIR=${PG_DIR}/data
export PGHOST=localhost
initdb -E UTF8 --no-locale -D ${PG_DATA_DIR}
pg_ctl -o "-p 5432 -k ${PG_DIR}" -D ${PG_DATA_DIR} -l ${PG_DIR}/logfile start

# Remove unneded dependency minitest/retry
sed -i -e '/require..minitest.retry./ s/^/#/' \
  test/isolation/abstract_unit.rb

# This test seems to fail due to specific sqlite3 configuration.
# https://github.com/rails/rails/issues/49928
sed -i '/test "db:drop failure because bad permissions" do$/a\          skip' \
  test/application/rake/dbs_test.rb

# TODO: Configure MySQL server to run MySQL test cases. There seems to be two
# test cases ATM:
#   railties/test/application/test_runner_test.rb:        use_mysql2
#   railties/test/commands/devcontainer_test.rb:      use_mysql2
sed -i '/def use_mysql2/a\      skip "Fedora TODO: Configure MySQL server"' test/isolation/abstract_unit.rb

# The test seems to have some issues with non interactive TTY. It works fine
# running from console.
sed -i '/def test_prompt_env_colorization/a\    skip' test/commands/console_test.rb

# TODO: package `solid_*` gem family.
sed -i -r '/require\s.solid_(cable|queue)./i\    skip' test/commands/devcontainer_test.rb

# Do not connect to the internet.
sed -i -r 's/\[bundle install\]/[bundle install --local]/' test/plugin_helpers.rb

# Skip `rubocop-rails-omakase` dependency.
sed -i -r 's/"--mountable"/"--mountable", "--skip-rubocop"/' test/engine/commands_test.rb
sed -i -r 's/"--mountable"/"--mountable", "--skip-rubocop"/' test/engine/test_test.rb

# TODO: Mismatch in RAILS_FRAMEWORK_ROOT, not sure how to fix it.
sed -i '/test "i18n files have lower priority than application ones" do$/,/^    end$/ s/^/#/' \
  test/railties/engine_test.rb

# It seems that the test either does not run in development mode, which would
# display the exception or there is some issue.
sed -i '/test "displays statement invalid template correctly" do/a\
    skip' test/application/middleware/exceptions_test.rb

# It seems that ActionMailbox does not work properly. Why?
sed -i '/^\s*def test_create_migrations/ a \  skip' \
  test/generators/action_mailbox_install_generator_test.rb

# Requires `solid_cache`.
sed -i '/test_app_update_does_not_generate_public_files/a\
    skip' test/generators/api_app_generator_test.rb

# We don't have {turbo,tailwindcss,cssbundling}-rails in Fedora.
sed -r -i '/test_(hotwire|css_option_with_(asset_pipeline_tailwind|cssbundling_gem)|app_update|application_name_is_detected_if_it_exists_and_app_folder_renamed)/a\
    skip' test/generators/app_generator_test.rb

# We don't have Rubycop in Fedora.
sed -r -i '/def test_generated_files_have_no_rubocop_warnings$/a\
    skip' test/generators/shared_generator_tests.rb

# The `bcrypt` gem is not re-added into Gemfile for some reason. Propably some
# mismatch with GEMFILE path.
sed -i '/def test_authentication_generator_without_bcrypt_in_gemfile$/a\    skip' \
  test/generators/authentication_generator_test.rb

# Drop `rubocop-rails-omakase` dependency.
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

# ActiveMailbox routes are generated for some reason :/ Might be related to the
# issues in test/generators/action_mailbox_install_generator_test.rb
mv test/commands/routes_test.rb{,.disable}

# This test is reaching for Active Storage test fixtures. While they could be
# included among sources, ignore the test for the moment.
# https://github.com/rails/rails/issues/54806
mv test/application/active_storage/uploads_integration_test.rb{,.disable}

# Tests needs to be executed in isolation. Also, use `bundle exec`, there
# is nothing to loose here and some tests depends on the Bundler (e.g.
# test/generators/app_generator_test.rb).
#
# The `$NOTIFY_SOCKET` is needed due to Puma 6+ bundling sd_notify, resulting
# in `ApplicationTests::ServerTest#test_restart_rails_server_with_custom_pid_file_path`
# test failures. Other option would be to skip this test. There is also chance
# that something is off for other reasons:
# https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/RHCFUMSMYCQ435LRPTFYDKTECHZHD4R7/
find test -type f -name '*_test.rb' -print0 | \
  sort -z | \
  xargs -0 -n1 -i sh -c "echo '* Test file: {}'; env -u NOTIFY_SOCKET bundle exec ruby -Itest -- '{}' || exit 255"

# Stop PostgreSQL server
pg_ctl -D ${PG_DATA_DIR} stop
rm -rf ${PG_DIR}
)
%endif

%files
%dir %{gem_instdir}
%{_bindir}/rails
%license %{gem_instdir}/MIT-LICENSE
%{gem_instdir}/exe
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/RDOC_MAIN.md
%doc %{gem_instdir}/README.rdoc

%changelog
%autochangelog
