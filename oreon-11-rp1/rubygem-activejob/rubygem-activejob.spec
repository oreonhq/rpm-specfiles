%global source0_hash d14aa5ca8903c86be596e20a58a92a8130357c5f257cc7fe7bc6d502c05c5d5b

# Generated from activejob-4.2.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name activejob

Name: rubygem-%{gem_name}
Version: 8.0.3
Release: 3%{?dist}
Summary: Job framework with pluggable queues
License: MIT
URL: https://rubyonrails.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}%{?prerelease}.gem
# git clone https://github.com/rails/rails.git && cd rails/activejob
# git archive -v -o activejob-8.0.3-tests.tar.gz v8.0.3 test/
Source1: %{gem_name}-%{version}%{?prerelease}-tests.tar.gz

BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 3.2.0
BuildRequires: rubygem(activesupport) = %{version}
BuildRequires: rubygem(globalid)
BuildRequires: rubygem(minitest-mock)
BuildRequires: rubygem(zeitwerk)
BuildRequires: tzdata
BuildArch: noarch

%description
Declare job classes that can be run by a variety of queuing backends.

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
( cd .%{gem_instdir}
cp -a %{builddir}/test .

mkdir ../tools
# Fake test_common.rb. It does not provide any functionality besides
# `force_skip` alias.
touch ../tools/test_common.rb
# Netiher strict_warnings.rb appears to be useful.
touch ../tools/strict_warnings.rb

# We don't have isneakers in Fedora.
sed -i '/ActiveJob::QueueAdapters::SneakersAdapter/ d' test/cases/exceptions_test.rb

ADAPTERS='async inline test'
for ADAPTER in ${ADAPTERS}; do
  # Reject test cases similarly to what upstream does:
  # https://github.com/rails/rails/blob/ce359806416550c3b1b790c116aee5f0f9a182d4/activejob/Rakefile#L39-L42
  AJ_ADAPTER=${ADAPTER} ruby -Ilib:test -e '
    Dir.glob("./test/cases/**/*_test.rb").reject { |t|
      (t.include?("delayed_job") && ENV["AJ_ADAPTER"] != "delayed_job") ||
      (t.include?("async") && ENV["AJ_ADAPTER"] != "async")
    }.each { |t| require t }'

  # Do not execute integration tests, otherwise Rails's generators are required.
  # AJ_INTEGRATION_TESTS=1 AJ_ADAPTER=${ADAPTER} ruby -Ilib:test -e 'Dir.glob "./test/integration/**/*_test.rb", &method(:require)'
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
%doc %{gem_instdir}/README.md

%changelog
%autochangelog
