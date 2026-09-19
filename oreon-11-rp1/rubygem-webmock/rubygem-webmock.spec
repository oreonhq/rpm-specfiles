%global source0_hash 21555b279f68b5c0337b8b6c404ed081b5218b3f376045cb25cd93f8739dae40

# Generated from webmock-1.7.6.gem by gem2rpm -*- rpm-spec -*-
%global gem_name webmock

# Disable HTTP clients integration tests we don't have in Fedora.
%bcond_with    async_http
%bcond_without curb
%bcond_without em_http_request
%bcond_without excon
%bcond_with    http_rb
%bcond_without httpclient
%bcond_with    manticore
%bcond_without net_http
%bcond_with    patron
%bcond_with    typhoeus

Name: rubygem-%{gem_name}
Version: 3.26.1
Release: 1%{?dist}
Summary: Library for stubbing HTTP requests in Ruby
License: MIT
URL: https://github.com/bblimke/webmock
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/bblimke/webmock.git && cd webmock
# git archive -v -o webmock-3.26.1-tests.tar.gz v3.26.1 minitest/ spec/ test/
Source1: %{gem_name}-%{version}-tests.tar.gz
# Revert dependency on rspec-retry, because it is not available in Fedora
Patch0: rubygem-webmock-3.23.1-Revert-Retry-timed-out-real-requests-when-running-we.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(addressable)
BuildRequires: rubygem(crack)
BuildRequires: rubygem(hashdiff)
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(rack)
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(test-unit)
BuildRequires: rubygem(webrick)

%{?with_async_http:BuildRequires: rubygem(async-http)}
%{?with_curb:BuildRequires: rubygem(curb)}
%{?with_em_http_request:BuildRequires: rubygem(em-http-request)}
%{?with_excon:BuildRequires: rubygem(excon)}
%{?with_http_rb:BuildRequires: rubygem(http_rb)}
%{?with_httpclient:BuildRequires: rubygem(httpclient)}
%{?with_manticore:BuildRequires: rubygem(manticore)}
%{?with_patron:BuildRequires: rubygem(patron)}
%{?with_typhoeus:BuildRequires: rubygem(typhoeus)}
BuildArch: noarch

%description
WebMock allows stubbing HTTP requests and setting expectations on HTTP
requests.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b 1

# JSON is required by lib/webmock/request_body_diff.rb
%gemspec_add_dep -g json

( cd %{builddir}
%patch 0 -p1
)

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

# Run the test suite
%check
( cd .%{gem_instdir}

ln -s %{builddir}/minitest minitest
ln -s %{builddir}/spec spec
ln -s %{builddir}/test test

ruby -e 'Dir.glob "./minitest/**/*.rb", &method(:require)'
ruby -e 'Dir.glob "./test/**/test_*.rb", &method(:require)'

# Create list of dependencies to ignore based on bcond flags.
ignore_list=(
%{with_async_http_client}
%{with_curb}
%{with_em_http_request}
%{with_excon}
%{with_http_rb}
%{with_httpclient}
%{with_manticore}
%{with_net_http}
%{with_patron}
%{with_typhoeus}
)
ignore_list=($(echo ${ignore_list[*]} | \
  sed 's/1//g' | \
  sed -r 's/%\{with_([^{]*)\}/\1/g'
))

# Remove unavailable dependencies based on ignore_list.
for i in ${ignore_list[*]}; do
  sed -i "/$i/ s/^/#/" spec/spec_helper.rb
done

# and we don't care about code quality, that's upstream business.
rspec spec --exclude-pattern 'spec/{quality_spec.rb,acceptance/**/*}'

# The Curb test suite fails without this export since 3.25.2 🤷
# https://github.com/bblimke/webmock/issues/1118
export HTTP_STATUS_SERVICE=http://httpstatus

# Run acceptance test for each http client independently.
for t in spec/acceptance/*/; do
  acceptance_test=$(basename ${t})
  if [[ " ${ignore_list[*]} " =~ " ${acceptance_test} " ]]; then
    echo "* ${acceptance_test} acceptance test ignored due to missing dependency"
    continue
  fi
  rspec ${t}
done

)

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md

%changelog
%autochangelog
