%global source0_hash 8864735947b049f4185c609cb691c03a4e5a22b4ef0ead364029314558a4729d
%global gem_name dnsruby
Summary:        Ruby DNS(SEC) implementation
Name: rubygem-%{gem_name}
Version: 1.70.0
Release:        1%{?dist}
License: Apache-2.0
URL: https://github.com/alexdalitz/dnsruby
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems)
Requires: ruby
Requires: rubygem-simpleidn
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Dnsruby is a pure Ruby DNS client library. It provides a complete DNS
client implementation, including DNSSEC. It can also load (BIND) zone
files. Dnsruby has been used in OpenDNSSEC and ISC's DLV service.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}
%gem_install -n %{SOURCE0}

%build

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/
pushd %{buildroot}%{gem_instdir}
rm -rf \
     .gitignore \
     .coveralls.yml \
     .github \
     .yardopts \
     Rakefile \
     *gemspec \
     Gemfile \
     %{nil}
popd
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n rubygem-dnsruby-doc -f %{oreon_filedir}/rubygem-dnsruby-doc.list

%changelog

%autochangelog
