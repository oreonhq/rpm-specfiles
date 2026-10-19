%global source1_hash 1a02a3ff7a8f4604c3d69838e703acfe40d668dae58f148a9341ba72a878e160
%global source0_hash 4f696fb57c90a827c20aadb2d4f9058bbff10f7f043bd0d4c3f58791143b1cd7
%global gem_name webmock
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
Release:        1%{?dist}
Summary:        Library for stubbing HTTP requests in Ruby
License: MIT
URL: https://github.com/bblimke/webmock
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/bblimke/webmock/archive/refs/tags/v3.26.1.tar.gz
Patch0: rubygem-webmock-3.23.1-Revert-Retry-timed-out-real-requests-when-running-we.patch
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
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(addressable)
BuildRequires:  rubygem(crack)
BuildRequires:  rubygem(curb)
BuildRequires:  rubygem(em-http-request)
BuildRequires:  rubygem(excon)
BuildRequires:  rubygem(hashdiff)
BuildRequires:  rubygem(httpclient)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygem(rack)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygem(test-unit)
BuildRequires:  rubygem(webrick)
BuildRequires:  rubygems-devel
# /oreon:deps
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
find %{_builddir} -mindepth 2 -type d \( -name test -o -name tests -o -name spec -o -name specs \) -exec cp -a {} %{_builddir}/ \;

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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

( cd .%{gem_instdir}
ln -s %{builddir}/minitest minitest
ln -s %{builddir}/spec spec
ln -s %{builddir}/test test
ruby -e 'Dir.glob "./minitest/**/*.rb", &method(:require)'
ruby -e 'Dir.glob "./test/**/test_*.rb", &method(:require)'
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
for i in ${ignore_list[*]}; do
  sed -i "/$i/ s/^/#/" spec/spec_helper.rb
done
rspec spec --exclude-pattern 'spec/{quality_spec.rb,acceptance/**/*}'
export HTTP_STATUS_SERVICE=http://httpstatus
for t in spec/acceptance/*/; do
  acceptance_test=$(basename ${t})
  if [[ " ${ignore_list[*]} " =~ " ${acceptance_test} " ]]; then
    echo "* ${acceptance_test} acceptance test ignored due to missing dependency"
    continue
  fi
  rspec ${t}
done
)
%files -f %{oreon_filedir}/main.list
%files -n rubygem-webmock-doc -f %{oreon_filedir}/rubygem-webmock-doc.list

%changelog

%autochangelog
