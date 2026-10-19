%global source2_hash 563b7cc977204fae61bfcfb41d6a4a23aabdf972db04371da87e3d2429da52f7
%global source1_hash 5311e58497cab497b0abd92d3f221548dfe887328b85990133905f9ceb906da0
%global source0_hash 381aee04fcc9effbe5fa7cc703d8f5f20293722f987ded4f958f77514cd29373
%global gem_name faraday
Name: rubygem-%{gem_name}
Version: 1.0.1
Release:        19%{?dist}
Summary:        HTTP/REST API client library
License: MIT
URL: https://lostisland.github.io/faraday
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://raw.githubusercontent.com/danabr/multipart-parser/master/lib/multipart_parser/parser.rb
Source2: https://raw.githubusercontent.com/danabr/multipart-parser/master/lib/multipart_parser/reader.rb
Patch0: rubygem-faraday-1.0.1-Properly-fix-test-failure-with-Rack-2.1.patch
Patch1: faraday-1.0.1-net-http-persistent-3-error-kind.patch
Patch2: faraday-pr1523-testsuite-undefined-method-change.patch
Patch3: faraday-pr1560-ruby34-backtrace-change.patch
Patch4: faraday-pr1604-ruby34-hash-inspect-formatting-change.patch
Patch5: faraday-rack-pr13-rack31-rack_input.patch
Patch6: faraday-pr1549-unespace-rack-utils-query-result.patch
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(em-http-request)
BuildRequires:  rubygem(excon)
BuildRequires:  rubygem(httpclient)
BuildRequires:  rubygem(multipart-post)
BuildRequires:  rubygem(net-http-persistent)
BuildRequires:  rubygem(rack)
BuildRequires:  rubygem(rack-test)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygem(typhoeus)
BuildRequires:  rubygem(webmock)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
HTTP/REST API client library.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

mkdir -p multipart_parser/multipart_parser
cp %{SOURCE1} %{SOURCE2} multipart_parser/multipart_parser

%autosetup -n %{gem_name}-%{version} -p1

%build

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
sed -i "/simplecov/ s/^/#/" spec/spec_helper.rb
sed -i "/coveralls/ s/^/#/" spec/spec_helper.rb
sed -i "/SimpleCov/,/^end$/ s/^/#/" spec/spec_helper.rb
sed -i "/pry/ s/^/#/" spec/spec_helper.rb
mv spec/faraday/adapter/em_synchrony_spec.rb{,.disabled}
mv spec/faraday/adapter/patron_spec.rb{,.disabled}
sed -i '/allows to set min_version in SSL settings/a\      skip' \
  spec/faraday/adapter/net_http_persistent_spec.rb
rspec -I%{_builddir}/multipart_parser -rspec_helper -r%{SOURCE1} spec -f d
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-faraday-doc -f %{oreon_filedir}/rubygem-faraday-doc.list

%changelog

%autochangelog
