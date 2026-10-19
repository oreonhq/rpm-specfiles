%global source1_hash 0419bf47f7357e6d3da85ff4ad797a3609dcf36ff44be496162ffbc901ff4232
%global source0_hash 469eddb3822aff1c6a0df0bd3398f28bff8fcd1bd0e9d309e6b7ccbd0bdba1b6
%global gem_name activejob
Name: rubygem-%{gem_name}
Version: 8.0.3
Release:        1%{?dist}
Summary:        Job framework with pluggable queues
License: MIT
URL: https://rubyonrails.org
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/rails/rails/archive/refs/tags/v8.0.3.tar.gz
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(activesupport)
BuildRequires:  rubygem(globalid)
BuildRequires:  rubygem(minitest-mock)
BuildRequires:  rubygem(zeitwerk)
BuildRequires:  rubygems-devel
BuildRequires:  tzdata
# /oreon:deps
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

( cd .%{gem_instdir}
cp -a %{builddir}/test .
mkdir ../tools
touch ../tools/test_common.rb
touch ../tools/strict_warnings.rb
sed -i '/ActiveJob::QueueAdapters::SneakersAdapter/ d' test/cases/exceptions_test.rb
ADAPTERS='async inline test'
for ADAPTER in ${ADAPTERS}; do
  AJ_ADAPTER=${ADAPTER} ruby -Ilib:test -e '
    Dir.glob("./test/cases/**/*_test.rb").reject { |t|
      (t.include?("delayed_job") && ENV["AJ_ADAPTER"] != "delayed_job") ||
      (t.include?("async") && ENV["AJ_ADAPTER"] != "async")
    }.each { |t| require t }'
done
)
%files -f %{oreon_filedir}/main.list
%files -n rubygem-activejob-doc -f %{oreon_filedir}/rubygem-activejob-doc.list

%changelog

%autochangelog
