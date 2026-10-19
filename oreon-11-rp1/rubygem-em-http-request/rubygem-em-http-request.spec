%global source0_hash 16fbc72b2a6e20c804c564ac5d12e98668c6fcef8c3b1dd2387dff505f2efdab
%global gem_name em-http-request
Name: rubygem-%{gem_name}
Version: 1.1.7
Release:        1%{?dist}
Summary:        EventMachine based, async HTTP Request client
License: MIT
URL: http://github.com/igrigorik/em-http-request
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch0: %{name}-%{version}-explicit-keyword-argument.patch
Patch1: em-http-request-1.1.7-Also-stop-the-HTTP-parser-in-addition-to-resetting.patch
Patch2: rubygem-em-http-request-1.1.7-Compatibility-with-Rack-3.patch
BuildArch: noarch
# oreon:deps
BuildRequires:  /usr/bin/ping
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(addressable)
BuildRequires:  rubygem(cookiejar)
BuildRequires:  rubygem(em-socksify)
BuildRequires:  rubygem(eventmachine)
BuildRequires:  rubygem(http_parser.rb)
BuildRequires:  rubygem(multi_json)
BuildRequires:  rubygem(rack)
BuildRequires:  rubygem(rackup)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygem(webrick)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
EventMachine based, async HTTP Request client.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}

%patch 0 -p1
%patch 1 -p1
%patch 2 -p1

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
sed -i "/require 'bundler\/setup'/ s/^/#/" spec/helper.rb
sed -i "/^require 'helper'/i require 'pathname'" spec/client_spec.rb
sed -i '/it "should report error if connection was closed by server on client keepalive requests" do/ ,/^  end$/ s/^/#/' spec/client_spec.rb
sed -i '/it "should set content-length to 0 on posts with empty bodies" do/ ,/^  end$/ s/^/#/' spec/client_spec.rb
sed -i '/it "should keep default https port in redirect url that include it"/ ,/^  end$/ s/^/#/' spec/redirect_spec.rb
sed -i '/it "should keep default http port in redirect url that include it"/ ,/^  end$/ s/^/#/' spec/redirect_spec.rb
sed -i '/it "should fail gracefully on an invalid host in Location header" do/ ,/^  end$/ s/^/#/' spec/dns_spec.rb
LANG=C.UTF-8 rspec spec -f d
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-em-http-request-doc -f %{oreon_filedir}/rubygem-em-http-request-doc.list

%changelog

%autochangelog
